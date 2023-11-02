from django_filters import rest_framework as filters
from apps.pet.models import Breed, Pet

class BreedFilter(filters.FilterSet):
    class Meta:
        model = Breed
        fields = {
            'name': ['icontains'],
            'age_min': ['exact', 'gt', 'lt'],
            'age_max': ['exact', 'gt', 'lt'],
            'risk_level': ['exact', 'gt', 'lt'],
            'species': ['icontains']
        }
        
class PetFilter(filters.FilterSet):
    breed = filters.CharFilter(field_name='breed__name', lookup_expr='icontains')
    user = filters.CharFilter(field_name='user__name', lookup_expr='icontains')
    
    class Meta:
        model = Pet
        fields = {
            'name': ['icontains'],
            'age': ['exact', 'gt', 'lt'],
            'gender': ['icontains'],
            'species': ['icontains']
        }