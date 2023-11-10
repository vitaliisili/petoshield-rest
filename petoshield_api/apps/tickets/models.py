from collections.abc import Iterable
from django.db import models

from apps.core.models import BaseModel
from apps.user.models import User
# Create your models here.

class Ticket(BaseModel):
    
    STATUS = (
        ('new', '0'),
        ('in process', '1'),
        ('closed', '2'),
    )

    ticket_number = models.CharField(max_length=125)
    ticket_status = models.CharField(choices=STATUS, default=STATUS[0])
    
    user_name = models.CharField(max_length=125)
    user_email = models.EmailField()
    user_message = models.TextField(max_length=1000)
    
    is_client = models.BooleanField(default=False)
    company_reply = models.TextField(max_length=1000, blank=True, null=True)
    
    def save(self):
        if User.objects.filter(email=self.user_email).exists():
            self.is_client = True
        return super().save()
    
    def __str__(self) -> str:
        return f'{self.ticket_number}|{self.user_message[:50]}'
    