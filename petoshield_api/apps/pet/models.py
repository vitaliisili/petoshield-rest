from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from apps.core.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


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
    age_max = models.IntegerField()
    risk_level = models.IntegerField(validators=(MinValueValidator(1), MaxValueValidator(10)), default=5)
    species = models.CharField(max_length=3, choices=BREED_SPECIES)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def clean(self):
        if self.age_min < 0 or self.age_max < 0:
            raise ValidationError(_('Age cannot be negative.'))
        if self.age_min < 1:
            raise ValidationError(_('Minimum age should be 1 or greater.'))
        if self.age_max > 30:
            raise ValidationError(_('Maximum age should be 30 or less.'))
        if self.age_min > self.age_max:
            raise ValidationError(_('Minimum age should be less than maximum age.'))

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
    age = models.IntegerField(validators=(MinValueValidator(1), MaxValueValidator(10)))
    gender = models.CharField(max_length=1, choices=PET_GENDER)
    species = models.CharField(max_length=3, choices=PET_SPECIES)
    breed = models.ForeignKey(Breed, on_delete=models.SET(get_default_breed), related_name='pets')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.name
