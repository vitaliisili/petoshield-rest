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
def service_provider(provider_user):
    provider = ServiceProvider.objects.create(
        company_name='Service Provider 1',
        phone='+49856547725',
        registration_number='56899-5655-581',
        address='Musterstrasse3, 34332 MusterLand',
        iban='DE5689562365002354',
        user=provider_user
    )
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


@pytest.fixture
def users_list(roles):
    users_list = [
        get_user_model().objects.create_user(email='example1@mail.com',
                                             password='password1A@',
                                             name='Example Name1',
                                             role=roles[2]),

        get_user_model().objects.create_user(email='example2@mail.com',
                                             password='password1A@',
                                             name='Example Name2',
                                             role=roles[2]),

        get_user_model().objects.create_user(email='example3@mail.com',
                                             password='password1A@',
                                             name='Example Name3',
                                             role=roles[2]),
    ]
    return users_list


@pytest.fixture
def service_provider_list(service_provider, users_list):
    provider_list = [
        service_provider,
        ServiceProvider.objects.create(
            company_name='Service Provider 2',
            phone='+492222222222',
            registration_number='56899-5655-582',
            address='Musterstrasse2, 34332 MusterLand2',
            iban='DE5689562365002222',
            user=users_list[0]
        ),
        ServiceProvider.objects.create(
            company_name='Service Provider 3',
            phone='+493333333333',
            registration_number='56899-5655-583',
            address='Musterstrasse3, 34332 MusterLand3',
            iban='DE5689562365003333',
            user=users_list[1]
        ),
        ServiceProvider.objects.create(
            company_name='Service Provider 4',
            phone='+49444444444',
            registration_number='56899-5655-584',
            address='Musterstrasse4, 34332 MusterLand4',
            iban='DE5689562365004444',
            user=users_list[2]
        ),

    ]
    return provider_list


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
def policies_list(policy, pets_list):
    list = [
        policy,
        Policy.objects.create(
            policy_number='22-222-4860',
            start_date='2023-11-02',
            end_date='2024-11-02',
            status='valid',
            price=17.25,
            initial_limit=100000,
            current_limit=100000,
            deductible=500,
            pet=pets_list[0]
        ),
        Policy.objects.create(
            policy_number='33-333-4860',
            start_date='2022-11-01',
            end_date='2023-11-01',
            status='expired',
            price=11.99,
            initial_limit=100000,
            current_limit=100000,
            deductible=2000,
            pet=pets_list[1]
        ),
        Policy.objects.create(
            policy_number='44-444-4860',
            start_date='2023-09-03',
            end_date='2024-09-03',
            status='valid',
            price=15.89,
            initial_limit=100000,
            current_limit=100000,
            deductible=300,
            pet=pets_list[2]
        )
    ]
    return list


@pytest.fixture
def insurance_case(policy, service_provider):
    insurance_case_ex = InsuranceCase.objects.create(
        claim_date='2023-11-03',
        description='Accident happened',
        status='accept',
        policy=policy,
        service_provider=service_provider
    )
    return insurance_case_ex


@pytest.fixture
def insurance_cases_list(insurance_case, policies_list, service_provider_list):
    insurance_cases_list_ex = [
        insurance_case,
        InsuranceCase.objects.create(
            claim_date='2023-11-03',
            description='Accident happened',
            status='process',
            policy=policies_list[1],
            service_provider=service_provider_list[1]
        ),
        InsuranceCase.objects.create(
            claim_date='2023-10-29',
            description='Accident happened',
            status='reject',
            policy=policies_list[2],
            service_provider=service_provider_list[2]
        ),
        InsuranceCase.objects.create(
            claim_date='2023-11-05',
            description='Accident happened',
            status='accept',
            policy=policies_list[3],
            service_provider=service_provider_list[3]
        )
    ]
    return insurance_cases_list_ex


@pytest.fixture
def incoming_invoice(insurance_case):
    incoming_invoice_ex = IncomingInvoice.objects.create(
        invoice_date='2023-11-03',
        amount=125.39,
        insurance_case=insurance_case
    )
    return incoming_invoice_ex


@pytest.fixture
def incoming_invoices_list(incoming_invoice, insurance_cases_list):
    incoming_invoices_list_ex = [
        incoming_invoice,
        IncomingInvoice.objects.create(
            invoice_date='2023-11-06',
            amount=750.50,
            insurance_case=insurance_cases_list[3]
        ),
    ]
    return incoming_invoices_list_ex
