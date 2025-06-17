import pytest
from ticket_manager.tickets.models import Ticket, TicketStatuses


@pytest.mark.django_db
class TestTicketModel:
    def test_change_status(self):
        ticket = Ticket.objects.create(
            title="Test ticket", description="Test description"
        )

        assert ticket.status == TicketStatuses.OPEN

        ticket.change_status(TicketStatuses.STALLED)
        ticket.refresh_from_db()
        assert ticket.status == TicketStatuses.STALLED

    def test_close_method(self):
        ticket = Ticket.objects.create(
            title="Test ticket", description="Test description"
        )

        ticket.closed()
        ticket.refresh_from_db()
        assert ticket.status == TicketStatuses.CLOSED
