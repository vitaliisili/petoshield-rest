from rest_framework import viewsets
from .models import Ticket, PartnerTicket, JobTicket
from .serializers import TicketSerializer, JobTicketSerializer, PartnerTicketSerializer
from .permissions import AnyCreateOnlyStaffUpdate
from .filters import TicketFilter, JobTicketFilter, PartnerTicketFilter


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = TicketSerializer
    ordering_fields = ['created_at', 'visitor_name', 'visitor_email', 'ticket_status']
    ordering = ['-created_at']
    filterset_class = TicketFilter
    search_fields = ['$visitor_email', '$visitor_message']

    def create(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # email = serializer.data.get('visitor_email')
        # TODO: Send notification email that ticket received

        return super().create(request, *args, **kwargs)


class JobTicketViewSet(viewsets.ModelViewSet):
    queryset = JobTicket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = JobTicketSerializer
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    filterset_class = JobTicketFilter
    search_fields = ['$position', '$last_name', 'email']

    def create(self, request, *args, **kwargs):
        serializer = JobTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # email = serializer.data.get('email')
        # TODO: Send notification email that ticket received

        return super().create(request, *args, **kwargs)


class PartnerTicketViewSet(viewsets.ModelViewSet):
    queryset = PartnerTicket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = PartnerTicketSerializer
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    filterset_class = PartnerTicketFilter
    search_fields = ['$business_name', '$name', 'email']

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = PartnerTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # email = serializer.data.get('email')
        # TODO: Send notification email that ticket received

        return super().create(request, *args, **kwargs)
