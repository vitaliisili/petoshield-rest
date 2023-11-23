from rest_framework import permissions
import stripe
from django.conf import settings


class StripePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create_checkout', 'public_key', 'checkout_confirm', 'cancel_insurance']:
            return request.user.is_authenticated or request.user.is_staff
        elif view.action == 'webhook':
            try:
                stripe.Webhook.construct_event(
                    payload=request.body,
                    sig_header=request.headers.get('stripe-signature'),
                    secret=settings.STRIPE_WEBHOOK_SECRET
                )
                return True
            except stripe.error.SignatureVerificationError:
                return False
        else:
            return False
