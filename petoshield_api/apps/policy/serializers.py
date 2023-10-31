from rest_framework import serializers
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
from apps.user.serializers import BaseUserSerializer


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        exclude = ['user']
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserServiceProviderSerializer(serializers.Serializer):
    user = BaseUserSerializer()
    service_provider = ServiceProviderSerializer()


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'
        read_only_fields = ['id']


class InsuranceCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCase
        fields = '__all__'
        read_only_fields = ['id', 'total_cost']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['total_cost'] = IncomingInvoice.objects.get(insurance_case=instance).amount
        except IncomingInvoice.DoesNotExist:  # noqa
            representation['total_cost'] = None
        return representation


class IncomingInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingInvoice
        fields = '__all__'
        read_only_fields = ['id']
