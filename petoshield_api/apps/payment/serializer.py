from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class StripeCheckOutSerializer(serializers.Serializer):
    FREQUENCY = [
        ('annual', _('Annual')),
        ('monthly', _('monthly')),
    ]
    final_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    frequency = serializers.ChoiceField(choices=FREQUENCY)
    redirect_link = serializers.URLField()
    pet = serializers.IntegerField()


class CancelInsuranceSerializer(serializers.Serializer):
    policy = serializers.IntegerField()
