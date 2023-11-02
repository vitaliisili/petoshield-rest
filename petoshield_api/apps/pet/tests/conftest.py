import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.pet.models import Pet, Breed
from apps.user.models import Role


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def roles(db):
    custom_roles = [
        Role.objects.create(name='client'),
        Role.objects.create(name='admin'),
        Role.objects.create(name='provider'),
    ]
    return custom_roles


@pytest.fixture
def staff_user(roles):
    user_staff = get_user_model().objects.create_superuser('admin@mail.com', 'password1A@')
    assert user_staff.email == 'admin@mail.com'
    assert user_staff.is_superuser
    assert user_staff.is_staff
    return user_staff


@pytest.fixture
def simple_user(roles):
    simple_user = get_user_model().objects.create_user(email='simple_user@mail.com',
                                                       password='password1A@',
                                                       name='Simple User',
                                                       role=roles[0])

    assert simple_user.email == 'simple_user@mail.com'
    assert not simple_user.is_superuser
    assert not simple_user.is_staff
    return simple_user


@pytest.fixture
def provider_user(roles):
    provider = get_user_model().objects.create_user(email='provider@mail.com',
                                                    password='password1A@',
                                                    name='Provider User',
                                                    role=roles[2])
    return provider


@pytest.fixture
def breed(db):
    breed = Breed.objects.create(
        name='German Shepherd',
        age_min=8,
        age_max=12,
        risk_level=3,
        species='dog'
    )
    assert breed.name == 'German Shepherd'
    return breed


@pytest.fixture
def pet(breed, simple_user):
    custom_pet = Pet.objects.create(name='Lenore',
                                    age=5,
                                    gender='M',
                                    species='dog',
                                    breed=breed,
                                    user=simple_user)
    assert custom_pet.name == 'Lenore'
    return custom_pet


@pytest.fixture
def breeds_list(db):
    breeds_list = [
        # breed,
        Breed.objects.create(
            name='Siameses cat',
            age_min=10,
            age_max=13,
            risk_level=4,
            species='cat'
        ),
        Breed.objects.create(
            name='Ragdoll',
            age_min=9,
            age_max=11,
            risk_level=6,
            species='cat'
        ),
        Breed.objects.create(
            name='Arenol',
            age_min=9,
            age_max=11,
            risk_level=6,
            species='dog'
        ),
    ]
    return breeds_list


@pytest.fixture
def pets_list(breed, simple_user, staff_user):
    pets_list = [
        Pet.objects.create(
            name='Simple User dog',
            age=5,
            gender='M',
            species='dog',
            breed=breed,
            user=simple_user
        ),

        Pet.objects.create(
            name='Jack',
            age=3,
            gender='M',
            species='dog',
            breed=breed,
            user=simple_user
        ),
        Pet.objects.create(
            name='Samy',
            age=4,
            gender='F',
            species='cat',
            breed=breed,
            user=staff_user
        ),
    ]
    return pets_list
