import uuid
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from apps.core.utils import EmailSender
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
def email_sender():
    return EmailSender()


@pytest.fixture
def email_invoice_data():
    return {
        'email': 'testuser@example.com',
        'invoice_url': 'http://example.com/invoice',
    }


@pytest.fixture
def email_data():
    return {
        'name': 'Test User',
        'email': 'testuser@example.com',
        'policy_number': 'ABC123',
    }
