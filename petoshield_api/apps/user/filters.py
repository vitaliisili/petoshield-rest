from django_filters import rest_framework as filters
from apps.user.models import Role, User

class RoleFilter(filters.FilterSet):
    class Meta:
        model = Role
        fields = {
            'name': ['icontains']
        }
        
class UserFilter(filters.FilterSet):
    role = filters.CharFilter(field_name='role__name', lookup_expr='icontains')
    
    class Meta:
        model = User
        fields = {
            'name': ['icontains'],
            'email': ['exact'],
            'created_at': ['exact', 'gt', 'lt'],
            'is_active': ['icontains']
        }