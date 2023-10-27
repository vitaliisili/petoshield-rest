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
    
    def test_update_user_by_staff(self, staff_user, simple_user, api_client):
        api_client.force_authenticate(staff_user)

        updated_data = {   
            "email": "updated@email.com",
            "name": "updated name",
            "password": "updated password"
        }
        response = api_client.put(
            f"{self.endpoint}{simple_user.id}/", 
            updated_data,
            format="json"
        )
        assert response.status_code == 200

        response_data = json.loads(response.content)
        
        assert response_data.get("id") == simple_user.id
        assert response_data.get("email") == updated_data["email"]
        assert response_data.get("name") == updated_data["name"]
        # assert response_data.get("password") == updated_data["password"]
        
    def test_update_staff_user_by_simple_user(self, simple_user, staff_user, api_client):
        api_client.force_authenticate(simple_user)

        updated_data = {   
            "email": "updated@email.com",
            "name": "updated name",
            "password": "updated password"
        }
            
        response = api_client.put(
            f"{self.endpoint}{staff_user.id}/", 
            updated_data,
            format="json"
        )
            
        assert response.status_code == 403
    
    def test_update_user_by_himself(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)

        updated_data = {   
            "email": "updated@email.com",
            "name": "updated name",
            "password": "updated password"
        }
            
        response = api_client.put(
            f"{self.endpoint}{simple_user.id}/", 
            updated_data,
            format="json"
        )
        
        response_data = json.loads(response.content)
        
        assert response.status_code == 200
        assert response_data.get("id") == simple_user.id
        assert response_data.get("email") == updated_data["email"]
        assert response_data.get("name") == updated_data["name"]

    def test_delete_user_by_himself(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
            
        response = api_client.delete(
            f"{self.endpoint}{simple_user.id}/"
        )
        
        assert response.status_code == 403
    
    def test_delete_user_by_staff_user(self, simple_user, staff_user, api_client):
        api_client.force_authenticate(staff_user)
            
        response = api_client.delete(
            f"{self.endpoint}{simple_user.id}/"
        )
        
        assert response.status_code == 204
    
    def test_delete_user_by_unauthorized_user(self, simple_user, staff_user, api_client):
        # api_client.force_authenticate(staff_user)
            
        response = api_client.delete(
            f"{self.endpoint}{simple_user.id}/"
        )
        
        assert response.status_code == 401