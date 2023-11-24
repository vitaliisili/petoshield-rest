from django.contrib import admin
from apps.user.models import User, Role


class CustomUser(admin.ModelAdmin):
    """Admin model customization for the User model.
    Attributes:
        list_display (tuple): The fields to be displayed in the admin list view.
    Methods:
        get_role: Retrieve the role name of the user.
    """

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
        """Retrieves the role name of the user.

        Args:
            self (CustomUser): The CustomUser instance.
            obj (User): The User object.
        Returns:
            str: The role name of the user.
        Raises:
            None
        Notes:
            This method is used as a custom display function for the 'get_role' field in the admin list view.
        """
        return obj.role.name


class CustomRole(admin.ModelAdmin):
    """Admin model customization for the Role model.
    Attributes:
        list_display (tuple): The fields to be displayed in the admin list view.

    """

    list_display = (
        'name',
        'description'
    )


admin.site.register(Role, CustomRole)
admin.site.register(User, CustomUser)
