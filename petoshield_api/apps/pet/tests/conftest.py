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
def pet_created_by_admin(breed, staff_user):
    pet_created_by_admin = Pet.objects.create(
        name='Admin Name',
        age=5,
        gender='M',
        species='dog',
        breed=breed,
        user=staff_user
        )
    assert pet_created_by_admin.age == 5
    return pet_created_by_admin

@pytest.fixture
def pet_created_by_user(db, breed, simple_user):
    pet_created_by_user = Pet.objects.create(
        name='Simple User dog 1',
        age=5,
        gender='M',
        species='dog',
        breed=breed,
        user=simple_user
        )
    return pet_created_by_user

@pytest.fixture
def breeds_list(db, breed):
    breeds_list = [
        breed,
        Breed.objects.create(
            name='Bulldog',
            age_min=10,
            age_max=16,
            risk_level=6,
            species='dog'
            ),

        Breed.objects.create(
            name='Labrador',
            age_min=10,
            age_max=16,
            risk_level=6,
            species='dog'
            ),

        Breed.objects.create(
            name='Beagle',
            age_min=10,
            age_max=13,
            risk_level=4,
            species='dog'
            ),
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
    ]
    return breeds_list


@pytest.fixture
def pets_list(db, breed, pet_created_by_admin, pet_created_by_user, simple_user, staff_user):
    pets_list = [
        pet_created_by_admin,
        pet_created_by_user,
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
            user=staff_user
            ),

        Pet.objects.create(
            name='Thomas',
            age=8,
            gender='M',
            species='dog',
            breed=breed,
            user=staff_user
            ),
        Pet.objects.create(
            name='Leo Simple User',
            age=5,
            gender='M',
            species='dog',
            breed=breed,
            user=simple_user
            ),
        Pet.objects.create(
            name='Linda',
            age=7,
            gender='F',
            species='cat',
            breed=breed,
            user=simple_user
            ),
    ]
    return pets_list


