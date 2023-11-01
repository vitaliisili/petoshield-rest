from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filter
from django_filters.widgets import RangeWidget
from .models import Breed, Pet
from apps.user.models import User

BREED_SPECIES = (
        ('cat', _('Cat')),
        ('dog', _('Dog')),
    )
PET_GENDER = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
class BreedFilterSet(filter.FilterSet):
    name = filter.CharFilter(field_name='name', lookup_expr='icontains')
    age_min = filter.NumberFilter(field_name='age_min',lookup_expr='exact')
    age_max = filter.NumberFilter(field_name='age_max', lookup_expr='exact')
    risk_level = filter.NumberFilter(field_name='risk_level', lookup_expr='exact')
    species = filter.ChoiceFilter(choices=BREED_SPECIES)
    
    class Meta:
        model = Breed
        fields = ('name', 'age_min', 'age_max', 'risk_level', 'species')
        
class PetFilterSet(filter.FilterSet):
    name = filter.CharFilter(field_name='name', lookup_expr='icontains')
    age = filter.NumberFilter(field_name='age',lookup_expr='exact')
    gender = filter.ChoiceFilter(choices=PET_GENDER)
    breed = filter.ChoiceFilter(choices=BREED_SPECIES)
    user = filter.CharFilter(field_name='user__name', lookup_expr='icontains')
        
    class Meta:
        model = Pet
        fields = ('name','age', 'gender', 'species', 'breed', 'user')