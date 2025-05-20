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
            messages.success(request, "Thank you for subscribing!")
            return redirect('home')
    else:
        form = NewsletterForm()
    return render(request, 'home/newsletter.html', {'form': form})