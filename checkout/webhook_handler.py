from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        print(">>> SENDING EMAIL NOW <<<")
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [order.email]
        )

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.get('bag')
        save_info = intent.metadata.get('save_info')
        order_id = intent.metadata.get('order_id')
        username = intent.metadata.get('username')
        shipping_details = intent.get("shipping", {})

        try:
            stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
            billing_details = stripe_charge.billing_details
            grand_total = round(stripe_charge.amount / 100, 2)
        except Exception as e:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR retrieving charge: {e}',
                status=400
            )

        shipping_details = intent.get("shipping", {})
        for field, value in shipping_details.get("address", {}).items():
            if value == "":
                shipping_details["address"][field] = None

        profile = None
        if username and username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.get("phone")
                profile.default_country = shipping_details.get("address", {}).get("country")
                profile.default_postcode = shipping_details.get("address", {}).get("postal_code")
                profile.default_town_or_city = shipping_details.get("address", {}).get("city")
                profile.default_street_address1 = shipping_details.get("address", {}).get("line1")
                profile.default_street_address2 = shipping_details.get("address", {}).get("line2")
                profile.default_county = shipping_details.get("address", {}).get("state")
                profile.save()

        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                if not order.email_sent:
                    self._send_confirmation_email(order)
                    order.email_sent = True
                    order.save(update_fields=['email_sent'])
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Email sent using order_id',
                    status=200
                )
            except Order.DoesNotExist:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: Order ID not found',
                    status=404
                )

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.get("name"),
                    email__iexact=billing_details.get("email"),
                    phone_number__iexact=shipping_details.get("phone"),
                    country__iexact=shipping_details.get("address", {}).get("country"),
                    postcode__iexact=shipping_details.get("address", {}).get("postal_code"),
                    town_or_city__iexact=shipping_details.get("address", {}).get("city"),
                    street_address1__iexact=shipping_details.get("address", {}).get("line1"),
                    street_address2__iexact=shipping_details.get("address", {}).get("line2"),
                    county__iexact=shipping_details.get("address", {}).get("state"),
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            if not order.email_sent:
                print(">>> Calling send_mail from webhook handler <<<")
                self._send_confirmation_email(order)
                order.email_sent = True
                order.save(update_fields=['email_sent'])
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order manually',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.get("name"),
                    user_profile=profile,
                    email=billing_details.get("email"),
                    phone_number=shipping_details.get("phone"),
                    country=shipping_details.get("address", {}).get("country"),
                    postcode=shipping_details.get("address", {}).get("postal_code"),
                    town_or_city=shipping_details.get("address", {}).get("city"),
                    street_address1=shipping_details.get("address", {}).get("line1"),
                    street_address2=shipping_details.get("address", {}).get("line2"),
                    county=shipping_details.get("address", {}).get("state"),
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                for item_id, quantity in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

            except Exception as e:
               print(f"🔥 Webhook Error: {e}")  # Add this line to get the actual error in terminal
               if order:
                    order.delete()
               return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500
               )

            self._send_confirmation_email(order)
            print(">>> Called send_mail after creating new order <<<")
            order.email_sent = True
            order.save(update_fields=['email_sent'])

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Payment failed',
            status=200
        )
