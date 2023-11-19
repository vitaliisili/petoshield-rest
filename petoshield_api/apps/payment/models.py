from apps.core import models as core_model
from django.db import models
from apps.policy.models import Policy


class StripeSession(core_model.BaseModel):
    session_id = models.TextField()
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='session')


class StripeCustomer(models.Model):
    id = models.CharField(max_length=250, editable=False, primary_key=True)
    name = models.CharField(max_length=100)


class StripeSubscription(models.Model):
    id = models.CharField(max_length=250, editable=False, primary_key=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stripe_customer = models.OneToOneField(StripeCustomer, on_delete=models.CASCADE, related_name='subscription')
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='subscription')
