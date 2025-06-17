from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    A ViewSet for listing, retrieving, creating, updating, and closing Ticket instances.

    list:
    List all tickets
    * Accessible to unauthenticated users

    retrieve:
    Retrieve a ticket by ID
    * Accessible to unauthenticated users

    create:
    Create a new ticket
    * Unauthenticated users can create a ticket
    * Requires `title` and optionally `description`

    update:
    Update an existing ticket
    * Unauthenticated users can update a ticket

    partial_update:
    Partially update a ticket
    * Unauthenticated users can update a ticket

    close:
    Close a ticket
    * Unauthenticated users can close a ticket
    """

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @swagger_auto_schema(
        operation_description="Close a ticket.",
        responses={204: "Ticket successfully closed", 404: "Ticket not found"},
    )
    @action(detail=True, methods=["patch"])
    def close(self, request, pk=None):
        """
        Custom action to close a ticket (sets status to 'closed').
        """
        ticket = self.get_object()
        ticket.closed()
        return Response(status=status.HTTP_204_NO_CONTENT)
