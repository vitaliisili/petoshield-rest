from django.db import models
from apps.core.models import BaseModel
from apps.user.models import User


class Ticket(BaseModel):

    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_process', 'In Process'),
        ('closed', 'Closed'),
    )
    visitor_name = models.CharField(max_length=125)
    visitor_email = models.EmailField()
    visitor_message = models.TextField(max_length=1000)

    is_client = models.BooleanField(default=False)
    ticket_status = models.CharField(choices=STATUS_CHOICES, default='new')

    def save(self):
        if User.objects.filter(email=self.visitor_email).exists():
            self.is_client = True
        return super().save()

    def __str__(self) -> str:
        return f'Ticket|{self.pk}|{self.user_message[:50]}'

    class Meta:
        verbose_name_plural = 'tickets'