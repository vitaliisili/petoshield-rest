from django.shortcuts import render
from rest_framework import viewsets

from apps.core.utils import EmailSender
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import AnyCreateOnlyStaffUpdate


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = TicketSerializer
    
    def update(self, request, *args, **kwargs):
        EmailSender.send_reply_to_ticket(self.pk, self.visitor_email, self.company_reply, request.META.get('HTTP_REFERER'))
        return super().update(request, *args, **kwargs)
