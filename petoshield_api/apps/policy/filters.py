from django_filters import rest_framework as filters
from .models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice


class ServiceProviderFilter(filters.FilterSet):
    user = filters.CharFilter(field_name='user__name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')
       
    class Meta:
        model = ServiceProvider
        fields = {
            'company_name': ['iexact', 'icontains'], 
            'registration_number': ['exact'], 
            'address': ['iexact','icontains'], 
            'iban': ['exact'],
            'created_at': ['exact', 'gt', 'lt']
            }
        
        
class PolicyFilter(filters.FilterSet):
    pet = filters.CharFilter(field_name='pet__name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')
               
    class Meta:
        model = Policy
        fields = {
            'policy_number': ['exact'],
            'start_date': ['exact','gt','lt'],
            'end_date': ['exact','gt','lt'],
            'status': ['icontains'],
            'deductible': ['exact','gt','lt'],
            'created_at': ['exact', 'gt', 'lt']
            }
        

class InsuranceCaseFilter(filters.FilterSet):
    policy = filters.CharFilter(field_name='policy__policy_number', lookup_expr='icontains')
    service_provider = filters.CharFilter(field_name='service_provider__company_name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')
          
    class Meta:
        model = InsuranceCase
        fields = {
            'claim_date': ['exact','gt','lt'], 
            'status': ['icontains'], 
            'created_at': ['exact', 'gt', 'lt']
                  }

class IncomingInvoiceFilter(filters.FilterSet):
    insurance_case = filters.CharFilter(field_name='insurance_case__claim_date', lookup_expr='iexact')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')
           
    class Meta:
        model = IncomingInvoice
        fields = {
            'invoice_date': ['exact','gt','lt'], 
            'amount': ['exact','gt','lt'],
            'created_at': ['exact', 'gt', 'lt']
        }