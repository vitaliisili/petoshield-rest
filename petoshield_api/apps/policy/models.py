from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
from apps.pet.models import Pet
from config import settings


class ServiceProvider(BaseModel):
    """Model representing a service provider.
    Attributes:
        company_name (CharField): The name of the company. Max length is 255 characters.
        phone (CharField): The phone number of the company. Max length is 15 characters.
        registration_number (CharField): The registration number of the company. Max length is 255 characters.
        address (CharField): The address of the company. Max length is 255 characters.
        iban (CharField): The IBAN of the company. Max length is 34 characters.
        user (ForeignKey): The user associated with the service provider.
    Methods:
        __str__: Returns the company name.
    """

    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    iban = models.CharField(max_length=34)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='provider')

    def __str__(self):
        """Returns the company name.
        Returns:
            str: The company name.
        """
        return self.company_name


class Policy(BaseModel):
    """Model representing a policy.
    Attributes:
        POLICY_STATUS (tuple): Choices for the status of the policy.
        policy_number (CharField): The policy number. Max length is 255 characters. Must be unique.
        start_date (DateField): The start date of the policy.
        end_date (DateField): The end date of the policy.
        status (CharField): The status of the policy. Max length is 20 characters. Choices are 'valid',
        'invalid', and 'expired'.
        price (DecimalField): The price of the policy. Max digits is 8. Decimal places is 2.
        Default is POLICY_BASE_PRICE from settings.
        initial_limit (DecimalField): The initial limit of the policy. Max digits is 8. Decimal places is 2.
        current_limit (DecimalField): The current limit of the policy. Max digits is 8. Decimal places is 2.
        deductible (DecimalField): The deductible of the policy. Max digits is 6. Decimal places is 2.
        pet (ForeignKey): The pet associated with the policy.
    Methods:
        __str__: Returns the policy number.
    Meta:
        verbose_name_plural (str): The plural name for the model.
    """

    POLICY_STATUS = (
        ('valid', _('Valid')),
        ('invalid', _('Invalid')),
        ('expired', _('Expired')),
    )
    policy_number = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=POLICY_STATUS)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=settings.POLICY_BASE_PRICE)
    initial_limit = models.DecimalField(max_digits=8, decimal_places=2)
    current_limit = models.DecimalField(max_digits=8, decimal_places=2)
    deductible = models.DecimalField(max_digits=6, decimal_places=2)
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, related_name='policy', null=True)

    def __str__(self):
        """Returns the policy number.
        Returns:
            str: The policy number.
        """
        return self.policy_number

    class Meta:
        """Meta-options for the Policy model.
        Attributes:
            verbose_name_plural (str): The plural name for the model.
        """
        verbose_name_plural = 'policies'


class InsuranceCase(BaseModel):
    """Model representing an insurance case.
    Attributes:
        INSURANCE_STATUS (tuple): Choices for the status of the insurance case.
        claim_date (DateField): The date of the insurance claim.
        description (TextField): The description of the insurance case.
        status (CharField): The status of the insurance case. Max length is 20 characters.
        Choices are 'accept', 'process', and 'reject'.
        policy (ForeignKey): The policy associated with the insurance case.
        service_provider (ForeignKey): The service provider associated with the insurance case.
    Methods:
        __str__: Returns a formatted string representation of the insurance case.
    """

    INSURANCE_STATUS = (
        ('accept', _('Accept')),
        ('process', _('Process')),
        ('reject', _('Reject')),
    )
    claim_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=INSURANCE_STATUS, default='process')
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='insurance_cases')
    service_provider = models.ForeignKey(ServiceProvider,
                                         on_delete=models.SET_NULL,
                                         related_name='insurance_cases',
                                         null=True)

    def __str__(self):
        """Returns a formatted string representation of the insurance case.
        Returns:
            str: A formatted string representation of the insurance case.
        """
        return f'{self.claim_date}-{self.status}'


class IncomingInvoice(BaseModel):
    """Model representing an incoming invoice.
    Attributes:
        invoice_date (DateField): The date of the invoice.
        amount (DecimalField): The amount of the invoice. Max digits is 8 and decimal places is 2.
        insurance_case (ForeignKey): The insurance case associated with the invoice.
    Methods:
        __str__: Returns a formatted string representation of the invoice.
    """

    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    insurance_case = models.ForeignKey(InsuranceCase, on_delete=models.CASCADE, related_name='incoming_invoice')

    def __str__(self):
        """Returns a formatted string representation of the invoice.
        Returns:
            str: A formatted string representation of the invoice.
        """
        return f'{self.amount}'
