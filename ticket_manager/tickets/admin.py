from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "created_date")
    list_filter = ("status",)
    search_fields = ("title", "description")
    readonly_fields = ("created_date", "updated_date")
