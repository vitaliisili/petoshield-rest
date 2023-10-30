from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
from apps.user.models import Role
from django.utils.translation import gettext_lazy as _
from apps.policy.permissions import (PolicyPermissions,
                                     ProviderPermissions,
                                     InsuranceCasePermissions,
                                     IncomingInvoicePermissions)
from apps.policy.serializers import (PolicySerializer,
                                     InsuranceCaseSerializer,
                                     IncomingInvoiceSerializer,
                                     UserServiceProviderSerializer)


class ServiceProviderViewSet(viewsets.ModelViewSet):
    serializer_class = UserServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
    permission_classes = (ProviderPermissions,)
    search_fields = ['$company_name', 'registration_number']
    ordering_fields = ['created_at']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user['role'] = Role.objects.get(name='provider')

        provider = serializer.validated_data['service_provider']
        user_instance = get_user_model().objects.create_user(**user)
        provider['user'] = user_instance

        ServiceProvider.objects.create(**provider)

        return Response(data={'message': _("Service Provider was registered successfully")},
                        status=status.HTTP_201_CREATED)


class PolicyViewSet(viewsets.ModelViewSet):
    serializer_class = PolicySerializer
    permission_classes = (IsAuthenticated, PolicyPermissions)
    search_fields = ['policy_number']
    ordering_fields = ['created_at', 'start_date', 'end_date']

    def get_queryset(self):
        if self.request.user.role.name == 'client':
            return Policy.objects.filter(pet__user=self.request.user)
        elif self.request.user.role.name == 'provider':
            return ServiceProvider.objects.get(user=self.request.user).policies.all()

        return Policy.objects.all()


class InsuranceCaseViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceCaseSerializer
    permission_classes = (IsAuthenticated, InsuranceCasePermissions)
    ordering_fields = ['created_at', 'claim_date']

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

    def get_queryset(self):
        if self.request.user.role.name == 'provider':
            return IncomingInvoice.objects.filter(insurance_case__service_provider__user=self.request.user)
        return IncomingInvoice.objects.all()