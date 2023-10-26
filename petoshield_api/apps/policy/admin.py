from django.contrib import admin
from apps.policy import models

class CustomServiceProvider(admin.ModelAdmin):
    list_display= (
        'company_name',
        'email',
        'phone',
        'registration_number',
        'address',
        'iban'
    )
class CustomPolicy(admin.ModelAdmin):
    list_display= (
        'policy_number',
        'start_date',
        'end_date',
        'status',
        'initial_limit',
        'current_limit',
        'deductible',
        'get_pet_name',
        'get_providers'
    )

    @admin.display(description = "providers")
    def get_providers(self,obj):
        return ", ".join([providers.company_name for providers in obj.providers.all()])

    @admin.display(description='pet_name')
    def get_pet_name(self,obj):
        return obj.pet.name

class CustomInsuranceCase(admin.ModelAdmin):
    list_display= (
        'claim_date',
        'description',
        'status',
        'service_provider',
        'get_service_provider'
    )
    @admin.display(description='service_provider_name')
    def get_service_provider(self,obj):
        return obj.service_provider.company_name

class CustomIncomingInvoice(admin.ModelAdmin):
    list_display = (
        'invoice_date',
        'amount',
        'insurance_case'
    )

admin.site.register(models.ServiceProvider, CustomServiceProvider)
admin.site.register(models.Policy, CustomPolicy)
admin.site.register(models.InsuranceCase, CustomInsuranceCase)
admin.site.register(models.IncomingInvoice, CustomIncomingInvoice)