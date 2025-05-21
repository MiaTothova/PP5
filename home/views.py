from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def newsletter_signup(request):
    """View to handle newsletter signup."""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Subscribed to the newsletter successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'This email is already subscribed or invalid.')
    return redirect('home')


# def newsletter_thank_you(request):
#     return render(request, 'home/newsletter_thank_you.html')
