import uuid

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.user.models import Role, MailVerificationTokens


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
def confirmation_token(simple_user):
    token = uuid.uuid4()
    mail_verification_token = MailVerificationTokens.objects.create(user=simple_user, confirmation_token=token)
    return mail_verification_token


@pytest.fixture
def provider_user(roles, raw_password):
    provider = get_user_model().objects.create_user(email='provider@mail.com',
                                                    password=raw_password,
                                                    name='Provider User',
                                                    role=roles[2])
    return provider


@pytest.fixture
def users_list(roles, staff_user, simple_user, raw_password):
    users_list = [
        staff_user,
        simple_user,
        get_user_model().objects.create_user(email='example1@mail.com',
                                             password=raw_password,
                                             name='Example Name1',
                                             is_active=False,
                                             role=roles[0]),

        get_user_model().objects.create_user(email='example2@mail.com',
                                             password=raw_password,
                                             name='Example Name2',
                                             role=roles[0]),

        get_user_model().objects.create_user(email='example3@mail.com',
                                             password=raw_password,
                                             name='Example Name3',
                                             role=roles[0]),
    ]
    return users_list
