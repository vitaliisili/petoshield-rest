from django.contrib import admin
from . import models


class CustomTicket(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "visitor_name",
        "visitor_email",
        "get_description",
        "ticket_status",
    )

    @admin.display(description="Visitor Message")
    def get_description(self, obj):
        if len(obj.visitor_message) > 50:
            return f"{obj.visitor_message[:50]}..."

        return f"{obj.visitor_message[:50]}"


admin.site.register(models.Ticket, CustomTicket)
