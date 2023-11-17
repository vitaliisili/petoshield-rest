import stripe
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError as RestValidationError
from apps.payment.models import StripeSession
from apps.payment.serializer import StripeCheckOutSerializer
from django.utils.translation import gettext_lazy as _
from apps.policy.models import Policy


class StripeViewSet(viewsets.ModelViewSet):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    @action(detail=False, methods=['post'])
    def create_checkout(self, request):
        data = request.data

        serializer = StripeCheckOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        redirect_link = data.get('redirect_link')

        try:
            price = stripe.Price.create(
                product=settings.STRIPE_ANNUAL if data.get('frequency') == 'annual' else settings.STRIPE_MONTHLY,
                unit_amount=int(float(request.data.get('final_price')) * 100),
                currency='eur',
                recurring={'interval': 'year' if data.get('frequency') == 'annual' else 'month'},
            )

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    },
                ],
                client_reference_id=request.user.id,
                payment_method_types=['card'],
                mode='subscription',
                customer_email=request.user.email,
                success_url=redirect_link + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=redirect_link + '?cancel=true'
            )

            policy = Policy.objects.get(pet__id=data.get('pet'))
            StripeSession.objects.create(session_id=checkout_session.id, policy=policy)

            return Response({"checkout_url": checkout_session.url}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'something went wrong when creating stripe checkout session:'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def checkout_confirm(self, request):
        policy = Policy.objects.filter(session__session_id=request.data.get('session_id')).first()

        if not policy:
            raise RestValidationError('Session id is not correct')

        policy.status = 'valid'
        policy.save()

        return Response({'message': _('Checkout has been confirmed')})

    @action(detail=False, methods=['post'])
    def cancel_insurance(self, request):
        pass
