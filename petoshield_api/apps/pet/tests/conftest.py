import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.pet.models import Pet, Breed

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def staff_user(db):
    user_staff = get_user_model().objects.create_superuser('admin@mail.com', 'password1A@')
    assert user_staff.email == 'admin@mail.com'
    assert user_staff.is_superuser
    assert user_staff.is_staff
    return user_staff

@pytest.fixture
def simple_user(db):
    simple_user = get_user_model().objects.create_user(
        email='simple_user@mail.com', password='password1A@', name='Simple User')

    assert simple_user.email == 'simple_user@mail.com'
    assert not simple_user.is_superuser
    assert not simple_user.is_staff
    return simple_user


@pytest.fixture
def users_list(db, staff_user, simple_user):
    users_list = [
        staff_user,
        simple_user,
        get_user_model().objects.create_user(email='example1@mail.com', password='password1A@', name='Example Name1'),
        get_user_model().objects.create_user(email='example2@mail.com', password='password1A@', name='Example Name2'),
        get_user_model().objects.create_user(email='example3@mail.com', password='password1A@', name='Example Name3'),
    ]
    return users_list

@pytest.fixture
def breed(db):
    breed = Breed.objects.create(
        name='German Shepherd',
        age_min=8,
        age_max=12,
        risk_level=3,
        species='dog'
    )
    return breed

@pytest.fixture
def pet_created_by_admin(db,breed,admin_user):
    pet_created_by_admin = Pet.objects.create(
        name='Admin Name',
        age=5,
        gender='M',
        species='dog',
        breed=f'{breed.id}',
        user=f'{admin_user.id}'
        )
    return pet_created_by_admin

@pytest.fixture
def pet_created_by_user(db,breed,simple_user):
    pet_created_by_admin = Pet.objects.create(
        name='Simple User dog 1',
        age=5,
        gender='M',
        species='dog',
        breed=f'{breed.id}',
        user=f'{simple_user.id}'
        )
    return pet_created_by_admin

@pytest.fixture
def breeds_list(db,breed):
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
def pets_list(db,breed, pet_created_by_admin,pet_created_by_user, simple_user, admin_user):
    pets_list = [
        pet_created_by_admin,
        pet_created_by_user,
        Pet.objects.create(
            name='Simple User dog',
            age=5,
            gender='M',
            species='dog',
            breed=f'{breed.id}',
            user=f'{simple_user.id}'
            ),
        
        Pet.objects.create(
            name='Jack',
            age=3,
            gender='M',
            species='dog',
            breed=f'{breed.id}',
            user=f'{admin_user.id}'
            ),

        Pet.objects.create(
            name='Thomas',
            age=8,
            gender='M',
            species='dog',
            breed=f'{breed.id}',
            user=f'{admin_user.id}'
            ),
        Pet.objects.create(
            name='Leo Simple User',
            age=5,
            gender='M',
            species='dog',
            breed=f'{breed.id}',
            user=f'{simple_user.id}'
            ),  
        Pet.objects.create(
            name='Linda',
            age=7,
            gender='F',
            species='cat',
            breed=f'{breed.id}',
            user=f'{simple_user.id}'
            ),       
    ]
    return pets_list
    
