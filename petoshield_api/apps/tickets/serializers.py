from rest_framework import serializers
from .models import Ticket, JobTicket, PartnerTicket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only = ['id', 'created_at', 'updated_at']


class JobTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTicket
        fields = '__all__'
        read_only = ['id', 'created_at', 'updated_at']


class PartnerTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerTicket
        fields = '__all__'
        read_only = ['id', 'created_at', 'updated_at']
