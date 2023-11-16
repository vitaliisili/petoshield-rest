from django_filters import rest_framework as filters
from .models import Ticket


class TicketFilter(filters.FilterSet):
    class Meta:
        model = Ticket
        fields = {
            'visitor_name': ['iexact', 'icontains'],
            'visitor_email': ['iexact', 'icontains'],
            'visitor_message': ['icontains'],
            'ticket_status': ['exact'],
            'created_at': ['exact', 'gt', 'lt'],
        }
