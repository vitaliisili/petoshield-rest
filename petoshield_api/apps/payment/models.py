from apps.core import models as core_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.policy.models import Policy


# class PolicySubscription(core_model.BaseModel):
#     FREQUENCY = [
#         ('annual', _('Annual')),
#         ('monthly', _('monthly')),
#     ]
#
#     final_price = models.DecimalField(max_digits=8, decimal_places=2)
#     frequency = models.CharField(max_length=7, choices=FREQUENCY)
#     # session_id = models.CharField(max_length=250)
#     # payment_status =
#     policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='policy_subscription')


class StripeSession(core_model.BaseModel):
    session_id = models.TextField()
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='session')
