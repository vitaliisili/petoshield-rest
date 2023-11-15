from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import AnyCreateOnlyStaffUpdate


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = TicketSerializer
