from django.db import models
from apps.core.models import BaseModel


class Ticket(BaseModel):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_process', 'In Process'),
        ('closed', 'Closed'),
    )
    visitor_name = models.CharField(max_length=125)
    visitor_email = models.EmailField()
    visitor_message = models.TextField(max_length=1000)
    ticket_status = models.CharField(choices=STATUS_CHOICES, default='new')

    def __str__(self) -> str:
        return f'Ticket|{self.pk}|{self.user_message[:50]}'


class JobTicket(BaseModel):
    position = models.CharField(max_length=250)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.position}'


class PartnerTicket(BaseModel):
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    url = models.URLField()

    def __str__(self) -> str:
        return f'{self.business_name}'
