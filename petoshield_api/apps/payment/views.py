import stripe
from django.conf import settings
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from apps.payment.models import StripeSession, StripeCustomer, StripeSubscription
from apps.payment.permissions import StripePermission
from apps.payment.serializer import StripeCheckOutSerializer, CancelInsuranceSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError as RestValidationError
from apps.pet.models import Pet
from apps.policy.models import Policy
from apps.core.utils import EmailSender


@extend_schema(tags=['Stripe'])
@extend_schema_view(
    list=extend_schema(exclude=True),
    retrieve=extend_schema(exclude=True),
    create=extend_schema(exclude=True),
    update=extend_schema(exclude=True),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(exclude=True),
    webhook=extend_schema(exclude=True),
    create_checkout=extend_schema(request=StripeCheckOutSerializer,
                                  responses={'checkout_url': OpenApiTypes.STR}),
    public_key=extend_schema(responses={'key': OpenApiTypes.STR}),
    checkout_confirm=extend_schema(request={'session_id': OpenApiTypes.STR},
                                   responses={'message': OpenApiTypes.STR, 'invoice_url': OpenApiTypes.STR}),
    cancel_insurance=extend_schema(request=CancelInsuranceSerializer, responses={'message': OpenApiTypes.STR})
)
class StripeViewSet(viewsets.ModelViewSet):
    """A viewset for interacting with the Stripe API."""

    stripe.api_key = settings.STRIPE_SECRET_KEY
    permission_classes = (StripePermission,)

    @action(detail=False, methods=['post'])
    def create_checkout(self, request):
        data = request.data

        serializer = StripeCheckOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pet = Pet.objects.get(pk=serializer.data.get('pet'))

        try:
            customer = stripe.Customer.create(name=pet.name, email=request.user.email)
            price = stripe.Price.create(
                product=settings.STRIPE_ANNUAL if data.get('frequency') == 'annual' else settings.STRIPE_MONTHLY,
                unit_amount=int(float(request.data.get('final_price')) * 100),
                currency='eur',
                recurring={'interval': 'year' if data.get('frequency') == 'annual' else 'month'}
            )

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card', 'paypal'],
                mode='subscription',
                customer=customer.id,
                client_reference_id=pet.id,
                success_url=serializer.data.get('redirect_link') + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=serializer.data.get('redirect_link') + '?cancel=true'
            )

            policy = Policy.objects.get(pet__id=pet.id)
            StripeSession.objects.create(session_id=checkout_session.id, policy=policy)

            return Response({"checkout_url": checkout_session.url}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': _('something went wrong when creating stripe checkout session')},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False)
    def public_key(self, request):
        return Response({'key': settings.STRIPE_PUBLIC_KEY})

    @action(detail=False, methods=['post'])
    def webhook(self, request):
        event = stripe.Event.construct_from(request.data, settings.STRIPE_SECRET_KEY)
        if event.type == 'invoice.paid':
            invoice = event.data.object
            email_data = {
                "email": invoice.customer_email,
                "invoice_url": invoice.hosted_invoice_url,
            }
            EmailSender.send_mail_checkout_confirm(email_data)

        return Response({'success': True}, status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def checkout_confirm(self, request):
        try:
            session = stripe.checkout.Session.retrieve(request.data.get('session_id'))
            policy = StripeSession.objects.get(session_id=session.id).policy
            stripe_customer = StripeCustomer.objects.create(id=session.customer, name=session.customer_details.name)

            stripe_subscription = StripeSubscription.objects.create(id=session.subscription,
                                                                    price=float(session.amount_total / 100),
                                                                    stripe_customer=stripe_customer,
                                                                    policy=policy)
            policy.status = 'valid'
            policy.save()

            invoice_id = stripe.Subscription.retrieve(stripe_subscription.id).latest_invoice
            invoice_url = stripe.Invoice.retrieve(invoice_id).hosted_invoice_url

            return Response({
                'message': _('Payment has been accepted'),
                'invoice_url': invoice_url
            }, status=status.HTTP_200_OK)

        except Exception:
            return Response({'error': _('something went wrong when try to confirm payment')},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def cancel_insurance(self, request):
        serializer = CancelInsuranceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        stripe_subscription = StripeSubscription.objects.filter(policy__id=serializer.data.get('policy')).first()

        if not stripe_subscription:
            raise RestValidationError(_('Subscription not found'))

        stripe.Subscription.modify(
            stripe_subscription.id,
            cancel_at_period_end=True,
        )

        policy = stripe_subscription.policy
        policy.status = 'invalid'
        policy.save()
        email_data = {
            "name": request.user.name,
            "email": request.user.email,
            "policy_number": policy.policy_number,
        }
        EmailSender.send_mail_subscription_cancelled(email_data)

        return Response({'message': 'Subscription has been canceled'}, status.HTTP_200_OK)
