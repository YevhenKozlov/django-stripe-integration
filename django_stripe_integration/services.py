import stripe
from djstripe.models import Customer, Plan
from django.contrib.auth import get_user_model

User = get_user_model()


def create_subscription(user: User, plan: Plan):
    customer = Customer.objects.get(subscriber=user)
    customer.subscribe(plan=plan)


def cancel_subscription(user: User):
    customer = Customer.objects.get(subscriber=user)
    customer.subscription.cancel()
