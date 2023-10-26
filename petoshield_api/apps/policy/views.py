from rest_framework import viewsets
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
from apps.policy.serializers import (
    ServiceProviderSerializer,
    PolicySerializer,
    InsuranceCaseSerializer,
    IncomingInvoiceSerializer)


class ServiceProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
    # permission_classes =  # TODO: add permission class
    search_fields = ['$company_name', 'registration_number']
    ordering_fields = ['created_at']


class PolicyViewSet(viewsets.ModelViewSet):
    serializer_class = PolicySerializer
    queryset = Policy.objects.all()
    # permission_classes =  # TODO: add permission class
    search_fields = ['policy_number']
    ordering_fields = ['created_at', 'start_date', 'end_date']


class InsuranceCaseViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceCaseSerializer
    queryset = InsuranceCase.objects.all()
    # permission_classes =  # TODO: add permission class
    ordering_fields = ['created_at', 'claim_date']


class IncomingInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = IncomingInvoiceSerializer
    queryset = IncomingInvoice.objects.all()
    # permission_classes =  # TODO: add permission class
    ordering_fields = ['created_at', 'invoice_date', 'amount']