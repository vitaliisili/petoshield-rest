import json

import pytest
from django.conf import settings


class TestStripeEndpoints:
    endpoint = '/api/payment/'

    def test_payment_get_public_key_success(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(f'{self.endpoint}public_key/')
        assert response.status_code == 200
        assert json.loads(response.content).get('key') == settings.STRIPE_PUBLIC_KEY

    @pytest.mark.django_db
    def test_payment_get_public_key_with_anonymous_user_unauthorized(self, api_client):
        response = api_client.get(f'{self.endpoint}public_key/')
        assert response.status_code == 401
