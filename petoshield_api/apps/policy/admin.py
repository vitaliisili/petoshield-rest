from django.contrib import admin
from apps.policy import models


class CustomServiceProvider(admin.ModelAdmin):
    """Admin model customization for the ServiceProvider model.
    Attributes:
        list_display (tuple): The fields to be displayed in the admin list view.
    """

    list_display = (
        'company_name',
        'phone',
        'registration_number',
        'address',
        'iban',
        'user'
    )


class CustomPolicy(admin.ModelAdmin):
    """Admin model customization for the Policy model.
    Attributes:
        list_display (tuple): The fields to be displayed in the admin list view.
    Methods:
        get_pet_name: Retrieve the name of the associated pet.
    """

    list_display = (
        'policy_number',
        'start_date',
        'end_date',
        'status',
        'price',
        'initial_limit',
        'current_limit',
        'deductible',
        'get_pet_name'
    )

    @admin.display(description="Pet's name")
    def get_pet_name(self, obj):
        """Retrieves the name of the associated pet.
        Args:
            self (CustomPolicy): The CustomPolicy instance.
            obj (Policy): The Policy object.
        Returns:
            str: The name of the associated pet.
        Raises:
            None
        Notes:
            This method is used as a custom display function for the 'get_pet_name' field in the admin list view.
        """
        return obj.pet.name


class CustomInsuranceCase(admin.ModelAdmin):
    """Admin model customization for the InsuranceCase model.
    Attributes:
        list_display (tuple): The fields to be displayed in the admin list view.
    Methods:
        get_service_provider: Retrieve the name of the associated service provider.
    """

    list_display = (
        'claim_date',
        'description',
        'status',
        'service_provider',
        'get_service_provider'
    )

    @admin.display(description='service_provider_name')
    def get_service_provider(self, obj):
        """Retrieves the name of the associated service provider.
        Args:
            self (CustomInsuranceCase): The CustomInsuranceCase instance.
            obj (InsuranceCase): The InsuranceCase object.
        Returns:
            str: The name of the associated service provider.
        Raises:
            None
        Notes:
            This method is used as a custom display function for the 'get_service_provider'
            field in the admin list view.
        """
        return obj.service_provider.company_name


class CustomIncomingInvoice(admin.ModelAdmin):
    """Admin model customization for the IncomingInvoice model.
    Attributes:
        list_display (tuple): The fields to be displayed in the admin list view.
    """

    list_display = (
        'invoice_date',
        'amount',
        'insurance_case'
    )


admin.site.register(models.ServiceProvider, CustomServiceProvider)
admin.site.register(models.Policy, CustomPolicy)
admin.site.register(models.InsuranceCase, CustomInsuranceCase)
admin.site.register(models.IncomingInvoice, CustomIncomingInvoice)
