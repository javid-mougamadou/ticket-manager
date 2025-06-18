import pytest
from rest_framework.test import APIClient
from ticket_manager.tickets.models import Ticket


### GHERKIN FIXTURE


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def tickets(db):
    return [
        Ticket.objects.create(
            title=f"Test ticket {i}",
            description=f"Description {i}",
        )
        for i in range(5)
    ]


@pytest.fixture
def ticket(db):
    return Ticket.objects.create(
        title="Test ticket",
        description="Test description",
    )


@pytest.fixture
def context():
    return {}


@pytest.fixture
def create_tickets(tickets):
    return tickets
