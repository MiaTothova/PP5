from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm, ContactForm
from .models import FAQ


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def newsletter_signup(request):
    """View to handle newsletter signup."""
    if request.method == 'POST':
        form = NewsletterForm(request.POST, prefix='newsletter')
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Subscribed to the newsletter successfully!'
                )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'This email is already subscribed or invalid.'
                )
    return redirect('home')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for your message! We will get back to you soon.'
                )
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'home/faq.html', {'faqs': faqs})
