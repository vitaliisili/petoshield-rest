from django_filters import rest_framework as filter
from .models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice


class ServiceProviderFilter(filter.FilterSet):
    user = filter.CharFilter(field_name='user__name', lookup_expr='icontains')
    
    class Meta:
        model = ServiceProvider
        fields = {
            'company_name': ['icontains'], 
            'registration_number': ['exact'], 
            'address': ['icontains'], 
            'iban': ['exact']
            }
        
        
class PolicyFilter(filter.FilterSet):
    pet = filter.CharFilter(field_name='pet__name', lookup_expr='icontains')
        
    class Meta:
        model = Policy
        fields = {
            'policy_number': ['exact'],
            'start_date': ['exact','gt','lt'],
            'end_date': ['exact','gt','lt'],
            'status': ['icontains'],
            'deductible': ['exact','gt','lt']
            }
        

class InsuranceCaseFilter(filter.FilterSet):
    policy = filter.CharFilter(field_name='policy__policy_number', lookup_expr='icontains')
    service_provider = filter.CharFilter(field_name='service_provider__company_name', lookup_expr='icontains')
    
    class Meta:
        model = InsuranceCase
        fields = {
            'claim_date': ['exact','gt','lt'], 
            'status': ['icontains'], 
                  }

class IncomingInvoiceFilter(filter.FilterSet):
    insurance_case = filter.CharFilter(field_name='insurance_case__claim_date', lookup_expr='iexact')
    
    class Meta:
        model = IncomingInvoice
        fields = {
            'invoice_date': ['exact','gt','lt'], 
            'amount': ['exact','gt','lt']
        }