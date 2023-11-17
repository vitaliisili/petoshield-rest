from apps.core import models as core_model
from django.db import models
from apps.policy.models import Policy


class StripeSession(core_model.BaseModel):
    session_id = models.TextField()
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='session')
