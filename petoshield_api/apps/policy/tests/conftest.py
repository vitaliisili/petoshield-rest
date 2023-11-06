import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.pet.models import Pet, Breed
from apps.policy.models import ServiceProvider, Policy, InsuranceCase, IncomingInvoice
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
def service_provider(simple_user):
    provider = ServiceProvider.objects.create(
        company_name = 'Service Provider 1',
        phone = '+49856547725',
        registration_number = '56899-5655-581',
        address = 'Musterstrasse3, 34332 MusterLand',
        iban = 'DE5689562365002354',
        user = simple_user
    )
    return provider

@pytest.fixture
def service_provider_list(service_provider, simple_user):
    provider_list = [
        service_provider,
        ServiceProvider.objects.create(
            company_name = 'Service Provider 2',
            phone = '+492222222222',
            registration_number = '56899-5655-582',
            address = 'Musterstrasse2, 34332 MusterLand2',
            iban = 'DE5689562365002222',
            user = simple_user
                 ),
        ServiceProvider.objects.create(
            company_name = 'Service Provider 3',
            phone = '+493333333333',
            registration_number = '56899-5655-583',
            address = 'Musterstrasse3, 34332 MusterLand3',
            iban = 'DE5689562365003333',
            user = simple_user
                 ),
        ServiceProvider.objects.create(
            company_name = 'Service Provider 4',
            phone = '+49444444444',
            registration_number = '56899-5655-584',
            address = 'Musterstrasse4, 34332 MusterLand4',
            iban = 'DE5689562365004444',
            user = simple_user
                 ),       
        
    ]

    return provider_list