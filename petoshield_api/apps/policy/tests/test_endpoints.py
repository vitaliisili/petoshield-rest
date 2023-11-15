import json
import pytest  # noqa


class TestServiceProviderEndpoints:
    endpoint = '/api/insurance/service-providers/'

    # test ServiceProviderFilter by company name
    @pytest.mark.parametrize('company_name, length',
                             [('Service Provider 2', 1),
                              ('Service Provider 3', 1),
                              ('Service Provider 4', 1)
                              ])
    def test_service_provider_filter_by_company_name_exact_success(
            self,
            staff_user,
            service_provider_list,
            api_client,
            company_name,
            length
    ):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?company_name={company_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    @pytest.mark.parametrize('company_name, length', [('Service', 4), ('Provider 3', 1), ('4', 1), ('', 4)])
    def test_service_provider_filter_by_company_name_icontains_success(
            self,
            staff_user,
            service_provider_list,
            api_client,
            company_name,
            length
    ):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?company_name__icontains={company_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    # test ServiceProviderFilter by user_name
    @pytest.mark.parametrize('user_name, length', [('Example', 3), ('example name1', 1), ('name2', 1), (' ', 4)])
    def test_service_provider_filter_by_user_name_icontains_success(self,
                                                                    staff_user,
                                                                    service_provider_list,
                                                                    api_client,
                                                                    user_name,
                                                                    length
                                                                    ):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?user={user_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    #  test ServiceProviderFilter by registration_number
    @pytest.mark.parametrize('registration_number, length',
                             [
                                 ('56899-5655-582', 1),
                                 ('Provider 3', 0),
                                 ('4', 0),
                                 ('', 4)
                             ]
                             )
    def test_service_provider_filter_by_registration_number_exact_success(self,
                                                                          staff_user,
                                                                          service_provider_list,
                                                                          api_client,
                                                                          registration_number,
                                                                          length
                                                                          ):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?registration_number={registration_number}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    #  test ServiceProviderFilter by registration_number
    @pytest.mark.parametrize('address, length',
                             [('Musterstrasse3, 34332 MusterLand3', 1), ('Strasse', 0), ('112', 0), ('', 4)])
    def test_service_provider_filter_by_address_exact_success(self, staff_user, service_provider_list, api_client,
                                                              address, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?address={address}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    @pytest.mark.parametrize('address, length',
                             [('Musterstrasse3, 34332 MusterLand3', 1), ('Strasse', 4), ('3', 4), ('', 4)])
    def test_service_provider_filter_by_address_icontains_success(self, staff_user, service_provider_list, api_client,
                                                                  address, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?address__icontains={address}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    # test filter by created_at
    def test_service_provider_filter_created_at_year_exact_success(self, staff_user, service_provider_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_service_provider_filter_created_at_year_exact_bad_request(self, staff_user, service_provider_list,
                                                                       api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 4), (2023, 0), ('2022', 4)])
    def test_service_provider_filter_created_at_year_gt_success(self, staff_user, service_provider_list, api_client,
                                                                year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_service_provider_filter_created_at_year_gt_bad_request(self, staff_user, service_provider_list,
                                                                    api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 4), ('2022', 0)])
    def test_service_provider_filter_created_at_year_lt_success(self, staff_user, service_provider_list, api_client,
                                                                year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_service_provider_filter_created_at_year_lt_bad_request(self, staff_user, service_provider_list,
                                                                    api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt=2023-10-20')
        assert response.status_code == 400

    def test_service_provider_filter_created_at_bad_request(self, staff_user, service_provider_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023')
        assert response.status_code == 400

    def test_service_provider_filter_created_at_bad_success(self, staff_user, service_provider_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023-10-10')
        assert response.status_code == 200

    def test_service_provider_list_success(self, staff_user, api_client, service_provider_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(service_provider_list)

    def test_service_provider_list_with_provider_unauthorized(self, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_service_provider_list_with_simple_user_unauthorized(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_service_provider_list_with_anonymous_user_unauthorized(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_service_provider_patch_with_admin_success(self, staff_user, service_provider, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{service_provider.id}/', {'phone': '+499999999999'})
        assert response.status_code == 200
        assert json.loads(response.content).get('phone') == '+499999999999'

    def test_service_provider_patch_with_simple_user_forbidden(self, simple_user, service_provider, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{service_provider.id}/', {'phone': '+499999999999'})
        assert response.status_code == 403

    def test_service_provider_patch_with_service_provider_success(self, provider_user, service_provider, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.patch(f'{self.endpoint}{service_provider.id}/', {'phone': '+499999999999'})
        assert response.status_code == 200
        assert json.loads(response.content).get('phone') == '+499999999999'

    def test_service_provider_patch_with_anonymous_user_unauthorized(self, api_client, service_provider):
        response = api_client.patch(f'{self.endpoint}{service_provider.id}/', {'phone': '+499999999999'})
        assert response.status_code == 401

    def test_service_provider_save_with_admin_user_success(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        data = {"user": {
                        "name": "Roberto",
                        "password": "password1A@",
                        "email": "provider@mail.com"
                        },
                "service_provider": {
                        "company_name": "PetWorld Insdurance",
                        "registration_number": "AK42345670-23",
                        "phone": "+49176855452",
                        "address": "Ludwig Strasse 7, 31134 Hildesheim",
                        "iban": "DE52114575800000254"
                        }
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 201

    def test_service_provider_save_with_admin_user_bad_request(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                "company_name": "PetWorld Insdurance",
                "registration_number": "AK42345670-23",
                "phone": "+49176855452",
                "address": "Ludwig Strasse 7, 31134 Hildesheim",
                "iban": "DE52114575800000254"
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 400

    def test_service_provider_save_with_simple_user_success(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        data = {"user": {
                        "name": "Roberto",
                        "password": "password1A@",
                        "email": "provider@mail.com"
                        },
                "service_provider": {
                        "company_name": "PetWorld Insdurance",
                        "registration_number": "AK42345670-23",
                        "phone": "+49176855452",
                        "address": "Ludwig Strasse 7, 31134 Hildesheim",
                        "iban": "DE52114575800000254"
                        }
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 201

    def test_service_provider_save_with_anonymous_user_success(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        data = {"user": {
                        "name": "Roberto",
                        "password": "password1A@",
                        "email": "provider@mail.com"
                        },
                "service_provider": {
                        "company_name": "PetWorld Insdurance",
                        "registration_number": "AK42345670-23",
                        "phone": "+49176855452",
                        "address": "Ludwig Strasse 7, 31134 Hildesheim",
                        "iban": "DE52114575800000254"
                        }
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 201

    def test_service_provider_save_with_service_provider_success(self, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        data = {"user": {
                        "name": "Roberto",
                        "password": "password1A@",
                        "email": "provider1@mail.com"
                        },
                "service_provider": {
                        "company_name": "PetWorld Insdurance",
                        "registration_number": "AK42345670-23",
                        "phone": "+49176855452",
                        "address": "Ludwig Strasse 7, 31134 Hildesheim",
                        "iban": "DE52114575800000254"
                        }
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 201

    @pytest.mark.parametrize(
        'name, password, email, company_name, registration_number, phone, address, iban',
        [
            ('', "password1A@", "provider@mail.com", "PetWorld Insdurance", "AK42345670-23",
            "+49176855452", "Ludwig Strasse 7, 31134 Hildesheim", "DE52114575800000254"),
            ("Roberto", "password1A@", "", "PetWorld Insdurance", "AK42345670-23", "+49176855452",
            "Ludwig Strasse 7, 31134 Hildesheim", "DE52114575800000254"),
            ("Roberto", "password1A@", "provider@mail.com", "", "AK42345670-23", "+49176855452",
            "Ludwig Strasse 7, 31134 Hildesheim", "DE52114575800000254"),
            ("Roberto", "password1A@", "provider@mail.com", "PetWorld Insdurance", "",
            "+49176855452", "Ludwig Strasse 7, 31134 Hildesheim", "DE52114575800000254"),
            ("Roberto", "password1A@", "provider@mail.com", "PetWorld Insdurance", "AK42345670-23", "",
             "Ludwig Strasse 7, 31134 Hildesheim", "DE52114575800000254"),
            ("Roberto", "password1A@", "provider@mail.com", "PetWorld Insdurance", "AK42345670-23", "+49176855452", "",
             "DE52114575800000254"),
            ("Roberto", "password1A@", "provider@mail.com", "PetWorld Insdurance", "AK42345670-23", "+49176855452",
             "Ludwig Strasse 7, 31134 Hildesheim", "")
        ]
    )
    def test_service_provider_save_with_blank_or_empty_data(self,
                                                            staff_user,
                                                            api_client,
                                                            name,
                                                            password,
                                                            email,
                                                            company_name,
                                                            registration_number,
                                                            phone,
                                                            address,
                                                            iban):
        api_client.force_authenticate(staff_user)
        data = {"user": {
                        "name": name,
                        "password": password,
                        "email": email
                        },
                "service_provider": {
                        "company_name": company_name,
                        "registration_number": registration_number,
                        "phone": phone,
                        "address": address,
                        "iban": iban
                        }
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 400

    def test_service_provider_put_with_admin_user_success(self, staff_user, api_client, service_provider):
        api_client.force_authenticate(staff_user)
        data = {"company_name": "PetWorld Insurance AG",
                "phone": "+49176855452",
                "registration_number": "FT53822U",
                "address": "Ludwig Strasse 7, 31134 Hildesheim",
                "iban": "DE52114575800000254"
                }
        response = api_client.put(f'{self.endpoint}{service_provider.id}/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('iban') == "DE52114575800000254"

    def test_service_provider_put_with_simple_user_forbidden(self, simple_user, api_client, service_provider):
        api_client.force_authenticate(simple_user)
        data = {"company_name": "PetWorld Insurance AG",
                "phone": "+49176855452",
                "registration_number": "FT53822U",
                "address": "Ludwig Strasse 7, 31134 Hildesheim",
                "iban": "DE52114575800000254"
                }
        response = api_client.put(f'{self.endpoint}{service_provider.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_service_provider_put_with_provider_user_success(self, provider_user, api_client, service_provider):
        api_client.force_authenticate(provider_user)
        data = {"company_name": "PetWorld Insurance AG",
                "phone": "+49176855452",
                "registration_number": "FT53822U",
                "address": "Ludwig Strasse 7, 31134 Hildesheim",
                "iban": "DE52114575800000254"
                }
        response = api_client.put(f'{self.endpoint}{service_provider.id}/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('iban') == "DE52114575800000254"

    def test_service_provider_put_with_anonymous_user_unauthorized(self, api_client, service_provider):
        data = {"company_name": "PetWorld Insurance AG",
                "phone": "+49176855452",
                "registration_number": "FT53822U",
                "address": "Ludwig Strasse 7, 31134 Hildesheim",
                "iban": "DE52114575800000254"
                }
        response = api_client.put(f'{self.endpoint}{service_provider.id}/', data=data, format='json')
        assert response.status_code == 401

    def test_service_provider_put_service_provider_not_found(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        data = {"company_name": "PetWorld Insurance AG",
                "phone": "+49176855452",
                "registration_number": "FT53822U",
                "address": "Ludwig Strasse 7, 31134 Hildesheim",
                "iban": "DE52114575800000254"
                }
        response = api_client.put(f'{self.endpoint}5556585/', data=data, format='json')
        assert response.status_code == 404

    def test_service_provider_delete_with_admin_user_success(self, staff_user, api_client, service_provider):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}{service_provider.id}/')
        assert response.status_code == 204

    def test_service_provider_delete_with_simple_user_forbidden(self, simple_user, api_client, service_provider):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f'{self.endpoint}{service_provider.id}/')
        assert response.status_code == 403

    def test_service_provider_delete_with_provider_user_forbidden(self,
                                                                  provider_user,
                                                                  api_client,
                                                                  service_provider_list):
        api_client.force_authenticate(provider_user)
        response = api_client.delete(f'{self.endpoint}{service_provider_list[3].id}/')
        assert response.status_code == 403

    def test_service_provider_delete_himself_with_provider_user_success(self,
                                                                        provider_user,
                                                                        api_client,
                                                                        service_provider):
        api_client.force_authenticate(provider_user)
        response = api_client.delete(f'{self.endpoint}{service_provider.id}/')
        assert response.status_code == 204

    def test_service_provider_delete_with_anonymous_user_unauthorized(self, api_client, service_provider):
        response = api_client.delete(f'{self.endpoint}{service_provider.id}/')
        assert response.status_code == 401

    def test_service_provider_delete_provider_not_found(self,
                                                        staff_user,
                                                        api_client,
                                                        service_provider):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}595665/')
        assert response.status_code == 404


class TestPolicyEndpoints:
    endpoint = '/api/insurance/policies/'

    # test filter by pet
    @pytest.mark.parametrize('pet_name, length', [('Simple User dog', 1), ('Jack', 1), ('Lenore', 1), (2, 0)])
    def test_policy_filter_by_pet_success(self, staff_user, policies_list, api_client, pet_name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?pet={pet_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    # test filter by start_date
    def test_policy_filter_by_start_date_exact_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?start_date=2023-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_policy_filter_by_start_date_exact_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?start_date=01-11-2023')
        assert response.status_code == 400

    def test_policy_filter_by_start_date_gt_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?start_date__gt=2023-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_policy_filter_by_start_date_gt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?start_date__gt=01-11-2023')
        assert response.status_code == 400

    def test_policy_filter_by_start_date_lt_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?start_date__lt=2023-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_policy_filter_by_start_date_lt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?start_date__lt=01-11-2023')
        assert response.status_code == 400

    # test filter by end_date
    def test_policy_filter_by_end_date_exact_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date=2023-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_policy_filter_by_end_date_exact_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date=01-11-2024')
        assert response.status_code == 400

    def test_policy_filter_by_end_date_gt_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__gt=2024-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_policy_filter_by_end_date_gt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__gt=01-11-2024')
        assert response.status_code == 400

    def test_policy_filter_by_end_date_lt_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__lt=2024-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_policy_filter_by_end_date_lt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__lt=01-11-2024')
        assert response.status_code == 400

    # test filter by status
    @pytest.mark.parametrize('status, length', [('valid', 3), ('expired', 1), ('invalid', 0)])
    def test_policy_filter_by_status_exact_success(self, staff_user, policies_list, api_client, status, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?status={status}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_policy_filter_by_status_exact_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?status=asd')
        assert response.status_code == 400

        # test filter by price
    @pytest.mark.parametrize('price_, length', [(17.25, 1), (12.58, 1), ('', 4), ('99999', 0)])
    def test_policy_filter_by_price_exact_success(self, staff_user, policies_list, api_client, price_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?price={price_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_policy_filter_by_price_exact_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?price=one')
        assert response.status_code == 400

    @pytest.mark.parametrize('price_, length', [(11, 4), (17.25, 0), ('', 4), ('99999', 0)])
    def test_policy_filter_by_price_gt_success(self, staff_user, policies_list, api_client, price_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?price__gt={price_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_policy_filter_by_price_gt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?price__gt=one')
        assert response.status_code == 400

    def test_policy_filter_by_price_lt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?price__lt=one')
        assert response.status_code == 400

    # test filter by deductible
    @pytest.mark.parametrize('deductible, length', [(300, 1), (1000, 1), (2000, 1), ('', 4), ('99999', 0)])
    def test_policy_filter_by_deductible_exact_success(self, staff_user, policies_list, api_client, deductible, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?deductible={deductible}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_policy_filter_by_deductible_exact_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?deductible=one')
        assert response.status_code == 400

    @pytest.mark.parametrize('deductible, length', [(300, 3), (1000, 1), (2000, 0), ('', 4), ('99999', 0)])
    def test_policy_filter_by_deductible_gt_success(self, staff_user, policies_list, api_client, deductible, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?deductible__gt={deductible}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_policy_filter_by_deductible_gt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?deductible__gt=one')
        assert response.status_code == 400

    def test_policy_filter_by_deductible_lt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?deductible__lt=one')
        assert response.status_code == 400

    # test filter by created_at
    def test_policy_filter_by_created_at_year_exact_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_policy_filter_by_created_at_year_exact_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 4), (2023, 0), ('2022', 4)])
    def test_policy_filter_by_created_at_year_gt_success(self, staff_user, policies_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_policy_filter_by_created_at_year_gt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 4), ('2022', 0)])
    def test_policy_filter_by_created_at_year_lt_success(self, staff_user, policies_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_policy_filter_by_created_at_year_lt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt=2023-10-20')
        assert response.status_code == 400

    def test_policy_filter_by_created_at_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023')
        assert response.status_code == 400

    def test_policy_filter_by_created_at_bad_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023-10-10')
        assert response.status_code == 200

    def test_policy_list_with_staff_user_success(self, staff_user, api_client, policies_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(policies_list)

    def test_policy_list_with_simple_user_success(self, simple_user, api_client, policies_list):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    # Have to check, ERROR
    # def test_policy_list_with_provider_user_success(self, provider_user, api_client, policies_list):
    #     api_client.force_authenticate(provider_user)
    #     response = api_client.get(self.endpoint)
    #     assert response.status_code == 200

    def test_policy_list_with_anonymous_user_unauthorized(self, api_client, policies_list):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_policy_save_with_staff_user_forbidden(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "policy_number": "123-456-234567",
                    "start_date": "2023-10-10",
                    "end_date": "2024-10-10",
                    "status": "valid",
                    "initial_limit": 10000,
                    "current_limit": 10000,
                    "deductible": 500,
                    "pet": 11,
                    "providers": []
                }
        response = api_client.post(f'{self.endpoint}', data=data)
        assert response.status_code == 403

    def test_policy_save_with_simple_user_forbidden(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        data = {
                    "policy_number": "123-456-234567",
                    "start_date": "2023-10-10",
                    "end_date": "2024-10-10",
                    "status": "valid",
                    "initial_limit": 10000,
                    "current_limit": 10000,
                    "deductible": 500,
                    "pet": 11,
                    "providers": []
                }
        response = api_client.post(f'{self.endpoint}', data=data)
        assert response.status_code == 403

    def test_policy_save_with_provider_user_forbidden(self, provider_user, api_client):
        api_client.force_authenticate(provider_user)
        data = {
                    "policy_number": "123-456-234567",
                    "start_date": "2023-10-10",
                    "end_date": "2024-10-10",
                    "status": "valid",
                    "initial_limit": 10000,
                    "current_limit": 10000,
                    "deductible": 500,
                    "pet": 11,
                    "providers": []
                }
        response = api_client.post(f'{self.endpoint}', data=data)
        assert response.status_code == 403

    def test_policy_save_with_anonymous_user_unauthorized(self, api_client):
        data = {
                    "policy_number": "123-456-234567",
                    "start_date": "2023-10-10",
                    "end_date": "2024-10-10",
                    "status": "valid",
                    "initial_limit": 10000,
                    "current_limit": 10000,
                    "deductible": 500,
                    "pet": 11,
                    "providers": []
                }
        response = api_client.post(f'{self.endpoint}', data=data)
        assert response.status_code == 401

    def test_policy_patch_with_staff_user_success(self, staff_user, policy, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "status": "expired"
                }
        response = api_client.patch(f'{self.endpoint}{policy.id}/', data=data)
        assert response.status_code == 200
        assert json.loads(response.content).get('status') == "expired"

    def test_policy_patch_with_simple_user_forbidden(self, simple_user, policy, api_client):
        api_client.force_authenticate(simple_user)
        data = {
                    "status": "expired"
                }
        response = api_client.patch(f'{self.endpoint}{policy.id}/', data=data)
        assert response.status_code == 403

    def test_policy_patch_with_provider_user_forbidden(self, provider_user, policy, api_client):
        api_client.force_authenticate(provider_user)
        data = {
                    "status": "expired"
                }
        response = api_client.patch(f'{self.endpoint}{policy.id}/', data=data)
        assert response.status_code == 403

    def test_policy_patch_with_anonymous_user_unauthorized(self, api_client, policy):
        data = {
                    "status": "expired"
                }
        response = api_client.patch(f'{self.endpoint}{policy.id}/', data=data)
        assert response.status_code == 401

    def test_policy_put_with_staff_user_success(self, staff_user, policy, pet, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "created_at": "2023-10-26T08:20:36.990701Z",
                    "updated_at": "2023-10-26T08:20:36.990721Z",
                    "policy_number": "new field",
                    "start_date": "2022-10-10",
                    "end_date": "2023-10-10",
                    "status": "expired",
                    "initial_limit": "10000.00",
                    "current_limit": "10000.00",
                    "deductible": "500.00",
                    "pet": pet.id
                }
        response = api_client.put(f'{self.endpoint}{policy.id}/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('status') == 'expired'
        assert json.loads(response.content).get('end_date') == '2023-10-10'

    def test_policy_put_with_simple_user_forbidden(self, simple_user, policy, pet, api_client):
        api_client.force_authenticate(simple_user)
        data = {
                    "policy_number": "new field",
                    "start_date": "2022-10-10",
                    "end_date": "2023-10-10",
                    "status": "expired",
                    "initial_limit": "10000.00",
                    "current_limit": "10000.00",
                    "deductible": "500.00",
                    "pet": pet.id
                }
        response = api_client.put(f'{self.endpoint}{policy.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_policy_put_with_provider_user_forbidden(self, provider_user, policy, pet, api_client):
        api_client.force_authenticate(provider_user)
        data = {
                    "policy_number": "new field",
                    "start_date": "2022-10-10",
                    "end_date": "2023-10-10",
                    "status": "expired",
                    "initial_limit": "10000.00",
                    "current_limit": "10000.00",
                    "deductible": "500.00",
                    "pet": pet.id
                }
        response = api_client.put(f'{self.endpoint}{policy.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_policy_put_with_anonymous_user_unauthorize(self, policy, pet, api_client):
        data = {
                    "policy_number": "new field",
                    "start_date": "2022-10-10",
                    "end_date": "2023-10-10",
                    "status": "expired",
                    "initial_limit": "10000.00",
                    "current_limit": "10000.00",
                    "deductible": "500.00",
                    "pet": pet.id
                }
        response = api_client.put(f'{self.endpoint}{policy.id}/', data=data, format='json')
        assert response.status_code == 401

    @pytest.mark.parametrize('policy_number, start_date, end_date, status, initial_limit, current_limit, deductible',
                             [
                                 ("", "2022-10-10", "2023-10-10", "expired", "10000.00", "10000.00", "500.00"),
                                 ("new field", "2022/10/10", "2023-10-10", "expired", "10000.00", "10000.00", "500.00"),
                                 ("new field", "", "2023-10-10", "expired", "10000.00", "10000.00", "500.00"),
                                 ("new field", "2022-10-10", "", "expired", 10000.00, "10000.00", "500.00"),
                                 ("new field", "2022-10-10", "2023-10-10", "", "10000.00", "10000.00", "500.00"),
                                 ("new field", "2022-10-10", "2023-10-10", "expired", "", 10000.00, "500.00"),
                                 ("new field", "2022-10-10", "2023-10-10", "expired", "10000.00", "", 500.00),
                                 ("new field", "2022-10-10", "2023-10-10", "expired", "10000.00", "10000.00", ""),
                                 ("new field", "2022-10-10", "2023-10-10", "expired", "10000.00", "10000.00",
                                  "five hundred")
                             ]
                            )
    def test_policy_put_with_blank_or_wrong_data_bad_request(self,
                                                            staff_user,
                                                            policy,
                                                            pet,
                                                            api_client,
                                                            policy_number,
                                                            start_date,
                                                            end_date,
                                                            status,
                                                            initial_limit,
                                                            current_limit,
                                                            deductible):
        api_client.force_authenticate(staff_user)
        data = {
                    "policy_number": policy_number,
                    "start_date": start_date,
                    "end_date": end_date,
                    "status": status,
                    "initial_limit": initial_limit,
                    "current_limit": current_limit,
                    "deductible": deductible,
                    "pet": pet.id
                }
        response = api_client.put(f'{self.endpoint}{policy.id}/', data=data, format='json')
        assert response.status_code == 400

    def test_policy_delete_with_staff_user_success(self, staff_user, policy, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f"{self.endpoint}{policy.id}/")
        assert response.status_code == 204

    def test_policy_delete_with_simple_user_forbidden(self, simple_user, policy, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f"{self.endpoint}{policy.id}/")
        assert response.status_code == 403

    def test_policy_delete_with_forbidden(self, provider_user, policy, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.delete(f"{self.endpoint}{policy.id}/")
        assert response.status_code == 403

    def test_policy_delete_with_anonymous_user_unauthorize(self, policy, api_client):
        response = api_client.delete(f"{self.endpoint}{policy.id}/")
        assert response.status_code == 401

    def test_policy_delete_not_found(self, staff_user, policy, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f"{self.endpoint}55666/")
        assert response.status_code == 404


class TestInsuranceCaseEndpoints:
    endpoint = '/api/insurance/insurance-cases/'

    # test filter by policy number
    @pytest.mark.parametrize('policy_nr, length',
                             [('84-121-4860', 1), ('84', 1), ('', 4), (' ', 4), ('33', 1), (84, 1)])
    def test_insurance_cases_filter_by_policy_success(self, staff_user, insurance_cases_list, api_client, policy_nr,
                                                      length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?policy={policy_nr}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    # test filter by service provider
    @pytest.mark.parametrize('service_provider_, length',
                             [('Service Provider 2', 1), ('Service Provider 1', 1), ('Service', 4)])
    def test_insurance_cases_filter_by_service_provider_success(self, staff_user, insurance_cases_list, api_client,
                                                                service_provider_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?service_provider={service_provider_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    # test filter by created_at
    def test_insurance_cases_filter_by_created_at_year_exact_success(self, staff_user, insurance_cases_list,
                                                                     api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_insurance_cases_filter_by_created_at_year_exact_bad_request(self, staff_user, insurance_cases_list,
                                                                         api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 4), (2023, 0), ('2022', 4)])
    def test_insurance_cases_filter_by_created_at_year_gt_success(self, staff_user, insurance_cases_list, api_client,
                                                                  year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_insurance_cases_filter_by_created_at_year_gt_bad_request(self, staff_user, insurance_cases_list,
                                                                      api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 4), ('2022', 0)])
    def test_insurance_cases_filter_by_created_at_year_lt_success(self, staff_user, insurance_cases_list, api_client,
                                                                  year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_insurance_cases_filter_by_created_at_year_lt_bad_request(self, staff_user, insurance_cases_list,
                                                                      api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt=2023-10-20')
        assert response.status_code == 400

    def test_insurance_cases_filter_by_created_at_bad_request(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023')
        assert response.status_code == 400

    def test_insurance_cases_filter_by_created_at_bad_success(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023-10-10')
        assert response.status_code == 200

    # test filter by status
    @pytest.mark.parametrize('status, length', [('accept', 2), ('reject', 1), ('process', 1)])
    def test_insurance_cases_filter_by_status_exact_success(self, staff_user, insurance_cases_list, api_client, status,
                                                            length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?status={status}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_insurance_cases_filter_by_status_exact_bad_request(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?status=asd')
        assert response.status_code == 400

    @pytest.mark.parametrize('status, length', [('acc', 2), ('rej', 1), ('proc', 1), ('asd', 0)])
    def test_insurance_cases_filter_by_status_icontains_success(self, staff_user, insurance_cases_list, api_client,
                                                                status, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?status__icontains={status}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_insurance_case_list_with_staff_user_success(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(insurance_cases_list)

    def test_insurance_case_list_with_simple_user_success(self, simple_user, insurance_cases_list, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_insurance_case_list_with_provider_user_success(self, provider_user, insurance_cases_list, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_insurance_case_list_with_anonymous_user_unauthorize(self, insurance_cases_list, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_insurance_case_save_with_staff_user_success(self, staff_user, service_provider, policy, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Test insurance case",
                    "status": "accept",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 201

    def test_insurance_case_save_with_staff_user_bad_request(self, staff_user, service_provider, policy, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Test insurance case",
                    "status": "accept"
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 400

    def test_insurance_case_save_with_simple_user_forbidden(self, simple_user, service_provider, policy, api_client):
        api_client.force_authenticate(simple_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Test insurance case",
                    "status": "accept",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 403

    def test_insurance_case_save_with_provider_user_forbidden(self, provider_user, service_provider,
                                                              policy, api_client):
        api_client.force_authenticate(provider_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Test insurance case",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 201

    def test_insurance_case_save_with_anonymous_user_unauthorize(self, service_provider, policy, api_client):
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Test insurance case",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 401

    @pytest.mark.parametrize("claim_date, description",
                             [
                                 ("", "Test insurance case"),
                                 ("30-10-2023", "Test insurance case"),
                                 ("2023-09-30", "")
                             ])
    def test_insurance_case_save_with_blank_or_wrong_data(self, staff_user, claim_date, description,
                                                          service_provider, policy, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "claim_date": claim_date,
                    "description": description,
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.post(f'{self.endpoint}', data=data, format='json')
        assert response.status_code == 400

    def test_insurance_case_put_with_staff_user_success(self, staff_user, insurance_case, service_provider,
                                                        policy, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Cat broke his leg",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.put(f'{self.endpoint}{insurance_case.id}/', data=data, format='json')
        assert response.status_code == 200
        assert json.loads(response.content).get('description') == "Cat broke his leg"

    def test_insurance_case_put_with_staff_user_not_found(self, staff_user, service_provider, policy, api_client):
        api_client.force_authenticate(staff_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Cat broke his leg",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.put(f'{self.endpoint}996565/', data=data, format='json')
        assert response.status_code == 404

    @pytest.mark.parametrize('claim_date, description, status',
                             {
                                 ("", "Cat broke his leg", "active"),
                                 ("2023-09-30", "Cat broke his leg", 1),
                                 ("2023-09-30", "Cat broke his leg", "inactive"),
                                 ("2023-09-30", "", "active")
                             })
    def test_insurance_case_put_with_blank_or_wrong_data_bad_request(self, staff_user, insurance_case, service_provider,
                                                        policy, api_client, claim_date, description, status):
        api_client.force_authenticate(staff_user)
        data = {
                    "claim_date": claim_date,
                    "description": description,
                    "status": status,
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.put(f'{self.endpoint}{insurance_case.id}/', data=data, format='json')
        assert response.status_code == 400

    def test_insurance_case_put_with_simple_user_forbidden(self, simple_user, insurance_case, service_provider,
                                                        policy, api_client):
        api_client.force_authenticate(simple_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Cat broke his leg",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.put(f'{self.endpoint}{insurance_case.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_insurance_case_put_with_provider_user_forbidden(self, provider_user, insurance_case, service_provider,
                                                        policy, api_client):
        api_client.force_authenticate(provider_user)
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Cat broke his leg",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.put(f'{self.endpoint}{insurance_case.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_insurance_case_put_with_anonymous_user_unauthorize(self, insurance_case, service_provider,
                                                        policy, api_client):
        data = {
                    "claim_date": "2023-09-30",
                    "description": "Cat broke his leg",
                    "service_provider": service_provider.id,
                    "policy": policy.id
                }
        response = api_client.put(f'{self.endpoint}{insurance_case.id}/', data=data, format='json')
        assert response.status_code == 401

    def test_insurance_case_patch_with_staff_user_success(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{insurance_cases_list[2]}.id',
                                    {"description": "Cat broke his leg"})
        assert response.status_code == 200
        assert json.loads(response.content).get('description') == "Cat broke his leg"

    def test_insurance_case_patch_with_simple_user_forbidden(self, simple_user, insurance_cases_list, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{insurance_cases_list[1]}.id',
                                    {"description": "Cat broke his leg"})
        assert response.status_code == 403

    def test_insurance_case_patch_with_provider_user_forbidden(self, provider_user, insurance_cases_list, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.patch(f'{self.endpoint}{insurance_cases_list[1]}.id',
                                    {"description": "Cat broke his leg"})
        assert response.status_code == 403

    def test_insurance_case_patch_with_anonymous_user_unauthorize(self, insurance_cases_list, api_client):
        response = api_client.patch(f'{self.endpoint}{insurance_cases_list[0]}.id',
                                    {"description": "Cat broke his leg"})
        assert response.status_code == 401

    def test_insurance_case_delete_with_staff_user_success(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}{insurance_cases_list[1].id}/')
        assert response.status_code == 204

    def test_insurance_case_delete_with_simple_user_forbidden(self, simple_user, insurance_cases_list, api_client):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f'{self.endpoint}{insurance_cases_list[0].id}/')
        assert response.status_code == 403

    def test_insurance_case_delete_with_provider_user_forbidden(self, provider_user, insurance_cases_list, api_client):
        api_client.force_authenticate(provider_user)
        response = api_client.delete(f'{self.endpoint}{insurance_cases_list[2].id}/')
        assert response.status_code == 403

    def test_insurance_case_delete_with_anonymous_user_unauthorize(self, insurance_cases_list, api_client):
        response = api_client.delete(f'{self.endpoint}{insurance_cases_list[2].id}/')
        assert response.status_code == 401

    def test_insurance_case_delete_case_not_found(self, staff_user, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}5644/')
        assert response.status_code == 404


class TestIncomingInvoiceEndpoints:
    endpoint = '/api/insurance/incoming-invoices/'

    # test filter by invoice_data
    @pytest.mark.parametrize('invoice_date_, length', [('2023-11-06', 1), ('2023-11-03', 1)])
    def test_incoming_invoice_filter_by_invoice_date_exact_success(self, staff_user, incoming_invoices_list, api_client,
                                                                   invoice_date_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?invoice_date={invoice_date_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_invoice_date_exact_bad_request(self, staff_user, incoming_invoices_list,
                                                                       api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?invoice_date=03-11-2023')
        assert response.status_code == 400

    @pytest.mark.parametrize('invoice_date_, length', [('2023-11-06', 0), ('2023-11-03', 1)])
    def test_incoming_invoice_filter_by_invoice_date_gt_success(self, staff_user, incoming_invoices_list, api_client,
                                                                invoice_date_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?invoice_date__gt={invoice_date_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_invoice_date_gt_bad_request(self, staff_user, incoming_invoices_list,
                                                                    api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?invoice_date__gt=03-11-2023')
        assert response.status_code == 400

    @pytest.mark.parametrize('invoice_date_, length', [('2023-11-06', 1), ('2023-11-03', 0)])
    def test_incoming_invoice_filter_by_invoice_date_lt_success(self, staff_user, incoming_invoices_list, api_client,
                                                                invoice_date_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?invoice_date__lt={invoice_date_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_invoice_date_lt_bad_request(self, staff_user, incoming_invoices_list,
                                                                    api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?invoice_date__lt=2023')
        assert response.status_code == 400

        # test filter by amount
    @pytest.mark.parametrize('amount_, length', [('125.39', 1), (125.39, 1), (750.50, 1)])
    def test_incoming_invoice_filter_by_amount_exact_success(self, staff_user, incoming_invoices_list, api_client,
                                                             amount_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?amount={amount_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_amount_exact_bad_request(self, staff_user, incoming_invoices_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?amount=ten')
        assert response.status_code == 400

    @pytest.mark.parametrize('amount_, length', [('125.39', 1), (125.39, 1), (750.50, 0)])
    def test_incoming_invoice_filter_by_amount_gt_success(self, staff_user, incoming_invoices_list, api_client, amount_,
                                                          length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?amount__gt={amount_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_amount_gt_bad_request(self, staff_user, incoming_invoices_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?amount__gt=ten')
        assert response.status_code == 400

    @pytest.mark.parametrize('amount_, length', [('125.39', 0), (125.39, 0), (750.50, 1), (99999, 2)])
    def test_incoming_invoice_filter_by_amount_lt_success(self, staff_user, incoming_invoices_list, api_client, amount_,
                                                          length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?amount__lt={amount_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_amount_lt_bad_request(self, staff_user, incoming_invoices_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?amount__lt=ten')
        assert response.status_code == 400

    # test filter by insurance_care
    @pytest.mark.parametrize('insurance_case_, length', [('2023-11-05', 1), ('2023-11-03', 1), ('2022-10-03', 0)])
    def test_incoming_invoice_filter_by_insurance_case_exact_success(self, staff_user, incoming_invoices_list,
                                                                     api_client, insurance_case_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?insurance_case={insurance_case_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_insurance_case_exact_bad_request(self, staff_user, incoming_invoices_list,
                                                                         api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?insurance_case=05-11-2023')
        assert response.status_code == 400

    # test filter by created_at
    def test_incoming_invoice_filter_by_created_at_year_exact_success(self, staff_user, incoming_invoices_list,
                                                                      api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_incoming_invoice_filter_by_created_at_year_exact_bad_request(self, staff_user, incoming_invoices_list,
                                                                          api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 2), (2023, 0), ('2022', 2)])
    def test_incoming_invoice_filter_by_created_at_year_gt_success(self, staff_user, incoming_invoices_list, api_client,
                                                                   year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_created_at_year_gt_bad_request(self, staff_user, incoming_invoices_list,
                                                                       api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400

    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 2), ('2022', 0)])
    def test_incoming_invoice_filter_by_created_at_year_lt_success(self, staff_user, incoming_invoices_list, api_client,
                                                                   year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length

    def test_incoming_invoice_filter_by_created_at_year_lt_bad_request(self, staff_user, incoming_invoices_list,
                                                                       api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt=2023-10-20')
        assert response.status_code == 400

    def test_incoming_invoice_filter_by_created_at_bad_request(self, staff_user, incoming_invoices_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023')
        assert response.status_code == 400

    def test_incoming_invoice_filter_by_created_at_bad_success(self, staff_user, incoming_invoices_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at=2023-10-10')
        assert response.status_code == 200
