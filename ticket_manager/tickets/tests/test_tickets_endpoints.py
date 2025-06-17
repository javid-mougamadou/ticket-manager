import pytest
from rest_framework.test import APIClient
from ticket_manager.tickets.models import Ticket


@pytest.mark.django_db
class TestTicketViewSet:
    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def tickets(self):
        return [Ticket.objects.create(title=f"Test ticket {i}") for i in range(5)]

    @pytest.fixture
    def ticket(self):
        return Ticket.objects.create(title="Test ticket 1")

    def test_list_tickets(self, client, tickets):
        response = client.get("/api/tickets/")
        assert response.status_code == 200

        response_data = response.json()
        expected_fields = {"id", "title", "description", "status", "created_date"}

        for ticket_data in response_data:
            assert set(ticket_data.keys()) == expected_fields

        for ticket in tickets:
            matched = next((t for t in response_data if t["id"] == ticket.id), None)
            assert matched is not None
            assert matched["title"] == ticket.title
            assert matched["description"] == ticket.description
            assert matched["status"] == ticket.status

    def test_retrieve_ticket(self, client, ticket):
        response = client.get(f"/api/tickets/{ticket.id}/")
        assert response.status_code == 200

        ticket_data = response.json()
        assert ticket_data["title"] == ticket.title
        assert ticket_data["description"] == ticket.description
        assert ticket_data["status"] == ticket.status

    def test_create_ticket(self, client):
        payload = {
            "title": "New Ticket",
            "description": "New Description",
        }

        response = client.post("/api/tickets/", payload, format="json")
        assert response.status_code == 201

        ticket = Ticket.objects.get(title=payload["title"])
        assert ticket.title == payload["title"]
        assert ticket.description == payload["description"]
        assert ticket.status == "open"

    def test_update_ticket(self, client, ticket):
        payload = {
            "title": "Updated Ticket",
            "description": "Updated Description",
        }
        response = client.put(f"/api/tickets/{ticket.id}/", payload, format="json")
        assert response.status_code == 200

        ticket_data = response.json()
        assert ticket_data["title"] == payload["title"]
        assert ticket_data["description"] == payload["description"]

        ticket.refresh_from_db()
        assert ticket.title == payload["title"]
        assert ticket.description == payload["description"]

    def test_close_ticket(self, client, ticket):
        response = client.patch(
            f"/api/tickets/{ticket.id}/close/",
        )
        assert response.status_code == 204

        ticket.refresh_from_db()
        assert ticket.status == "closed"
