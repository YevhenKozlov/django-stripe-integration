import stripe

from django.urls import path
from . import views

urlpatterns = [
    path("stripe/checkout/", views.payment_checkout),
    path("stripe/success/", views.payment_success),
    path("stripe/cancel/", views.payment_cancel),
]
