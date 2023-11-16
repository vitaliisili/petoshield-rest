import json
import pytest  # noqa


class TestBreedEndpoints:
    endpoint = '/api/pet-profile/breeds/'

    def test_breed_list_admin_access_success(self, staff_user, api_client, breeds_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert len(json.loads(response.content)) == len(breeds_list)
        assert response.status_code == 200

    def test_breed_list_user_access(self, simple_user, api_client, breeds_list):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert len(json.loads(response.content)) == len(breeds_list)
        assert response.status_code == 200

    def test_breed_list_with_unauthenticated_user_success(self, api_client, breeds_list):
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(breeds_list)

    def test_patch_breed_with_simple_user_forbidden(self, breed, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{breed.id}/', {'min_age': 20})
        assert response.status_code == 403

    def test_patch_breed_with_admin_user_success(self, breed, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{breed.id}/', {'age_max': 20})
        assert response.status_code == 200
        assert json.loads(response.content).get('age_max') == 20

    def test_patch_breed_not_found(self, breed, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}999999/', {'age_max': 20})
        assert response.status_code == 404

    def test_patch_breed_with_provider_user_permission_denied(self, breed, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.patch(f'{self.endpoint}{breed.id}/', {'min_age': 2})
        assert response.status_code == 403

    def test_save_breed_with_simple_user_forbidden(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.post(f'{self.endpoint}', {"name": "Siameses cat1",
                                                        "age_min": 9,
                                                        "age_max": 11,
                                                        "risk_level": 4,
                                                        "species": "cat"})
        assert response.status_code == 403

    def test_save_breed_with_admin_user_success(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.post(f'{self.endpoint}', {"name": "Siameses cat1",
                                                        "age_min": 9,
                                                        "age_max": 11,
                                                        "risk_level": 4,
                                                        "species": "cat"})
        assert response.status_code == 201

    def test_save_breed_with_unauthenticated_user_permission_denied(self, api_client):
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

    def test_save_breed_with_provider_user_permission_denied(self, breed, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.post(f'{self.endpoint}', {"name": "Test name",
                                                        "age_min": 2,
                                                        "age_max": 10,
                                                        "risk_level": 5,
                                                        "species": 'cat'
                                                        })
        assert response.status_code == 403

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

    def test_put_breed_with_provider_user_permission_denied(self, breed, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.put(f'{self.endpoint}{breed.id}/', {"name": "Siameses cat new",
                                                                  "age_min": 10,
                                                                  "age_max": 13,
                                                                  "risk_level": 4,
                                                                  "species": "cat"})
        assert response.status_code == 403

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

    def test_delete_breed_with_provider_user_permission_denied(self, provider_user, breed, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.delete(f'{self.endpoint}{breed.id}/')
        assert response.status_code == 403

    @pytest.mark.parametrize('name, length', [('Arenol', 1), ('arenol', 1), ('ol', 2)])
    def test_breed_search_by_name(self, staff_user, api_client, breeds_list, name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?search={name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_breed_ordering_by_name(self, staff_user, api_client, breeds_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?ordering=name')
        assert response.status_code == 200
        assert json.loads(response.content)[0].get('name') == 'Arenol'

    @pytest.mark.parametrize('page, length', [
        (1, 2), (2, 1)
    ])
    def test_breed_pagination_success(self, staff_user, breeds_list, api_client, page, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size=2')
        assert response.status_code == 200
        assert len(json.loads(response.content).get('results')) == length

    @pytest.mark.parametrize('page', [-1, 'one', 999999, '', ' '])
    def test_breed_pagination_not_found(self, staff_user, breeds_list, api_client, page):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size=2')
        assert response.status_code == 404

    @pytest.mark.parametrize('name, length', [('Arenol', 1), ('arenol', 0), ('reno', 0), (" ", 3), (12, 0)])
    def test_breed_filter_by_name__exact_success(self, staff_user, breeds_list, api_client, name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name={name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    @pytest.mark.parametrize('name, length', [('Arenol', 1), ('arenol', 1), ('reno', 1), (" ", 3), (12, 0)])
    def test_breed_filter_by_name__icontains_success(self, staff_user, breeds_list, api_client, name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name__icontains={name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_breed_filter_by_age_min_exact_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_min={9}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_breed_filter_by_age_min_exact_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_min=nine')
        assert response.status_code == 400

    def test_breed_filter_by_age_min_gt_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_min__gt={9}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_breed_filter_by_age_min_gt_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_min__gt=nine')
        assert response.status_code == 400

    def test_breed_filter_by_age_min_lt_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_min__lt={10}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_breed_filter_by_age_min_lt_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_min__lt=ten')
        assert response.status_code == 400

    def test_breed_filter_by_age_max_exact_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_max={13}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_breed_filter_by_age_max_exact_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_max=ten')
        assert response.status_code == 400

    def test_breed_filter_by_age_max_gt_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_max__gt={11}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_breed_filter_by_age_max_gt_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_max__gt=eleven')
        assert response.status_code == 400

    def test_breed_filter_by_age_max_lt_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_max__lt={13}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_breed_filter_by_age_max_lt_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age_max__lt=thirteen')
        assert response.status_code == 400

    def test_breed_filter_by_risk_level_exact_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?risk_level={4}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_breed_filter_by_risk_level_exact_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?risk_level=four')
        assert response.status_code == 400

    def test_breed_filter_by_risk_level_gt_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?risk_level__gt={4}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_breed_filter_by_risk_level_gt_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?risk_level__gt=four')
        assert response.status_code == 400

    def test_breed_filter_by_risk_level_lt_success(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?risk_level__lt={6}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_breed_filter_by_risk_level_lt_bad_request(self, staff_user, breeds_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?risk_level__lt=six')
        assert response.status_code == 400

    @pytest.mark.parametrize('species, length', [('cat', 2), ('CAT', 2), ('c', 2), (' ', 3), (1, 0)])
    def test_breed_filter_by_species_success(self, staff_user, breeds_list, api_client, species, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?species__icontains={species}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length


class TestPetsEndpoints:
    endpoint = '/api/pet-profile/pets/'

    def test_pets_save_success(self, simple_user, api_client, breed):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "new pet",
            "age": 2,
            "gender": "F",
            "species": "cat",
            "breed": breed.id,
            "user": simple_user.id
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    def test_pets_save_with_id_not_owned_success(self, simple_user, api_client, staff_user, breed):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "new pet",
            "age": 2,
            "gender": "F",
            "species": "cat",
            "breed": breed.id,
            "user": staff_user.id
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    @pytest.mark.parametrize('breed_id, user_id', [
        ('string', 2),
        (1, 'string'),
        (-1, 2),
        (1, -2),
        (1.1, 2),
        (1, 2.1),
        (1, ''),
        ('', 1),
    ])
    def test_pets_save_with_wrong_id_bad_request(self, simple_user, api_client, breed_id, user_id):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "new pet",
            "age": 2,
            "gender": "F",
            "species": "cat",
            "breed": breed_id,
            "user": user_id
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.parametrize('name, age, gender, species', [
        ('', 2, 'F', 'cat'),
        (' ', 2, 'F', 'cat'),
        ('Test Name', -1, 'F', 'cat'),
        ('Test Name', 1.1, 'F', 'cat'),
        ('Test Name', 200, 'F', 'cat'),
        ('Test Name', 2, 1, 'cat'),
        ('Test Name', 2, 'S', 'cat'),
        ('Test Name', 2, 'Female', 'cat'),
        ('Test Name', '', 'F', 'cat'),
        ('Test Name', ' ', 'F', 'cat'),
        ('Test Name', 2, '', 'cat'),
        ('Test Name', 2, ' ', 'cat'),
        ('Test Name', 2, 'F', 'Cat'),
        ('Test Name', 2, 'F', ''),
        ('Test Name', 2, 'F', ' '),
        ('Test Name', 2, 'F', 'Dog'),
        ('Test Name', 2, 'F', 1),
    ])
    def test_pets_save_with_wrong_data_bad_request(self, simple_user, api_client, breed, name, age, gender, species):
        api_client.force_authenticate(simple_user)
        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "species": species,
            "breed": breed.id,
            "user": simple_user.id
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 400

    def test_save_with_provider_permission_denied(self, provider_user, api_client, breed):
        api_client.force_authenticate(provider_user)
        data = {
            "name": "new pet",
            "age": 2,
            "gender": "F",
            "species": "cat",
            "breed": breed.id,
            "user": provider_user.id
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 403

    def test_pets_create_new_account_success(self, api_client, breed, roles):
        data = {
            "pet": {
                "name": "new pet",
                "age": 2,
                "gender": "F",
                "species": "cat",
                "breed": breed.id
            },
            "user": {
                "email": "example@mail.com",
                "name": "Ria Dormen",
                "password": "password1A@"
            }
        }
        response = api_client.post(f'{self.endpoint}create_new_account/', data=data, format='json')
        assert response.status_code == 201
        assert len(json.loads(response.content).get('access')) > 0

    def test_pets_list_with_admin_success(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert len(json.loads(response.content)) == len(pets_list)
        assert response.status_code == 200

    def test_pets_list_with_simple_user_user(self, simple_user, pets_list, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(list(filter(lambda p: p.user == simple_user, pets_list)))

    def test_pets_list_with_unauthenticated_user(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_pets_list_with_provider_user_permission_denied(self, provider_user, pets_list, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_pets_get_by_id_with_staff_user_success(self, staff_user, pet, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}{pet.id}/')
        assert response.status_code == 200
        assert json.loads(response.content).get('name') == pet.name

    def test_pets_get_by_id_with_simple_user_success(self, simple_user, pet, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(f'{self.endpoint}{pet.id}/')
        assert response.status_code == 200
        assert json.loads(response.content).get('name') == pet.name

    def test_pets_get_by_id_with_simple_user_not_found(self, simple_user, pets_list, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(f'{self.endpoint}{pets_list[2].id}/')
        assert response.status_code == 404

    def test_pets_get_by_id_with_unauthenticated_user_permission_denied(self, pet, api_client):
        response = api_client.get(f'{self.endpoint}{pet.id}/')
        assert response.status_code == 401

    def test_pets_get_by_id_with_provider_user_permission_denied(self, provider_user, pet, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.get(f'{self.endpoint}{pet.id}/')
        assert response.status_code == 403

    @pytest.mark.parametrize('id', [-1, 'one', '1.1', '', ' '])
    def test_pets_get_by_id_with_wrong_id_bad_request(self, staff_user, api_client, pet, id):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}{id}/')
        assert response.status_code == 404

    def test_pets_by_id_check_data_success(self, staff_user, api_client, pet):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}{pet.id}/')
        assert json.loads(response.content).get('name') == pet.name
        assert json.loads(response.content).get('age') == pet.age
        assert json.loads(response.content).get('gender') == pet.gender
        assert json.loads(response.content).get('species') == pet.species
        assert json.loads(response.content).get('breed') == pet.breed.name
        assert json.loads(response.content).get('user') == pet.user.id

    def test_pets_put_with_staff_user_success(self, staff_user, api_client, pet, breed):
        api_client.force_authenticate(staff_user)
        data = {
            "name": "New Name",
            "age": 3,
            "gender": "M",
            "species": "dog",
            "breed": breed.id,
            "user": staff_user.id
        }
        response = api_client.put(f'{self.endpoint}{pet.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_pets_put_with_simple_user_success(self, simple_user, api_client, pet, breed):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "New Name",
            "age": 3,
            "gender": "M",
            "species": "dog",
            "breed": breed.id,
            "user": simple_user.id
        }
        response = api_client.put(f'{self.endpoint}{pet.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_pets_put_with_provider_user_permission_denied(self, provider_user, api_client, pet, breed):
        api_client.force_authenticate(provider_user)
        data = {
            "name": "New Name",
            "age": 3,
            "gender": "M",
            "species": "dog",
            "breed": breed.id,
            "user": provider_user.id
        }
        response = api_client.put(f'{self.endpoint}{pet.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_pets_put_with_simple_user_for_not_owned_success(self, simple_user, staff_user, pet, api_client, breed):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "New Name",
            "age": 3,
            "gender": "M",
            "species": "dog",
            "breed": breed.id,
            "user": staff_user.id
        }
        response = api_client.put(f'{self.endpoint}{pet.id}/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('user') == simple_user.id

    @pytest.mark.parametrize('name, age, gender, species', [
        ('', 2, 'F', 'cat'),
        (' ', 2, 'F', 'cat'),
        ('Test Name', -1, 'F', 'cat'),
        ('Test Name', 1.1, 'F', 'cat'),
        ('Test Name', 100, 'F', 'cat'),
        ('Test Name', 2, 1, 'cat'),
        ('Test Name', 2, 'S', 'cat'),
        ('Test Name', 2, 'Female', 'cat'),
        ('Test Name', '', 'F', 'cat'),
        ('Test Name', ' ', 'F', 'cat'),
        ('Test Name', 2, '', 'cat'),
        ('Test Name', 2, ' ', 'cat'),
        ('Test Name', 2, 'F', 'Cat'),
        ('Test Name', 2, 'F', ''),
        ('Test Name', 2, 'F', ' '),
        ('Test Name', 2, 'F', 'Dog'),
        ('Test Name', 2, 'F', 1),
    ])
    def test_pets_put_wrong_data_bad_request(self, simple_user, api_client, breed, name, age, gender, species, pet):
        api_client.force_authenticate(simple_user)
        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "species": species,
            "breed": breed.id,
            "user": simple_user.id
        }
        response = api_client.put(f'{self.endpoint}{pet.id}/', data=data, format='json')
        assert response.status_code == 400

    def test_pets_put_id_not_found(self, simple_user, breed, api_client):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "New Name",
            "age": 3,
            "gender": "M",
            "species": "dog",
            "breed": breed.id,
            "user": simple_user.id
        }
        response = api_client.put(f'{self.endpoint}999999/', data=data, format='json')
        assert response.status_code == 404

    def test_pets_put_not_owned_by_requested_user_not_found(self, simple_user, pets_list, api_client, breed):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "New Name",
            "age": 3,
            "gender": "M",
            "species": "dog",
            "breed": breed.id,
            "user": simple_user.id
        }
        response = api_client.put(f'{self.endpoint}{pets_list[2].id}/', data=data, format='json')
        assert response.status_code == 404

    def test_pets_patch_with_staff_user_success(self, staff_user, api_client, pet):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{pet.id}/', data={"name": "new name"}, format='json')
        assert response.status_code == 200

    def test_pets_patch_with_simple_user_success(self, simple_user, api_client, pet):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{pet.id}/', data={"name": "new name"}, format='json')
        assert response.status_code == 200

    def test_pets_patch_with_provider_user_permission_denied(self, provider_user, api_client, pet):
        api_client.force_authenticate(provider_user)
        response = api_client.patch(f'{self.endpoint}{pet.id}/', data={"name": "new name"}, format='json')
        assert response.status_code == 403

    def test_pets_patch_not_owned_by_requested_user_not_found(self, simple_user, pets_list, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.put(f'{self.endpoint}{pets_list[2].id}/', data={"name": "test name"}, format='json')
        assert response.status_code == 404

    def test_pets_patch_id_not_found(self, simple_user, breed, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.put(f'{self.endpoint}999999/', data={"name": "test name"}, format='json')
        assert response.status_code == 404

    def test_pets_delete_with_staff_user_success(self, staff_user, api_client, pet):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}{pet.id}/')
        assert response.status_code == 204

    def test_pets_delete_with_simple_user_success(self, simple_user, api_client, pet):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f'{self.endpoint}{pet.id}/')
        assert response.status_code == 204

    def test_pets_delete_with_simple_user_not_owned_not_found(self, simple_user, api_client, pets_list):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f'{self.endpoint}{pets_list[2]}/')
        assert response.status_code == 404

    def test_pets_delete_with_provider_user_permission_denied(self, provider_user, api_client, pet):
        api_client.force_authenticate(provider_user)
        response = api_client.delete(f'{self.endpoint}{pet.id}/')
        assert response.status_code == 403

    def test_pest_delete_not_found(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}999999/')
        assert response.status_code == 404

    @pytest.mark.parametrize('name, length', [
        ('samy', 1),
        ('SAMY', 1),
        ('sam', 1),
        ('a', 2),
        ('', 3),
    ])
    def test_pets_search_by_name(self, staff_user, api_client, pets_list, name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?search={name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_pets_ordering_by_name(self, staff_user, api_client, pets_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?ordering=name')
        assert response.status_code == 200
        assert json.loads(response.content)[0].get('name') == 'Jack'

    def test_pets_ordering_by_age_ascending(self, staff_user, api_client, pets_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?ordering=age')
        assert response.status_code == 200
        assert json.loads(response.content)[0].get('age') == 3

    def test_pets_ordering_by_age_descending(self, staff_user, api_client, pets_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?ordering__descending=age')
        assert response.status_code == 200
        assert json.loads(response.content)[0].get('age') == 4

    @pytest.mark.parametrize('page, length', [
        (1, 2), (2, 1)
    ])
    def test_pet_pagination_success(self, staff_user, pets_list, api_client, page, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size=2')
        assert response.status_code == 200
        assert len(json.loads(response.content).get('results')) == length

    @pytest.mark.parametrize('page', [-1, 'one', 999999, '', ' '])
    def test_pet_pagination_not_found(self, staff_user, pets_list, api_client, page):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size=2')
        assert response.status_code == 404

    # test PetFilter
    @pytest.mark.parametrize('name, length', [('Jack', 1), ('Ja', 0), ('jack', 0), ('ck', 0)])
    def test_pet_filter_by_name_exact_success(self, staff_user, pets_list, api_client, name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name={name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    # test  filter by pet's name
    @pytest.mark.parametrize('name, length', [('Jack', 1), ('Ja', 1), ('jack', 1), ('ck', 1)])
    def test_pet_filter_by_name_icontains_success(self, staff_user, pets_list, api_client, name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name__icontains={name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    #  test filter by breed
    def test_pet_filter_by_breed_icontains_success(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?breed=lalal')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    @pytest.mark.parametrize('breed_name, length', [('German Shepherd', 3), ('Ja', 0), (' ', 3), ('', 3)])
    def test_pet_filter_by_breed_exact_success(self, staff_user, pets_list, api_client, breed_name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?breed={breed_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    #  test filter by user_name
    @pytest.mark.parametrize('user_name, length', [('Simple User', 2), ('Simple', 2), (' ', 3), ('', 3), ('123ffa', 0)])
    def test_pet_filter_by_user_exact_success(self, staff_user, pets_list, api_client, user_name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?user={user_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    #  test filter by created_at
    def test_pet_filter_created_at_year_exact_success(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_pet_filter_created_at_year_exact_bad_request(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 3), (2023, 0), ('2022', 3)])
    def test_pet_filter_created_at_year_gt_success(self, staff_user, pets_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_pet_filter_created_at_year_gt_bad_request(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 3), ('2022', 0)])
    def test_pet_filter_created_at_year_lt_success(self, staff_user, pets_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_pet_filter_created_at_year_lt_bad_request(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt=2023-10-20')
        assert response.status_code == 400

    def test_pet_filter_created_at_bad_request(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023')
        assert response.status_code == 400

    def test_pet_filter_created_at_bad_success(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023-10-10')
        assert response.status_code == 200

    #  test filter by species
    @pytest.mark.parametrize('species, length', [('cat', 1), ('dog', 2)])
    def test_pet_filter_by_species_exact_success(self, staff_user, pets_list, api_client, species, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?species={species}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_pet_filter_by_species_bad_request(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?species=bird')
        assert response.status_code == 400

        # test filter by gender

    @pytest.mark.parametrize('gender, length', [('F', 1), ('M', 2)])
    def test_pet_filter_by_gender_exact_success(self, staff_user, pets_list, api_client, gender, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?gender={gender}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_pet_filter_by_gender_bad_request(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?gender=female')
        assert response.status_code == 400

        # test filter by age
    @pytest.mark.parametrize('age, length', [('3', 1), ('4', 1), ('5', 1), (999, 0)])
    def test_pet_filter_by_age_exact_success(self, staff_user, pets_list, api_client, age, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age={age}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_pet_filter_by_age_bad_request(self, staff_user, pets_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?age=nine')
        assert response.status_code == 400
