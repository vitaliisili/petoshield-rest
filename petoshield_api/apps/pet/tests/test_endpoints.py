import json

import pytest


class TestBreedEndpoints:
    endpoint = '/api/pet-profile/breeds/'

    def test_breed_list_admin_access(self, staff_user, api_client, breeds_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert len(json.loads(response.content)) == len(breeds_list)
        assert response.status_code == 200

    def test_breed_list_user_access(self, simple_user, api_client, breeds_list):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert len(json.loads(response.content)) == len(breeds_list)
        assert response.status_code == 200

    def test_breed_list_with_unauthenticated_user(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_patch_breed_with_simple_user(self, breed, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{breed.id}/', {'min_age': 20})
        assert response.status_code == 403

    def test_patch_breed_with_admin_user(self, breed, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{breed.id}/', {'age_max': 20})
        assert response.status_code == 200
        assert json.loads(response.content).get('age_max') == 20

    def test_save_breed_with_simple_user(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.post(f'{self.endpoint}', {"name": "Siameses cat1",
                                                        "age_min": 9,
                                                        "age_max": 11,
                                                        "risk_level": 4,
                                                        "species": "cat"})
        assert response.status_code == 403

    def test_save_breed_with_admin_user(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.post(f'{self.endpoint}', {"name": "Siameses cat1",
                                                        "age_min": 9,
                                                        "age_max": 11,
                                                        "risk_level": 4,
                                                        "species": "cat"})
        assert response.status_code == 201

    def test_save_breed_with_unauthenticated_user(self, api_client):
        response = api_client.post(f'{self.endpoint}', {"name": "Siameses cat1",
                                                        "age_min": 9,
                                                        "age_max": 11,
                                                        "risk_level": 4,
                                                        "species": "cat"})
        assert response.status_code == 401

    @pytest.mark.parametrize('name, age_min, age_max, risk_level, species', [
        (' ', 1, 10, 4, 'cat'),
        ('test breed', ' ', 10, 4, 'cat'),
        ('test breed', 1, ' ', 4, 'cat'),
        ('test breed', 1, 10, ' ', 'cat'),
        ('test breed', 1, 10, 4, ' '),
    ])
    def test_save_breed_with_blank_or_empty_data(self, staff_user, api_client, name, age_min, age_max, risk_level,
                                                 species):
        api_client.force_authenticate(staff_user)
        response = api_client.post(f'{self.endpoint}', {"name": name,
                                                        "age_min": age_min,
                                                        "age_max": age_max,
                                                        "risk_level": risk_level,
                                                        "species": species
                                                        })
        assert response.status_code == 400

    @pytest.mark.parametrize('name, age_min, age_max, risk_level, species', [
        ('test breed', -1, 10, 4, 'cat'),
        ('test breed', 'not_number', 10, 4, 'cat'),
        ('test breed', 1.01, 10, 4, 'cat'),
        ('test breed', 1, -10, 4, 'cat'),
        ('test breed', 1, 'not_number', 4, 'cat'),
        ('test breed', 1, 1.01, 4, 'cat'),
        ('test breed', 1, 31, 4, 'cat'),
        ('test breed', 32, 31, 4, 'cat'),
        ('test breed', 1, 10, -1, 'cat'),
        ('test breed', 1, 10, 0, 'cat'),
        ('test breed', 1, 10, 11, 'cat'),
        ('test breed', 1, 10, 'not_number', 'cat'),
        ('test breed', 1, 10, 1.01, 'cat'),
        ('test breed', 1, 10, 4, 'Cat'),
        ('test breed', 1, 10, 4, 'bird'),
        ('test breed', 1, 10, 4, 1),
    ])
    def test_save_breed_with_wrong_data(self, staff_user, api_client, name, age_min, age_max, risk_level,
                                        species):
        api_client.force_authenticate(staff_user)
        response = api_client.post(f'{self.endpoint}', {"name": name,
                                                        "age_min": age_min,
                                                        "age_max": age_max,
                                                        "risk_level": risk_level,
                                                        "species": species
                                                        })
        assert response.status_code == 400

    def test_put_breed_with_simple_user(self, breed, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.put(f'{self.endpoint}{breed.id}/', {"name": "Siameses cat new",
                                                                  "age_min": 10,
                                                                  "age_max": 13,
                                                                  "risk_level": 4,
                                                                  "species": "cat"})
        assert response.status_code == 403

    def test_put_breed_with_admin_user(self, breed, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.put(f'{self.endpoint}{breed.id}/', {"name": "Siameses cat new",
                                                                  "age_min": 10,
                                                                  "age_max": 13,
                                                                  "risk_level": 4,
                                                                  "species": "cat"})
        assert response.status_code == 200

    def test_put_breed_with_unauthenticated_user(self, breed, api_client):
        response = api_client.put(f'{self.endpoint}{breed.id}/', {"name": "Siameses cat new",
                                                                  "age_min": 10,
                                                                  "age_max": 13,
                                                                  "risk_level": 4,
                                                                  "species": "cat"})
        assert response.status_code == 401

    def test_put_breed_not_found(self, breed, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.put(f'{self.endpoint}999999/', {"name": "Siameses cat new",
                                                              "age_min": 10,
                                                              "age_max": 13,
                                                              "risk_level": 4,
                                                              "species": "cat"})
        assert response.status_code == 404

    def test_delete_breed_with_simple_user(self, breed, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f'{self.endpoint}{breed.id}/')
        assert response.status_code == 403

    def test_delete_breed_with_admin_user(self, breed, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}{breed.id}/')
        assert response.status_code == 204

    def test_delete_breed_with_unauthenticated_user(self, breed, api_client):
        response = api_client.delete(f'{self.endpoint}{breed.id}/')
        assert response.status_code == 401

    def test_delete_breed_not_found(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}999999/')
        assert response.status_code == 404


class TestPetsEndpoints:
    endpoint = '/api/pet-profile/pets/'

    def test_pets_list_with_admin_success(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert len(json.loads(response.content)) == len(pets_list)
        assert response.status_code == 200

    def test_pets_list_with_unauthorized_user(self, simple_user, pets_list, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_pets_list_with_unauthenticated_user(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    # def test_get_user_pet_by_id_with_staff_permission(self, staff_user, pet_created_by_user, api_client):
    #     api_client.force_authenticate(staff_user)
    #     response = api_client.get(f'{self.endpoint}{pet_created_by_user.id}/')
    #     assert response.status_code == 200
    #     assert json.loads(response.content).get('user') == pet_created_by_user.user.id
    #
    # def test_get_admin_pet_by_id_with_simple_user_not_allowed(self, simple_user, pet_created_by_admin, api_client):
    #     api_client.force_authenticate(simple_user)
    #     response = api_client.get(f'{self.endpoint}{pet_created_by_admin.id}/')
    #     assert response.status_code == 403
    #
    # def test_put_user_pet_with_staff_permissions(self, staff_user, breed, simple_user, pet_created_by_user, api_client):
    #     api_client.force_authenticate(staff_user)
    #     response = api_client.put(f'{self.endpoint}{pet_created_by_user.id}/',
    #                               {
    #                                   "name": "Simple User dog1",
    #                                   "age": 6,
    #                                   "gender": 'M',
    #                                   "species": 'dog',
    #                                   "breed": breed.id,
    #                                   "user": simple_user.id
    #                               }
    #                               )
    #     assert response.status_code == 200
    #     assert json.loads(response.content).get('name') == "Simple User dog1"
    #     assert json.loads(response.content).get('age') == 6
    #
    # def test_put_admin_pet_with_user_not_allowed(self, staff_user, breed, simple_user, pet_created_by_admin,
    #                                              api_client):
    #     api_client.force_authenticate(simple_user)
    #     response = api_client.put(f'{self.endpoint}{pet_created_by_admin.id}/',
    #                               {
    #                                   "name": "Admin Doggy dog1",
    #                                   "age": 6,
    #                                   "gender": 'M',
    #                                   "species": 'dog',
    #                                   "breed": breed.id,
    #                                   "user": staff_user.id
    #                               }
    #                               )
    #     assert response.status_code == 403
    #
    # def test_patch_user_pet_with_staff_permissions(self, staff_user, pet_created_by_user, api_client):
    #     api_client.force_authenticate(staff_user)
    #     response = api_client.patch(f'{self.endpoint}{pet_created_by_user.id}/',
    #                                 {
    #                                     "name": "Simple User dog1",
    #                                 }
    #                                 )
    #     assert response.status_code == 200
    #     assert json.loads(response.content).get('name') == "Simple User dog1"
    #
    # def test_patch_admin_pet_with_user_not_allowed(self, simple_user, pet_created_by_admin, api_client):
    #     api_client.force_authenticate(simple_user)
    #     response = api_client.patch(f'{self.endpoint}{pet_created_by_admin.id}/',
    #                                 {
    #                                     "name": "Admin Doggy dog1",
    #                                 }
    #                                 )
    #     assert response.status_code == 403
    #
    # def test_delete_user_pet_with_staff_permissions(self, staff_user, pet_created_by_user, api_client):
    #     api_client.force_authenticate(staff_user)
    #     response = api_client.delete(f'{self.endpoint}{pet_created_by_user.id}/')
    #     assert response.status_code == 204
    #
    # def test_delete_admin_pet_with_user_not_allowed(self, simple_user, pet_created_by_admin, api_client):
    #     api_client.force_authenticate(simple_user)
    #     response = api_client.delete(f'{self.endpoint}{pet_created_by_admin.id}/')
    #     assert response.status_code == 403
