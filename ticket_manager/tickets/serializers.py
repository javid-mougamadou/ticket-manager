from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    """
    Serializer for Ticket instance

    fields = ('id', 'title', 'description', 'status', 'created_date')
    """

    class Meta:
        model = Ticket
        fields = ("id", "title", "description", "status", "created_date")
