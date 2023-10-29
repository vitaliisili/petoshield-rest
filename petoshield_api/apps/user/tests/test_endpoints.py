import json
import pytest


class TestUserEndpoints:
    endpoint = '/api/users/'

    def test_user_list_with_staff_success(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_user_list_with_unauthorized_user(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_user_list_with_unauthenticated_user(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_user_patch_with_staff_permission(self, staff_user, simple_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{simple_user.id}/', {"name": "Test Name"})
        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'Test Name'

    def test_user_patch_with_simple_user_not_allowed(self, staff_user, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{staff_user.id}/', {'name': 'Test fail'})
        assert response.status_code == 403

    def test_user_patch_his_self(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{simple_user.id}/', {'name': 'Test Name'})
        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'Test Name'

    @pytest.mark.parametrize('name', ['', ' ', '   '])
    def test_user_patch_with_empty_name_or_blank(self, simple_user, api_client, name):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{simple_user.id}/', {'name': name})
        assert response.status_code == 400

    @pytest.mark.parametrize('email', ['', ' ', '   '])
    def test_user_patch_with_empty_email_or_blank(self, simple_user, api_client, email):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{simple_user.id}/', {'email': email})
        assert response.status_code == 400

    @pytest.mark.parametrize('email', [
        '@mail.com',
        'A@b@c@example.com',
        'just"not"right@example.com',
        '\still\"notallowed@example.com',
        '"not\allowed@example.com'
    ])
    def test_user_patch_with_wrong_email(self, simple_user, api_client, email):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{simple_user.id}/', {'email': email})
        assert response.status_code == 400

    def test_user_patch_not_found(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}999999/', {'name': 'Test Name'})
        assert response.status_code == 404

    def test_user_update_by_staff(self, staff_user, simple_user, api_client):
        api_client.force_authenticate(staff_user)

        updated_data = {
            "email": "updated@email.com",
            "name": "updated name",
            "password": "testpassword1A@"
        }
        response = api_client.put(f"{self.endpoint}{simple_user.id}/", updated_data)
        response_data = json.loads(response.content)
        assert response.status_code == 200
        assert response_data.get("email") == updated_data["email"]
        assert response_data.get("name") == updated_data["name"]

    def test_user_update_by_unauthorized_user(self, simple_user, staff_user, api_client):
        api_client.force_authenticate(simple_user)

        updated_data = {
            "email": "updated@email.com",
            "name": "updated name",
        }
        response = api_client.put(f'{self.endpoint}{staff_user.id}/', updated_data)
        assert response.status_code == 403

    def test_user_update_by_himself(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)

        updated_data = {
            "email": "updated@email.com",
            "name": "updated name",
        }
        response = api_client.put(f"{self.endpoint}{simple_user.id}/", updated_data)
        response_data = json.loads(response.content)
        assert response.status_code == 200
        assert response_data.get("email") == updated_data["email"]
        assert response_data.get("name") == updated_data["name"]

    def test_user_update_by_unauthenticated_user(self, simple_user, api_client):
        updated_data = {
            "email": "updated@email.com",
            "name": "updated name",
        }
        response = api_client.put(f"{self.endpoint}{simple_user.id}/", updated_data)
        assert response.status_code == 401

    def test_user_update_not_found(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.put(f'{self.endpoint}999999/', {"name": "Test Name"})
        assert response.status_code == 404

    def test_user_delete_by_himself(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f"{self.endpoint}{simple_user.id}/")
        assert response.status_code == 403

    def test_user_delete_by_staff_user(self, simple_user, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f"{self.endpoint}{simple_user.id}/")
        assert response.status_code == 204

    def test_user_delete_by_unauthorized_user(self, simple_user, staff_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f"{self.endpoint}{staff_user.id}/")
        assert response.status_code == 403

    def test_user_delete_by_unauthenticated_user(self, simple_user, api_client):
        response = api_client.delete(f"{self.endpoint}{simple_user.id}/")
        assert response.status_code == 401

    def test_user_delete_not_found(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f"{self.endpoint}999999/")
        assert response.status_code == 404

    @pytest.mark.parametrize('wrong_id', ['abc', 'id=1'])
    def test_user_delete_with_wrong_id(self, staff_user, api_client, users_list, wrong_id):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f"{self.endpoint}{wrong_id}/")
        assert response.status_code == 404
