import json
import pytest
from django.utils.translation import gettext_lazy as _


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

    def test_user_save_success_valid_data(self, api_client, roles):
        data = {
            'name': 'Test name',
            'email': 'example@mail.com',
            'password': 'password1A@',
            'role': 1
        }
        response = api_client.post(self.endpoint, data=data)
        assert len(json.loads(response.content).get('access')) > 0
        assert len(json.loads(response.content).get('refresh')) > 0

    def test_user_save_not_unique_email(self, api_client, staff_user):
        data = {
            'name': 'Test name',
            'email': staff_user.email,
            'password': 'password1A@',
            'role': 1
        }

        response = api_client.post(self.endpoint, data=data)
        assert response.status_code == 400

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
        assert response.status_code == 204

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

    @pytest.mark.parametrize('role_, length',
                             [('client', 4), ('cl', 4), ('ADMIN', 1), ('provider', 0), (' ', 5), ('nothing', 0)])
    def test_user_filter_by_role_success(self, staff_user, users_list, api_client, role_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?role={role_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_user_filter_by_created_at_year_exact_success(self, staff_user, users_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    def test_user_filter_by_created_at_year_exact_bad_request(self, staff_user, users_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 5), (2023, 5)])
    def test_user_filter_by_created_at_year_gt_success(self, staff_user, users_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_user_filter_by_created_at_year_gt_bad_request(self, staff_user, users_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 0)])
    def test_user_filter_by_created_at_year_lt_success(self, staff_user, users_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_user_filter_by_created_at_year_lt_bad_request(self, staff_user, users_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt=2023-10-20')
        assert response.status_code == 400

    def test_user_filter_by_created_at_bad_request(self, staff_user, users_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023')
        assert response.status_code == 400

    def test_user_filter_by_created_at_bad_success(self, staff_user, users_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023-10-10')
        assert response.status_code == 200

    @pytest.mark.parametrize(
        'email_, length',
        [
            ('admin@mail.com', 1),
            ('ADMIN@mail.com', 0),
            ('simple_user@mail.com', 1),
            ('simpLE_user@mail.com', 0),
            ('not_valid_mail', 0)
        ]
    )
    def test_user_filter_by_email_success(self, staff_user, users_list, api_client, email_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?email={email_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    @pytest.mark.parametrize('user_name, length', [('Example Name1', 1), ('Example', 3), (' ', 5)])
    def test_user_filter_by_name_icontains_success(self, staff_user, users_list, user_name, api_client, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name__icontains={user_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    @pytest.mark.parametrize('user_name, length', [('Example Name1', 1), ('Example', 0), (' ', 5)])
    def test_user_filter_by_name_exact_success(self, staff_user, users_list, user_name, api_client, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name={user_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    @pytest.mark.parametrize('is_active_, length', [('true', 4), (1, 4), (' ', 5), (0, 1), ('false', 1)])
    def test_user_filter_by_is_active_success(self, staff_user, users_list, is_active_, api_client, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?is_active={is_active_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_user_change_password_success(self, simple_user, api_client, raw_password):
        api_client.force_authenticate(simple_user)
        data = {
            'old_password': raw_password,
            'new_password': 'password'
        }
        response = api_client.post(f'{self.endpoint}change_password/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('message') == 'Password has been changed successfully'

    def test_user_change_password_with_unauthorized_user(self, api_client, raw_password):
        data = {
            'old_password': raw_password,
            'new_password': 'password'
        }
        response = api_client.post(f'{self.endpoint}change_password/', data=data, format='json')
        assert response.status_code == 401

    @pytest.mark.parametrize('new_password', ['', ' ', '1234', 'abc'])
    def test_user_change_password_with_wrong_data(self, simple_user, api_client, raw_password, new_password):
        api_client.force_authenticate(simple_user)
        data = {
            'old_password': raw_password,
            'new_password': new_password
        }
        response = api_client.post(f'{self.endpoint}change_password/', data=data, format='json')
        assert response.status_code == 400

    def test_user_reset_password(self, api_client, simple_user):
        data = {
            'email': simple_user.email,
            'redirect_link': 'https://example.com'
        }
        response = api_client.post(f'{self.endpoint}reset_password/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('message') == 'Email was send'

    def test_user_reset_password_with_non_existing_email(self, api_client, users_list):
        data = {
            'email': 'wrong@mail.com',
            'redirect_link': 'https://example.com'
        }
        response = api_client.post(f'{self.endpoint}reset_password/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.parametrize('link', [
        'httr://example.com',
        'http://example',
        'example',
        'example.com',
    ])
    def test_user_reset_password_with_wrong_link(self, api_client, simple_user, link):
        data = {
            'email': simple_user.email,
            'redirect_link': link
        }
        response = api_client.post(f'{self.endpoint}reset_password/', data=data, format='json')
        assert response.status_code == 400

    def test_user_reset_password_confirm_success(self, api_client, simple_user, confirmation_token):
        data = {
            'token': confirmation_token.confirmation_token,
            'password': 'newpassword'
        }
        response = api_client.post(f'{self.endpoint}reset_password_confirm/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('message') == _('Password has been reset successfully')

    def test_user_reset_password_confirm_wrong_token(self, api_client, simple_user, confirmation_token):
        data = {
            'token': 'jhdfghj4gh3jg576786gh',
            'password': 'newpassword'
        }
        response = api_client.post(f'{self.endpoint}reset_password_confirm/', data=data, format='json')
        assert response.status_code == 400

    def test_user_confirm_email_success(self, api_client, simple_user, confirmation_token):
        api_client.force_authenticate(simple_user)
        data = {
            'token': confirmation_token.confirmation_token
        }
        response = api_client.post(f'{self.endpoint}verify_email/', data=data, format='json')
        assert response.status_code == 200

    def test_user_confirm_email_wrong_token(self, api_client, simple_user, confirmation_token):
        api_client.force_authenticate(simple_user)
        data = {
            'token': 'wrong_token'
        }
        response = api_client.post(f'{self.endpoint}verify_email/', data=data, format='json')
        assert response.status_code == 400


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

    def test_role_save_already_existing(self, staff_user, api_client, roles):
        api_client.force_authenticate(staff_user)
        data = {
            "name": roles[0].name,
            "description": "new role description"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 400

    def test_role_get_list_with_staff_user_success(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_role_get_list_with_simple_user_forbidden(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_role_get_list_with_provider_user_forbidden(self, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_role_get_list_with_non_authenticated_unauthorized(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_role_retrieve_one_with_staff_user_status_success(self, staff_user, api_client, roles):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}{roles[0].id}/')
        assert response.status_code == 200

    def test_role_retrieve_one_with_provider_user_status_forbidden(self, provider_user, api_client, roles):
        api_client.force_authenticate(provider_user)
        response = api_client.get(f'{self.endpoint}{roles[0].id}/')
        assert response.status_code == 403

    def test_role_retrieve_one_with_simple_user_status_forbidden(self, simple_user, api_client, roles):
        api_client.force_authenticate(simple_user)
        response = api_client.get(f'{self.endpoint}{roles[0].id}/')
        assert response.status_code == 403

    def test_role_retrieve_one_with_unauthenticated_status_unauthorized(self, api_client, roles):
        response = api_client.get(f'{self.endpoint}{roles[0].id}/')
        assert response.status_code == 401

    @pytest.mark.parametrize("id", ["", " ", -1, "acd", 999999])
    def test_role_retrieve_with_wrong_id_not_found(self, staff_user, api_client, roles, id):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}{id}/')
        assert response.status_code == 404

    def test_role_update_with_staff_user_success(self, staff_user, api_client, roles):
        api_client.force_authenticate(staff_user)
        data = {
            "name": "new_name",
            "description": "test_description",
        }
        response = api_client.put(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 200
        assert json.loads(response.content).get("name") == data.get("name")

    def test_role_update_with_provider_user_forbidden(self, provider_user, api_client, roles):
        api_client.force_authenticate(provider_user)
        data = {
            "name": "new_name",
            "description": "",
        }
        response = api_client.put(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 403

    def test_role_update_with_simple_user_forbidden(self, simple_user, api_client, roles):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "new_name",
            "description": "",
        }
        response = api_client.put(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 403

    def test_role_update_with_unauthenticated_user_not_authorized(self, api_client, roles):
        data = {
            "name": "new_name",
            "description": "",
        }
        response = api_client.put(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 401

    def test_role_patch_with_staff_user_success(self, staff_user, api_client, roles):
        api_client.force_authenticate(staff_user)
        data = {
            "description": "test_description",
        }
        response = api_client.patch(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 200
        assert json.loads(response.content).get("name") == roles[0].name
        assert json.loads(response.content).get("description") == data.get("description")

    def test_role_patch_with_provider_user_forbidden(self, provider_user, api_client, roles):
        api_client.force_authenticate(provider_user)
        data = {
            "description": "test_description",
        }
        response = api_client.patch(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 403

    def test_role_patch_with_simple_user_forbidden(self, simple_user, api_client, roles):
        api_client.force_authenticate(simple_user)
        data = {
            "description": "test_description",
        }
        response = api_client.patch(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 403

    def test_role_patch_with_unauthenticated_user_not_authorized(self, api_client, roles):
        data = {
            "description": "test_description",
        }
        response = api_client.patch(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 401

    def test_role_delete_with_staff_user_success(self, staff_user, api_client, roles):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}{roles[0].id}/')

        assert response.status_code == 204  # no content = success

    def test_role_delete_with_provider_user_forbidden(self, provider_user, api_client, roles):
        api_client.force_authenticate(provider_user)
        data = {
            "description": "test_description",
        }
        response = api_client.delete(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 403

    def test_role_delete_with_simple_user_forbidden(self, simple_user, api_client, roles):
        api_client.force_authenticate(simple_user)
        data = {
            "description": "test_description",
        }
        response = api_client.delete(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 403

    def test_role_delete_with_unauthenticated_user_not_authorized(self, api_client, roles):
        data = {
            "description": "test_description",
        }
        response = api_client.delete(f'{self.endpoint}{roles[0].id}/', data=data, format="json")
        assert response.status_code == 401

    @pytest.mark.parametrize('role_name, length', [('admin', 1), ('client', 1), (' ', 3), ('provider', 1)])
    def test_role_filter_by_name_exact_success(self, staff_user, roles, users_list, role_name, api_client, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name={role_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    @pytest.mark.parametrize('role_name, length', [('ad', 1), ('clie', 1), (' ', 3), ('vider', 1)])
    def test_role_filter_by_name_icontains_success(self, staff_user, roles, role_name, api_client, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name__icontains={role_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
