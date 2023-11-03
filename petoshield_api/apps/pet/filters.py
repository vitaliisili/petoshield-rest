from django_filters import rest_framework as filters
from apps.pet.models import Breed, Pet

class BreedFilter(filters.FilterSet):
    class Meta:
        model = Breed
        fields = {
            'name': ['exact', 'icontains'],
            'age_min': ['exact', 'gt', 'lt'],
            'age_max': ['exact', 'gt', 'lt'],
            'risk_level': ['exact', 'gt', 'lt'],
            'species': ['icontains']
        }
        
class PetFilter(filters.FilterSet):
    breed = filters.CharFilter(field_name='breed__name', lookup_expr='icontains')
    user = filters.CharFilter(field_name='user__name', lookup_expr='icontains')
    created_at__year__exact = filters.NumberFilter(field_name='created_at__year', lookup_expr='exact')
    created_at__year__gt = filters.NumberFilter(field_name='created_at__year', lookup_expr='gt')
    created_at__year__lt = filters.NumberFilter(field_name='created_at__year', lookup_expr='lt')
         
    class Meta:
        model = Pet
        fields = {
            'name': ['exact', 'icontains'],
            'age': ['exact', 'gt', 'lt'],
            'gender': ['icontains'],
            'species': ['icontains'],
            'created_at': ['exact', 'gt', 'lt']
        }