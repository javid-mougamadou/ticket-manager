import pytest
from pytest_bdd import scenarios, given, when, then
from ticket_manager.tickets.models import Ticket

pytestmark = pytest.mark.django_db
scenarios("test_tickets.feature")


@given("the API client")
def api_client(client):
    return client


@given("there are 5 existing tickets")
def create_tickets(tickets):
    return tickets


@when("I list the tickets")
def list_tickets(api_client, context):
    response = api_client.get("/api/tickets/")
    context["list_response"] = response


@then("I should get 5 tickets with all expected fields")
def check_ticket_list(create_tickets, context):
    response = context["list_response"]
    assert response.status_code == 200

    expected_fields = {"id", "title", "description", "status", "created_date"}
    data = response.json()
    assert len(data) == 5
    for ticket in data:
        assert set(ticket.keys()) == expected_fields


@when("I retrieve the first ticket")
def retrieve_first_ticket(api_client, ticket, context):
    response = api_client.get(f"/api/tickets/{ticket.id}/")
    context["retrieve_response"] = response
    context["target_ticket"] = ticket


@then("the ticket details should match")
def validate_retrieved_ticket(context):
    response = context["retrieve_response"]
    ticket = context["target_ticket"]

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == ticket.title
    assert data["description"] == ticket.description
    assert data["status"] == ticket.status


@when("I close the ticket")
def close_ticket(api_client, ticket, context):
    response = api_client.patch(f"/api/tickets/{ticket.id}/close/")
    context["close_response"] = response
    context["closed_ticket"] = ticket


@then('the ticket status should be "closed"')
def validate_ticket_closed(context):
    response = context["close_response"]
    assert response.status_code == 204

    ticket = Ticket.objects.get(id=context["closed_ticket"].id)
    assert ticket.status == "closed"
