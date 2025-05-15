from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RP1dV5J0fjtCXWRaBoEdYOpDXZsa9ckQDRolryHwJxf7HWvkKxE8aekofb1yRhJuc0saHhg4oBQ0l8p4t3cPcTb00G7AQdDQS',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)