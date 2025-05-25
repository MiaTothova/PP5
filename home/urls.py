from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newsletter/', views.newsletter_signup, name='newsletter'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
]
