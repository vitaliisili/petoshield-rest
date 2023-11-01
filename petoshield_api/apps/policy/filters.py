from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filter
from django_filters.widgets import RangeWidget
from .models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
from apps.user.models import User
from apps.pet.models import Pet

POLICY_STATUS = (
        ('valid', _('Valid')),
        ('invalid', _('Invalid')),
        ('expired', _('Expired')),
    )

INSURANCE_STATUS = (
        ('accept', _('Accept')),
        ('process', _('Process')),
        ('reject', _('Reject')),
    )


class ServiceProviderFilterSet(filter.FilterSet):
    company_name = filter.CharFilter(field_name='name', lookup_expr='icontains')
    registration_number = filter.CharFilter(field_name='registration_number',lookup_expr='exact')
    address = filter.CharFilter(field_name='address', lookup_expr='startswith')
    iban = filter.CharFilter(field_name='iban', lookup_expr='exact')
    user = filter.CharFilter(field_name='user__name', lookup_expr='icontains')
    
    class Meta:
        model = ServiceProvider
        fields = ('company_name', 'registration_number', 'address', 'iban', 'user')
        
        
class PolicyFilterSet(filter.FilterSet):
    policy_number = filter.CharFilter(field_name='name', lookup_expr='icontains')
    start_date = filter.DateTimeFromToRangeFilter(widget=RangeWidget(attrs=({'type':'date'})))
    status = filter.ChoiceFilter(choices=POLICY_STATUS)
    pet = filter.CharFilter(field_name='pet__name', lookup_expr='iexact')
        
    class Meta:
        model = Policy
        fields = ('policy_number','start_date', 'end_date', 'status', 'deductible', 'pet')
        

class InsuranceCaseFilterSet(filter.FilterSet):
    claim_date = filter.DateTimeFromToRangeFilter(widget=RangeWidget(attrs=({'type':'date'})))
    status = filter.ChoiceFilter(choices=INSURANCE_STATUS)
    policy = filter.CharFilter(field_name='policy__policy_number', lookup_expr='iexact')
    service_provider = filter.CharFilter(field_name='service_provider__company_name', lookup_expr='iexact')
    
    class Meta:
        model = InsuranceCase
        fields = ('claim_date', 'status', 'policy', 'service_provider')

class IncomingInvoiceFilterSet(filter.FilterSet):
    invoice_date = filter.DateTimeFromToRangeFilter(widget=RangeWidget(attrs=({'type':'date'})))
    amount = filter.RangeFilter(field_name='amount')
    insurance_case = filter.CharFilter(field_name='insurance_case__claim_date', lookup_expr='iexact')
    
    class Meta:
        model = IncomingInvoice
        fields = ('invoice_date', 'amount', 'insurance_case')