from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import AnyCreateOnlyStaffUpdate
from .filters import TicketFilter


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = TicketSerializer
    ordering_fields = ['created_at', 'visitor_name', 'visitor_email', 'ticket_status']
    ordering = ['-created_at']
    filterset_class = TicketFilter
    search_fields = ['$visitor_email', '$visitor_message']
