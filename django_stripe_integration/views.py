import stripe
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.conf import settings

User = get_user_model()
stripe.api_key = settings.STRIPE_LIVE_SECRET_KEY if settings.STRIPE_LIVE_MODE else settings.STRIPE_TEST_SECRET_KEY


def payment_checkout(request):
    pass


def payment_success(request):
    pass


def payment_cancel(request):
    pass
