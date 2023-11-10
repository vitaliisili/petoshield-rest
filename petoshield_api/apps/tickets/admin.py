from django.contrib import admin

from . import models
# Register your models here.

class CustomTicket(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "get_description",
        "ticket_status",
    )
    
    @admin.display(description="visitor_message")
    def get_description(self, obj):
        if len(obj.visitor_message) > 50:
            return f"{obj.description[:50]}..."
        
        return f"{obj.description[:50]}"

admin.site.register(models.Ticket, CustomTicket)