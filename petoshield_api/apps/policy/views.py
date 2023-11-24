from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
from apps.user.models import Role
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
from apps.core.utils import EmailSender, JwtToken


@extend_schema(tags=['ServiceProvider'])
class ServiceProviderViewSet(viewsets.ModelViewSet):
    """ViewSet for managing service providers.
    Attributes:
        serializer_class (ServiceProviderSerializer): The serializer class for service providers.
        queryset (QuerySet): The queryset for retrieving service providers.
        permission_classes (tuple): The permission classes for accessing and modifying service providers.
        search_fields (list): The fields to be searched when filtering service providers.
        ordering_fields (list): The fields to be used for ordering service providers.
        filterset_class (ServiceProviderFilter): The filter class for filtering service providers.
    Methods:
        create: Create a new service provider.

    """

    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
    permission_classes = (ProviderPermissions,)
    search_fields = ['$company_name', 'registration_number']
    ordering_fields = ['created_at']
    filterset_class = ServiceProviderFilter

    def create(self, request, *args, **kwargs):
        """Creates a new service provider.
        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: The response object.
        """

        serializer = UserServiceProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user['role'] = Role.objects.get(name='provider')
        user_instance = get_user_model().objects.create_user(**user)

        provider = serializer.validated_data['service_provider']
        provider['user'] = user_instance
        ServiceProvider.objects.create(**provider)

        EmailSender.send_welcome_email_for_service_provider(user_instance)
        EmailSender.send_confirmation_email(user_instance, request.META.get('HTTP_REFERER'))

        return Response(JwtToken.get_jwt_token(user_instance), status=status.HTTP_201_CREATED)


@extend_schema(tags=['Policy'])
@extend_schema_view(create=extend_schema(exclude=True))
class PolicyViewSet(viewsets.ModelViewSet):
    """ViewSet for managing policies.
    Attributes:
        serializer_class (PolicySerializer): The serializer class for policies.
        queryset (QuerySet): The queryset for retrieving policies. Set to an empty queryset initially.
        permission_classes (tuple): The permission classes for accessing and modifying policies.
        search_fields (list): The fields to be searched when filtering policies.
        ordering_fields (list): The fields to be used for ordering policies.
        filterset_class (PolicyFilter): The filter class for filtering policies.
    Methods:
        get_queryset: Returns the queryset based on the user's role.
    """

    serializer_class = PolicySerializer
    queryset = Policy.objects.none()
    permission_classes = (IsAuthenticated, PolicyPermissions)
    search_fields = ['policy_number']
    ordering_fields = ['created_at', 'start_date', 'end_date']
    filterset_class = PolicyFilter

    def get_queryset(self):
        """Returns the queryset based on the user's role.
        Returns:
            QuerySet: The filtered queryset based on the user's role.
        """

        if self.request.user.role.name == 'client':
            return Policy.objects.filter(pet__user=self.request.user)
        elif self.request.user.role.name == 'provider':
            return Policy.objects.filter(insurance_cases__service_provider__user=self.request.user)
        return Policy.objects.all()


@extend_schema(tags=['InsuranceCase'])
class InsuranceCaseViewSet(viewsets.ModelViewSet):
    """ViewSet for managing insurance cases.
    Attributes:
        serializer_class (InsuranceCaseSerializer): The serializer class for insurance cases.
        queryset (QuerySet): The queryset for retrieving insurance cases. Set to an empty queryset initially.
        permission_classes (tuple): The permission classes for accessing and modifying insurance cases.
        ordering_fields (list): The fields to be used for ordering insurance cases.
        filterset_class (InsuranceCaseFilter): The filter class for filtering insurance cases.
    Methods:
        get_queryset: Returns the queryset based on the user's role.
        update: Updates an insurance case, with additional logic for providers.
    """

    serializer_class = InsuranceCaseSerializer
    queryset = InsuranceCase.objects.none()
    permission_classes = (IsAuthenticated, InsuranceCasePermissions)
    ordering_fields = ['created_at', 'claim_date']
    filterset_class = InsuranceCaseFilter

    def get_queryset(self):
        """Returns the queryset based on the user's role.
        Returns:
            QuerySet: The filtered queryset based on the user's role.
        """

        if self.request.user.role.name == 'client':
            return InsuranceCase.objects.filter(policy__pet__user=self.request.user)
        elif self.request.user.role.name == 'provider':
            return InsuranceCase.objects.filter(service_provider__user=self.request.user)
        return InsuranceCase.objects.all()

    def update(self, request, *args, **kwargs):
        """Updates an insurance case, with additional logic for providers.
        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: The response object.
        """

        if request.user.role.name == 'provider':
            request.data['service_provider'] = self.request.user.provider.id
        return super().update(request, *args, **kwargs)


@extend_schema(tags=['IncomingInvoice'])
class IncomingInvoiceViewSet(viewsets.ModelViewSet):
    """ViewSet for managing incoming invoices.
    Attributes:
        serializer_class (IncomingInvoiceSerializer): The serializer class for incoming invoices.
        queryset (QuerySet): The queryset for retrieving incoming invoices. Set to an empty queryset initially.
        permission_classes (tuple): The permission classes for accessing and modifying incoming invoices.
        ordering_fields (list): The fields to be used for ordering incoming invoices.
        filterset_class (IncomingInvoiceFilter): The filter class for filtering incoming invoices.
    Methods:
        get_queryset: Returns the queryset based on the user's role.
    """

    serializer_class = IncomingInvoiceSerializer
    queryset = IncomingInvoice.objects.none()
    permission_classes = (IsAuthenticated, IncomingInvoicePermissions)
    ordering_fields = ['created_at', 'invoice_date', 'amount']
    filterset_class = IncomingInvoiceFilter

    def get_queryset(self):
        """Returns the queryset based on the user's role.
        Returns:
            QuerySet: The filtered queryset based on the user's role.
        """

        if self.request.user.role.name == 'provider':
            return IncomingInvoice.objects.filter(insurance_case__service_provider__user=self.request.user)
        return IncomingInvoice.objects.all()
