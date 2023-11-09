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
