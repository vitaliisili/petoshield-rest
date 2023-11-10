from django.contrib import admin
from apps.user.models import User, Role


class CustomUser(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'is_active',
        'get_role',
        'is_staff',
        'is_verified',
        'created_at',
        'updated_at'
    )

    @admin.display(description='Role')
    def get_role(self, obj):
        return obj.role.name


class CustomRole(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )


admin.site.register(Role, CustomRole)
admin.site.register(User, CustomUser)
