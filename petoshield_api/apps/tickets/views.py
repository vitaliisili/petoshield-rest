from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from apps.tickets.models import Ticket, PartnerTicket, JobTicket
from apps.tickets.serializers import TicketSerializer, JobTicketSerializer, PartnerTicketSerializer
from apps.tickets.permissions import AnyCreateOnlyStaffUpdate
from apps.tickets.filters import TicketFilter, JobTicketFilter, PartnerTicketFilter
from apps.core.utils import EmailSender


@extend_schema(tags=['Ticket'])
class TicketViewSet(viewsets.ModelViewSet):
    """A viewset for interacting with the Ticket model."""

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

        email_data = {
            "name": serializer.data.get('visitor_name'),
            "email": serializer.data.get('visitor_email'),
        }

        EmailSender.send_mail_your_ticket_received(email_data)

        return super().create(request, *args, **kwargs)


@extend_schema(tags=['JobTicket'])
class JobTicketViewSet(viewsets.ModelViewSet):
    """A viewset for interacting with the JobTicket model."""

    queryset = JobTicket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = JobTicketSerializer
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    filterset_class = JobTicketFilter
    search_fields = ['$position']

    def create(self, request, *args, **kwargs):
        serializer = JobTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email_data = {
            "name": serializer.data.get('first_name') + ' ' + serializer.data.get('last_name'),
            "email": serializer.data.get('email'),
            "position": serializer.data.get('position'),
        }

        EmailSender.send_mail_job_ticket_received(email_data)

        return super().create(request, *args, **kwargs)


@extend_schema(tags=['PartnerTicket'])
class PartnerTicketViewSet(viewsets.ModelViewSet):
    """A viewset for interacting with the PartnerTicket model."""

    queryset = PartnerTicket.objects.all()
    permission_classes = (AnyCreateOnlyStaffUpdate,)
    serializer_class = PartnerTicketSerializer
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    filterset_class = PartnerTicketFilter
    search_fields = ['$business_name']

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = PartnerTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email_data = {
            "name": serializer.data.get('name'),
            "email": serializer.data.get('email'),
            "business_name": serializer.data.get('business_name'),
        }

        EmailSender.send_mail_partner_ticket_received(email_data)

        return super().create(request, *args, **kwargs)
