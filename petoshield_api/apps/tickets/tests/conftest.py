from apps.tickets.models import Ticket, JobTicket, PartnerTicket
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


@pytest.fixture
def job_ticket(db):
    simple_job_ticket = JobTicket.objects.create(position='test position name',
                                                 first_name='test-name',
                                                 last_name='test-last',
                                                 email='example@mail.com')
    return simple_job_ticket


@pytest.fixture
def job_ticket_list(db):
    return [
        JobTicket.objects.create(position='insurance manager',
                                 first_name='Moralez',
                                 last_name='Korlm',
                                 email='example1@mail.com'),

        JobTicket.objects.create(position='backend developer',
                                 first_name='Sara',
                                 last_name='Poter',
                                 email='example2@mail.com'),

        JobTicket.objects.create(position='frontend developer',
                                 first_name='Lara',
                                 last_name='Miko',
                                 email='example3@mail.com'),
    ]


@pytest.fixture
def partner_ticket(db):
    simple_partner_ticket = PartnerTicket.objects.create(name='Test Name',
                                                         business_name='test business name',
                                                         email='example@mail.com',
                                                         message='test message text',
                                                         url='https://example.com')
    return simple_partner_ticket


@pytest.fixture
def partner_ticket_list(db):
    return [
        PartnerTicket.objects.create(name='Lina Morex',
                                     business_name='lina morex gbh Company',
                                     email='example1@mail.com',
                                     message='lina text message',
                                     url='https://example1.com'),

        PartnerTicket.objects.create(name='Mike Nurner',
                                     business_name='Mike Company gbh',
                                     email='example2@mail.com',
                                     message='mike message text',
                                     url='https://example2.com'),

        PartnerTicket.objects.create(name='Sira',
                                     business_name='Sira sisters gbh',
                                     email='example3@mail.com',
                                     message='sira message text',
                                     url='https://example3.com')
    ]
