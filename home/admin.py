from django.contrib import admin
from .models import NewsletterSubscription, ContactMessage

@admin.register(NewsletterSubscription)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on')
    

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_on')  
    readonly_fields = ('sent_on',)