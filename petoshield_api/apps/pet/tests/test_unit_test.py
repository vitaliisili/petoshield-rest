import pytest
from django.contrib import admin
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.pet.admin import CustomBreed
from apps.pet.models import Breed


class TestBreedUnitTest:

    @pytest.fixture
    def valid_breed_data(self):
        return {
            'name': 'Test Breed',
            'description': 'Test description',
            'age_min': 1,
            'age_max': 10,
            'risk_level': 5,
            'species': 'dog',
        }

    def test_breed_string_representation(self, breed):
        assert str(breed) == breed.name

    def test_breed_admin_get_description(self):
        breed = Breed(
            name='Test Breed',
            species='Test Species',
            age_min=1,
            age_max=10,
            risk_level='High',
            description='This is a test description that is longer than 50 characters.'
        )
        admin_instance = CustomBreed(Breed, admin.site)
        result = admin_instance.get_description(breed)
        assert len(result) > 0

        breed.description = 'Short description'
        result = admin_instance.get_description(breed)
        assert result == 'Short description'

    @pytest.mark.django_db
    def test_breed_model_save_valid_breed(self, valid_breed_data):
        breed = Breed(**valid_breed_data)
        breed.save()
        assert breed.pk is not None

    def test_breed_model_clean_negative_age(self, valid_breed_data):
        valid_breed_data['age_min'] = -1
        breed = Breed(**valid_breed_data)

        with pytest.raises(ValidationError) as e:
            breed.full_clean()

        assert str(_('Age cannot be negative.')) in str(e.value)

    def test_breed_model_clean_minimum_age(self, valid_breed_data):
        valid_breed_data['age_min'] = 0
        breed = Breed(**valid_breed_data)

        with pytest.raises(ValidationError) as e:
            breed.full_clean()

        assert str(_('Minimum age should be 1 or greater.')) in str(e.value)

    def test_breed_model_clean_maximum_age(self, valid_breed_data):
        valid_breed_data['age_max'] = 31
        breed = Breed(**valid_breed_data)

        with pytest.raises(ValidationError) as e:
            breed.full_clean()

        assert str(_('Maximum age should be 30 or less.')) in str(e.value)

    def test_breed_model_clean_minimum_age_greater_than_maximum_age(self, valid_breed_data):
        valid_breed_data['age_min'] = 10
        valid_breed_data['age_max'] = 5
        breed = Breed(**valid_breed_data)

        with pytest.raises(ValidationError) as e:
            breed.full_clean()

        assert str(_('Minimum age should be less than maximum age.')) in str(e.value)


class TestPetUnitTest:

    def test_pet_string_representation(self, pet):
        assert str(pet) == pet.name
