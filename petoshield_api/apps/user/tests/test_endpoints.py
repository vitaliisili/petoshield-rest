import json
import pytest


class TestUserEndpoints:
    endpoint = '/api/users/'

    def test_user_save_success(self, api_client, roles):
        data = {
            'name': 'Test name',
            'email': 'example@mail.com',
            'password': 'password1A@',
            'role': 1
        }
        response = api_client.post(self.endpoint, data=data)
        assert response.status_code == 201

    @pytest.mark.parametrize('name, email, password', [
        ('', 'example@mail.com', 'password1A@'),
        (' ', 'example@mail.com', 'password1A@'),
        ('Test name', '', 'password1A@'),
        ('Test name', ' ', 'password1A@'),
        ('Test name', 'example@mail.com', ''),
        ('Test name', 'example@mail.com', ' '),
    ])
    def test_user_save_with_blank_or_empty_data(self, roles, api_client, name, email, password):
        data = {
            'name': name,
            'email': email,
            'password': password,
        }
        response = api_client.post(self.endpoint, data=data)
        assert response.status_code == 400

    @pytest.mark.parametrize('name, email, password', [
        ('Test name', '@mail.com', 'password1A@'),
        ('Test name', 'A@b@c@example.com', 'password1A@'),
        ('Test name', 'just"not"right@example.com', 'password1A@'),
        ('Test name', '\still\"notallowed@example.com', 'password1A@'),  # noqa
        ('Test name', '"not\allowed@example.com', 'password1A@'),
        ('Test name', 'example@mail.com', 'pass'),
        ('Test name', 'example@mail.com', '1234'),
    ])
    def test_user_save_with_wrong_data(self, roles, api_client, name, email, password):
        data = {
            'name': name,
            'email': email,
            'password': password,
        }
        response = api_client.post(self.endpoint, data=data)
        assert response.status_code == 400

    def test_user_get_authenticated_user_account(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(f'{self.endpoint}me/')
        assert response.status_code == 200

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

    @pytest.mark.parametrize('name, length', [
        ('simple', 1),
        ('Example', 3),
        ('example', 3),
    ])
    def test_user_search_by_name(self, staff_user, api_client, users_list, name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?search={name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_user_ordering_by_name(self, staff_user, api_client, users_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?ordering=name')
        assert response.status_code == 200
        assert json.loads(response.content)[1].get('name') == 'Example Name1'

    @pytest.mark.parametrize('page, length', [
        (1, 2), (2, 2), (3, 1)
    ])
    def test_user_pagination_success(self, staff_user, users_list, api_client, page, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size=2')
        assert response.status_code == 200
        assert len(json.loads(response.content).get('results')) == length

    @pytest.mark.parametrize('page', [-1, 'one', 999999, '', ' '])
    def test_user_pagination_not_found(self, staff_user, users_list, api_client, page):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size=2')
        assert response.status_code == 404


class TestRoleEndpoints:
    endpoint = '/api/roles/'

    def test_role_save_with_staff_user_success(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        data = {
            "name": "new role",
            "description": "new role description"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201
        assert json.loads(response.content).get('name') == data.get('name')
    
    def test_role_save_with_simple_user_forbidden(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "new role",
            "description": "new role description"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 403
    
    def test_role_save_with_provider_user_forbidden(self, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        data = {
            "name": "new role",
            "description": "new role description"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 403

    def test_role_save_with_anonymous_user_unauthenticated(self, api_client):
        data = {
            "name": "new role",
            "description": "new role description"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 401
    
    @pytest.mark.parametrize('name', ['', ' '])
    def test_role_save_with_wrong_data_bad_request(self, staff_user, api_client, name):
        api_client.force_authenticate(staff_user)
        data = {
            "name": name,
            "description": "new role description"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 400
    
