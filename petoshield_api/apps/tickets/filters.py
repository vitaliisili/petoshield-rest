from django_filters import rest_framework as filters
from apps.tickets.models import JobTicket, PartnerTicket, Ticket, JobTicket, PartnerTicket


class TicketFilter(filters.FilterSet):
    class Meta:
        model = Ticket
        fields = {
            'visitor_name': ['exact', 'icontains'],
            'visitor_email': ['exact', 'icontains'],
            'visitor_message': ['icontains'],
            'ticket_status': ['exact'],
            'created_at': ['exact', 'gt', 'lt'],
        }

class JobTicketFilter(filters.FilterSet):

    class Meta:
        model = JobTicket
        fields = {
            'position': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'email': ['exact']
        }


class PartnerTicketFilter(filters.FilterSet):

    class Meta:
        model = PartnerTicket
        fields = {
            'name': ['exact', 'icontains'],
            'business_name': ['exact', 'icontains'],
            'email': ['exact'],
            'url': ['exact']
        }

class JobTicketFilter(filters.FilterSet):
    class Meta:
        model = JobTicket
        fields = {
            'position': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'email': ['exact'],
        }


class PartnerTicketFilter(filters.FilterSet):
    class Meta:
        model = PartnerTicket
        fields = {
            'name': ['exact', 'icontains'],
            'business_name': ['exact', 'icontains'],
            'email': ['exact'],
            'message': ['icontains'],
            'url': ['exact', 'icontains'],
        }
