from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel

def get_default_breed():
    return Breed.objects.get_or_create(name='deleted', age_min=1, age_max=20)[0]

class Breed(BaseModel):
    BREED_SPECIES = (
        ('cat', _('Cat')),
        ('dog', _('Dog')),
    )

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    age_min = models.IntegerField()
    age_max= models.IntegerField()
    risk_level = models.IntegerField(choices=[(i, i) for i in range(11)], default=5)
    species = models.CharField(max_length=3, choices=BREED_SPECIES)
    
    def __str__(self):
        return self.name

class Pet(BaseModel):
    PET_GENDER = (
        ('M', _('Male')),
        ('F', _('Female')),
    )

    PET_SPECIES = (
        ('cat', _('Cat')),
        ('dog', _('Dog')),
    )

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=PET_GENDER)
    species = models.CharField(max_length=3, choices=PET_SPECIES)
    breed = models.ForeignKey(Breed, on_delete=models.SET(get_default_breed), related_name='pets')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pets')
    
    def __str__(self):
        return self.name