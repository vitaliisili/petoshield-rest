from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
from apps.pet.models import Pet


class ServiceProvider(BaseModel):
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    iban = models.CharField(max_length=34)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='provider')

class Policy(BaseModel):
    POLICY_STATUS = (
        ('valid', _('Valid')),
        ('invalid', _('Invalid')),
        ('expired', _('Expired')),
    )

    policy_number = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=POLICY_STATUS)
    initial_limit = models.DecimalField(max_digits=8, decimal_places=2)
    current_limit = models.DecimalField(max_digits=8, decimal_places=2)
    deductible = models.DecimalField(max_digits=6, decimal_places=2)
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, related_name='policies', null=True)
    providers = models.ManyToManyField(ServiceProvider, related_name='policies')


    class Meta:
        verbose_name_plural = 'policies'

class InsuranceCase(BaseModel):
    INSURANCE_STATUS = (
        ('accept', _('Accept')),
        ('process', _('Process')),
        ('reject', _('Reject')),
    )

    claim_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=INSURANCE_STATUS, default='process')
    service_provider = models.ForeignKey(
        ServiceProvider, on_delete=models.SET_NULL, related_name='insurance_cases', null=True)

class IncomingInvoice(BaseModel):
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    insurance_case = models.OneToOneField(InsuranceCase, on_delete=models.CASCADE, related_name='incoming_invoice')







