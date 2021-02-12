import stripe

from django.urls import path
from . import views

urlpatterns = [
    path("stripe/checkout/", views.payment_checkout),
]
