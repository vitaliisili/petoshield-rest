import json
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

    def test_patch_user_with_staff_permission(self, staff_user, simple_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{simple_user.id}/', {"name": "Test Name"})
        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'Test Name'

    def test_patch_user_with_simple_user_not_allowed(self, staff_user, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{staff_user.id}/', {'name': 'Test fail'})
        assert response.status_code == 403

    def test_patch_user_his_self(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{simple_user.id}/', {'name': 'Test Name'})
        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'Test Name'