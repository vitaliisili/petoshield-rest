import json


class TestBreedEndpoints:
    
    endpoint = '/api/pet-profile/breeds/'
    
    def test_breed_list_admin_access(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        
    def test_breed_list_user_access(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        
    def test_breed_list_with_unauthenticated_user(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401
        
    def test_patch_breed_with_simple_user(self,breed,simple_user,api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(
            f'{self.endpoint}{breed.id}/',
            {'min_age': 20}
            )
        assert response.status_code == 403

    def test_patch_breed_with_admin_user(self,breed,admin_user,api_client):
        api_client.force_authenticate(admin_user)
        response = api_client.patch(
            f'{self.endpoint}{breed.id}/',
            {'age_max': 20}
            )
        assert response.status_code == 200
        assert json.loads(response.content).get('age_max') == 20  
        
    def test_save_breed_with_simple_user(self,simple_user,api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.post(
            f'{self.endpoint}',
            { 
             "name":"Siameses cat1", 
             "age_min":9, 
             "age_max":11, 
             "risk_level":4,
             "species":"cat"
             }
            )
        assert response.status_code == 403
    
    def test_save_breed_with_admin_user(self,admin_user,api_client):
        api_client.force_authenticate(admin_user)
        response = api_client.post(
            f'{self.endpoint}',
            { 
             "name":"Siameses cat1", 
             "age_min":9, 
             "age_max":11, 
             "risk_level":4,
             "species":"cat"
             }
            )
        assert response.status_code == 201
        
    def test_put_breed_with_simple_user(self,breed,simple_user,api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.put(
            f'{self.endpoint}{breed.id}/',
                { 
                "name":"Siameses cat new", 
                "age_min":10, 
                "age_max":13, 
                "risk_level":4,
                "species":"cat"
                }
                )
        assert response.status_code == 403
        
    def test_put_breed_with_admin_user(self,breed,admin_user,api_client):
        api_client.force_authenticate(admin_user)
        response = api_client.put(
            f'{self.endpoint}{breed.id}/',
                { 
                "name":"Siameses cat new", 
                "age_min":10, 
                "age_max":13, 
                "risk_level":4,
                "species":"cat"
                }
                )
        assert response.status_code == 200
        
    def test_delete_breed_with_simple_user(self,breed,simple_user,api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f'{self.endpoint}{breed.id}/')
        assert response.status_code == 403
        
    def test_delete_breed_with_admin_user(self,breed,admin_user,api_client):
        api_client.force_authenticate(admin_user)
        response = api_client.delete(f'{self.endpoint}{breed.id}/')
        assert response.status_code == 204