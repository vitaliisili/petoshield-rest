from django.shortcuts import render
from rest_framework import viewsets

from .models import Ticket
from .serializers import TicketSerializer
from .permissions import AnyCreateOnlyStaffUpdate


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = TicketSerializer
    
    def update(self, request, *args, **kwargs):
        #TODO: send email with a company reply
        return super().update(request, *args, **kwargs)
