Feature: Ticket management

  Scenario: Full ticket lifecycle
    Given the API client
    And there are 5 existing tickets

    When I list the tickets
    Then I should get 5 tickets with all expected fields

    When I retrieve the first ticket
    Then the ticket details should match

    When I close the ticket
    Then the ticket status should be "closed"
