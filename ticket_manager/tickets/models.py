from django.db import models


class TicketStatuses(models.TextChoices):
    OPEN = "open", "Open"
    STALLED = "stalled", "Stalled"
    CLOSED = "closed", "Closed"
    # IN_PROGRESS = 'in_progress', 'In Progress'
    # RESOLVED = 'resolved', 'Resolved'


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=TicketStatuses.choices, default=TicketStatuses.OPEN
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def change_status(self, new_status):
        self.status = new_status
        self.save(update_fields=["status"])

    def closed(self):
        self.change_status(TicketStatuses.CLOSED)

    def __str__(self):
        return f"#{self.id} Ticket: {self.title}"
