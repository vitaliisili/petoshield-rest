from rest_framework.serializers import ModelSerializer
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice

class ServiceProviderSerializer(ModelSerializer):
    
    class Meta:
        model = ServiceProvider
        fields = "__all__"
        read_only_fields = ["id"]

class PolicySerializer(ModelSerializer):
    
    class Meta:
        model = Policy
        fields = "__all__"
        read_only_fields = ["id"]
        
class InsuranceCaseSerializer(ModelSerializer):

    class Meta:
        model = InsuranceCase
        fields = "__all__"
        read_only_fields = ["id"]
        

class IncomingInvoiceSerializer(ModelSerializer):
    
    class Meta:
        model = IncomingInvoice
        fields = ['invoice_date', 'amount', 'insurance_case']
        read_only_fields = ["id"]
