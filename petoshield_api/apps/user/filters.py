from django_filters import rest_framework as filters
from apps.user.models import Role, User


class RoleFilter(filters.FilterSet):
    class Meta:
        model = Role
        fields = {
            'name': ['exact', 'icontains']
        }


class UserFilter(filters.FilterSet):
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
