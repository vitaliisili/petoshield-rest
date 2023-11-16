from apps.tickets.models import Ticket
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
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
def provider_user(roles, raw_password):
    provider = get_user_model().objects.create_user(email='provider@mail.com',
                                                    password=raw_password,
                                                    name='Provider User',
                                                    role=roles[2])
    return provider


@pytest.fixture
def ticket(db):
    simple_ticket = Ticket.objects.create(visitor_email='example@mail.com',
                                          visitor_name='example',
                                          visitor_message='example message')
    return simple_ticket


@pytest.fixture
def ticket_list(db):
    return [
        Ticket.objects.create(visitor_email='amanda@mail.com',
                              visitor_name='Amanda',
                              visitor_message='Hello Amanda'),

        Ticket.objects.create(visitor_email='genevieve@mail.com',
                              visitor_name='Genevieve',
                              visitor_message='The message is love'),

        Ticket.objects.create(visitor_email='Eolie@mail.com',
                              visitor_name='Eolie',
                              visitor_message='Welcome Eolie'),

        Ticket.objects.create(visitor_email='Matilda@mail.com',
                              visitor_name='Matilda',
                              visitor_message='Welcome Matilda',
                              ticket_status='close'),

        Ticket.objects.create(visitor_email='Thorsten@mail.com',
                              visitor_name='Thorsten',
                              visitor_message='Welcome Thorsten',
                              ticket_status='open'),
    ]
