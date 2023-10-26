from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.user.models import User

class CustomUser(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'is_active',
        'is_staff',
        'created_at',
        'updated_at'
    )
    
admin.site.register(User, CustomUser)
