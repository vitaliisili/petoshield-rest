from rest_framework import serializers
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
from apps.user.serializers import RegisterUserSerializer


class ServiceProviderSerializer(serializers.ModelSerializer):
    """Serializer for the ServiceProvider model.
    Meta:
        model (ServiceProvider): The model to be serialized.
        exclude (list): The fields to be excluded from serialization.
        read_only_fields (list): The fields that are read-only.
    """

    class Meta:
        model = ServiceProvider
        exclude = ['user']
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserServiceProviderSerializer(serializers.Serializer):
    """Serializer for the UserServiceProvider model.
    Attributes:
        user (RegisterUserSerializer): The serializer for the User model.
        service_provider (ServiceProviderSerializer): The serializer for the ServiceProvider model.
    """

    user = RegisterUserSerializer()
    service_provider = ServiceProviderSerializer()


class PolicySerializer(serializers.ModelSerializer):
    """Serializer for the Policy model.
    Meta:
        model (Policy): The model to be serialized.
        fields (str): The fields to be included in serialization.
        read_only_fields (list): The fields that are read-only.
    """

    class Meta:
        model = Policy
        fields = '__all__'
        read_only_fields = ['id']


class InsuranceCaseSerializer(serializers.ModelSerializer):
    """Serializer for the InsuranceCase model.
    Meta:
        model (InsuranceCase): The model to be serialized.
        fields (str): The fields to be included in serialization.
        read_only_fields (list): The fields that are read-only.
    """

    class Meta:
        model = InsuranceCase
        fields = '__all__'
        read_only_fields = ['id', 'total_cost']

    def to_representation(self, instance):
        """Converts the serialized data representation.
        Args:
            instance: The instance of the model.
        Returns:
            dict: The converted representation of the serialized data.
        """

        representation = super().to_representation(instance)
        try:
            representation['total_cost'] = IncomingInvoice.objects.get(insurance_case=instance).amount
        except IncomingInvoice.DoesNotExist:  # noqa
            representation['total_cost'] = None
        return representation


class IncomingInvoiceSerializer(serializers.ModelSerializer):
    """Serializer for the IncomingInvoice model.
    Meta:
        model (IncomingInvoice): The model to be serialized.
        fields (str): The fields to be included in serialization.
        read_only_fields (list): The fields that are read-only.
    """

    class Meta:
        model = IncomingInvoice
        fields = '__all__'
        read_only_fields = ['id']
