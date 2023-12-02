import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from apps.payment.models import StripeSession, StripeCustomer, StripeSubscription
from apps.pet.models import Breed, Pet
from apps.policy.models import Policy
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
def raw_password():
    return 'password1A@'


@pytest.fixture
def staff_user(roles, raw_password):
    user_staff = get_user_model().objects.create_superuser('admin@mail.com', raw_password)
    assert user_staff.email == 'admin@mail.com'
    assert user_staff.is_superuser
    assert user_staff.is_staff
    return user_staff


@pytest.fixture
def simple_user(roles, raw_password):
    simple_user = get_user_model().objects.create_user(email='simple_user@mail.com',
                                                       password=raw_password,
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
def policy(pet):
    policy_ex = Policy.objects.create(
        policy_number='84-121-4860',
        start_date='2023-11-01',
        end_date='2024-11-01',
        status='valid',
        price=12.58,
        initial_limit=100000,
        current_limit=100000,
        deductible=1000,
        pet=pet
    )
    return policy_ex


@pytest.fixture
def stripe_session(policy):
    session = StripeSession.objects.create(session_id='123-3423dfsf-32mnb', policy=policy)
    assert session.session_id == '123-3423dfsf-32mnb'
    assert session.policy.policy_number == policy.policy_number

    return session


@pytest.fixture
def stripe_customer(db):
    customer = StripeCustomer.objects.create(id='test', name='test name')
    assert customer.id == 'test'
    assert customer.name == 'test name'

    return customer


@pytest.fixture
def stripe_subscription(stripe_customer, policy):
    subscription = StripeSubscription.objects.create(
        id='test',
        price=1.21,
        stripe_customer=stripe_customer,
        policy=policy)
    assert subscription.id == 'test'
    assert subscription.stripe_customer.id == stripe_customer.id

    return subscription
