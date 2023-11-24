from django_filters import rest_framework as filters
from .models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice


class ServiceProviderFilter(filters.FilterSet):
    """A filter class for the ServiceProvider model.
    Attributes:
        user (CharFilter): Filter for the 'user__name' field using the 'icontains' lookup.
        created_at__year__exact (NumberFilter): Filter for the 'created_at__year' field with exact matching.
        created_at__year__gt (NumberFilter): Filter for the 'created_at__year' field with greater than matching.
        created_at__year__lt (NumberFilter): Filter for the 'created_at__year' field with less than matching.
    Meta:
        model (ServiceProvider): The model to be filtered.
        fields (dict): The fields and lookup types to be used for filtering.
    """

    user = filters.CharFilter(field_name='user__name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')

    class Meta:
        model = ServiceProvider
        fields = {
            'company_name': ['exact', 'icontains'],
            'registration_number': ['exact'],
            'address': ['exact', 'icontains'],
            'iban': ['exact'],
            'created_at': ['exact', 'gt', 'lt']
        }


class PolicyFilter(filters.FilterSet):
    """A filter class for the Policy model.
    Attributes:
        pet (CharFilter): Filter for the 'pet__name' field using the 'icontains' lookup.
        created_at__year__exact (NumberFilter): Filter for the 'created_at__year' field with exact matching.
        created_at__year__gt (NumberFilter): Filter for the 'created_at__year' field with greater than matching.
        created_at__year__lt (NumberFilter): Filter for the 'created_at__year' field with less than matching.
    Meta:
        model (Policy): The model to be filtered.
        fields (dict): The fields and lookup types to be used for filtering.
    """

    pet = filters.CharFilter(field_name='pet__name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')

    class Meta:
        model = Policy
        fields = {
            'policy_number': ['exact'],
            'start_date': ['exact', 'gt', 'lt'],
            'end_date': ['exact', 'gt', 'lt'],
            'status': ['exact', 'icontains'],
            'price': ['exact', 'gt', 'lt'],
            'deductible': ['exact', 'gt', 'lt'],
            'created_at': ['exact', 'gt', 'lt']
        }


class InsuranceCaseFilter(filters.FilterSet):
    """A filter class for the InsuranceCase model.
    Attributes:
        policy (CharFilter): Filter for the 'policy__policy_number' field using the 'icontains' lookup.
        service_provider (CharFilter): Filter for the 'service_provider__company_name'
        field using the 'icontains' lookup.
        created_at__year__exact (NumberFilter): Filter for the 'created_at__year' field with exact matching.
        created_at__year__gt (NumberFilter): Filter for the 'created_at__year' field with greater than matching.
        created_at__year__lt (NumberFilter): Filter for the 'created_at__year' field with less than matching.
    Meta:
        model (InsuranceCase): The model to be filtered.
        fields (dict): The fields and lookup types to be used for filtering.
    """

    policy = filters.CharFilter(field_name='policy__policy_number', lookup_expr='icontains')
    service_provider = filters.CharFilter(field_name='service_provider__company_name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')

    class Meta:
        model = InsuranceCase
        fields = {
            'claim_date': ['exact', 'gt', 'lt'],
            'status': ['exact', 'icontains'],
            'created_at': ['exact', 'gt', 'lt']
        }


class IncomingInvoiceFilter(filters.FilterSet):
    """A filter class for the IncomingInvoice model.
    Attributes:
        insurance_case (DateFilter): Filter for the 'insurance_case__claim_date' field using the 'exact' lookup.
        created_at__year__exact (NumberFilter): Filter for the 'created_at__year' field with exact matching.
        created_at__year__gt (NumberFilter): Filter for the 'created_at__year' field with greater than matching.
        created_at__year__lt (NumberFilter): Filter for the 'created_at__year' field with less than matching.
    Meta:
        model (IncomingInvoice): The model to be filtered.
        fields (dict): The fields and lookup types to be used for filtering.
    """

    insurance_case = filters.DateFilter(field_name='insurance_case__claim_date', lookup_expr='exact')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')

    class Meta:
        model = IncomingInvoice
        fields = {
            'invoice_date': ['exact', 'gt', 'lt'],
            'amount': ['exact', 'gt', 'lt'],
            'created_at': ['exact', 'gt', 'lt']
        }
