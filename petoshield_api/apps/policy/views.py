from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
from apps.user.models import Role
from apps.core.utils import Validate
from apps.policy.permissions import (PolicyPermissions,
                                     ProviderPermissions,
                                     InsuranceCasePermissions,
                                     IncomingInvoicePermissions)
from apps.policy.serializers import (PolicySerializer,
                                     InsuranceCaseSerializer,
                                     IncomingInvoiceSerializer,
                                     UserServiceProviderSerializer,
                                     ServiceProviderSerializer)
from apps.policy.filters import (PolicyFilter,
                                 ServiceProviderFilter,
                                 InsuranceCaseFilter,
                                 IncomingInvoiceFilter)


class ServiceProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
    permission_classes = (ProviderPermissions,)
    search_fields = ['$company_name', 'registration_number']
    ordering_fields = ['created_at']
    filterset_class = ServiceProviderFilter

    def create(self, request, *args, **kwargs):
        serializer = UserServiceProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user['role'] = Role.objects.get(name='provider')
        user_instance = get_user_model().objects.create_user(**user)

        provider = serializer.validated_data['service_provider']
        provider['user'] = user_instance
        ServiceProvider.objects.create(**provider)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class PolicyViewSet(viewsets.ModelViewSet):
    serializer_class = PolicySerializer
    permission_classes = (IsAuthenticated, PolicyPermissions)
    search_fields = ['policy_number']
    ordering_fields = ['created_at', 'start_date', 'end_date']
    filterset_class = PolicyFilter

    def get_queryset(self):
        if self.request.user.role.name == 'client':
            return Policy.objects.filter(pet__user=self.request.user)
        elif self.request.user.role.name == 'provider':
            return Policy.objects.filter(insurance_cases__service_provider__user=self.request.user)

        return Policy.objects.all()


class InsuranceCaseViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceCaseSerializer
    permission_classes = (IsAuthenticated, InsuranceCasePermissions)
    ordering_fields = ['created_at', 'claim_date']
    filterset_class = InsuranceCaseFilter

    def get_queryset(self):
        if self.request.user.role.name == 'client':
            return InsuranceCase.objects.filter(policy__pet__user=self.request.user)
        elif self.request.user.role.name == 'provider':
            return InsuranceCase.objects.filter(service_provider__user=self.request.user)
        return InsuranceCase.objects.all()

    def update(self, request, *args, **kwargs):
        if request.user.role.name == 'provider':
            request.data['service_provider'] = self.request.user.provider.id
        return super().update(request, *args, **kwargs)


class IncomingInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = IncomingInvoiceSerializer
    permission_classes = (IsAuthenticated, IncomingInvoicePermissions)
    ordering_fields = ['created_at', 'invoice_date', 'amount']
    filterset_class = IncomingInvoiceFilter

    def get_queryset(self):
        if self.request.user.role.name == 'provider':
            return IncomingInvoice.objects.filter(insurance_case__service_provider__user=self.request.user)
        return IncomingInvoice.objects.all()
