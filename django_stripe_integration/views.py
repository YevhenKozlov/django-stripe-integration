import stripe
from djstripe.models import Customer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.conf import settings

User = get_user_model()

stripe.api_key = (
    settings.STRIPE_LIVE_SECRET_KEY 
    if settings.STRIPE_LIVE_MODE 
    else settings.STRIPE_TEST_SECRET_KEY
)


def payment_checkout(request):
    customer = Customer.objects.get(subscriber=request.user)
    session = stripe.checkout.Session.create(
        customer=customer.id,
        payment_method_types=["card"],
        subscription_data={"items": [{"plan": request.data["plan_id"]}],},
        success_url="http://example.com/success",
        cancel_url="http://example.com/cancelled",
    )
    
    return JsonResponse({"session_id": session.id})
