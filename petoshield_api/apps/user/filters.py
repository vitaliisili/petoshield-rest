from django_filters import rest_framework as filters
from apps.user.models import Role, User


class RoleFilter(filters.FilterSet):
    """A filter class for the Role model.
    Meta:
        model (Role): The model to be filtered.
        fields (dict): The fields and lookup types to be used for filtering.
    """

    class Meta:
        model = Role
        fields = {
            'name': ['exact', 'icontains']
        }


class UserFilter(filters.FilterSet):
    """A filter class for the User model.

    Attributes:
        role (CharFilter): Filter for the 'role__name' field using the 'icontains' lookup.
        created_at__year__exact (NumberFilter): Filter for the 'created_at__year' field with exact matching.
        created_at__year__gt (NumberFilter): Filter for the 'created_at__year' field with greater than matching.
        created_at__year__lt (NumberFilter): Filter for the 'created_at__year' field with less than matching.

    Meta:
        model (User): The model to be filtered.
        fields (dict): The fields and lookup types to be used for filtering.
    """

    role = filters.CharFilter(field_name='role__name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')

    class Meta:
        model = User
        fields = {
            'name': ['exact', 'icontains'],
            'email': ['exact'],
            'created_at': ['exact', 'gt', 'lt'],
            'is_active': ['exact']
        }
