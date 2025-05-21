# from django import forms
# from .models import NewsletterSubscription

# class NewsletterForm(forms.ModelForm):
#     class Meta:
#         model = NewsletterSubscription
#         fields = ['email']

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import NewsletterSubscription, ContactMessage

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
