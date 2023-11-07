import json
import pytest  # noqa

class TestServiceProviderEndpoints:
    endpoint = '/api/insurance/service-providers/'
    
    # test ServiceProviderFilter by company name
    @pytest.mark.parametrize('company_name, length', [('Service Provider 2', 1), ('Service Provider 3', 1), ('Service Provider 4',1)])
    def test_service_provider_filter_by_company_name_exact_success(self,staff_user, service_provider_list, api_client, company_name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?company_name={company_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
        
    @pytest.mark.parametrize('company_name, length', [('Service', 4), ('Provider 3', 1), ('4', 1), ('', 4)])
    def test_service_provider_filter_by_company_name_icontains_success(self,staff_user, service_provider_list, api_client, company_name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?company_name__icontains={company_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
        
    @pytest.mark.parametrize('company_name, length', [('Service', 4), ('Provider 3', 1), ('4', 1), ('', 4)])
    def test_service_provider_filter_by_company_name_icontains_success(self,staff_user, service_provider_list, api_client, company_name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?company_name__icontains={company_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
        
    # test ServiceProviderFilter by registration_number 
    @pytest.mark.parametrize('registration_number, length', [('56899-5655-582', 1), ('Provider 3', 0), ('4', 0), ('', 4)])
    def test_service_provider_filter_by_registration_number_exact_success(self,staff_user, service_provider_list, api_client, registration_number, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?registration_number={registration_number}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
        
    # test ServiceProviderFilter by registration_number 
    @pytest.mark.parametrize('address, length', [('Musterstrasse3, 34332 MusterLand3', 1), ('Strasse', 0), ('112', 0), ('', 4)])
    def test_service_provider_filter_by_address_exact_success(self,staff_user, service_provider_list, api_client, address, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?address={address}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length 
        
    @pytest.mark.parametrize('address, length', [('Musterstrasse3, 34332 MusterLand3', 1), ('Strasse', 4), ('3', 4), ('', 4)])
    def test_service_provider_filter_by_address_icontains_success(self,staff_user, service_provider_list, api_client, address, length):
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
        
    def test_service_provider_filter_created_at_year_exact_bad_request(self, staff_user, service_provider_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400 
        
    @pytest.mark.parametrize('year, length', [(2022, 4), (2023, 0), ('2022', 4)])   
    def test_service_provider_filter_created_at_year_gt_success(self, staff_user, service_provider_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200 
        assert len(json.loads(response.content)) == length
        
    def test_service_provider_filter_created_at_year_gt_bad_request(self, staff_user, service_provider_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400 
        
    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 4), ('2022', 0)])   
    def test_service_provider_filter_created_at_year_lt_success(self, staff_user, service_provider_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200 
        assert len(json.loads(response.content)) == length
        
    def test_service_provider_filter_created_at_year_lt_bad_request(self, staff_user, service_provider_list, api_client):
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
        response = api_client.get(f'{self.endpoint}?end_date=2023-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_policy_filter_by_start_date_exact_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date=01-11-2023')
        assert response.status_code == 400
        
    def test_policy_filter_by_start_date_gt_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__gt=2023-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1
        
    def test_policy_filter_by_start_date_gt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__gt=01-11-2023')
        assert response.status_code == 400
        
    def test_policy_filter_by_start_date_lt_success(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__lt=2023-11-01')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2
        
    def test_policy_filter_by_start_date_lt_bad_request(self, staff_user, policies_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?end_date__lt=01-11-2023')
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
       
    # test filter by initial_limit
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
        
    @pytest.mark.parametrize('deductible, length', [(300, 0), (1000, 2), (2000, 3), ('', 4), ('99999', 4)])
    def test_policy_filter_by_deductible_gt_success(self, staff_user, policies_list, api_client, deductible, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?deductible__lt={deductible}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
        
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
    @pytest.mark.parametrize('policy_nr, length', [('84-121-4860', 1), ('84', 1), ('', 4), (' ', 4), ('33', 1), (84, 1)])
    def test_insurance_cases_filter_by_policy_success(self, staff_user, insurance_cases_list, api_client, policy_nr, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?policy={policy_nr}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
        
    # test filter by service provider
    @pytest.mark.parametrize('service_provider_, length', [('Service Provider 2', 1), ('Service Provider 1', 1), ('Service', 4)])
    def test_insurance_cases_filter_by_service_provider_success(self, staff_user, insurance_cases_list, api_client, service_provider_, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?service_provider={service_provider_}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length
      
    # test filter by created_at
    def test_insurance_cases_filter_by_created_at_year_exact_success(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023')
        assert response.status_code == 200 
        assert len(json.loads(response.content)) == 4
        
    def test_insurance_cases_filter_by_created_at_year_exact_bad_request(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__exact=2023-10-20')
        assert response.status_code == 400 
        
    @pytest.mark.parametrize('year, length', [(2022, 4), (2023, 0), ('2022', 4)])   
    def test_insurance_cases_filter_by_created_at_year_gt_success(self, staff_user, insurance_cases_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt={year}')
        assert response.status_code == 200 
        assert len(json.loads(response.content)) == length
        
    def test_insurance_cases_filter_by_created_at_year_gt_bad_request(self, staff_user, insurance_cases_list, api_client):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__gt=2023-10-20')
        assert response.status_code == 400 
        
    @pytest.mark.parametrize('year, length', [(2022, 0), (2024, 4), ('2022', 0)])   
    def test_insurance_cases_filter_by_created_at_year_lt_success(self, staff_user, insurance_cases_list, api_client, year, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?created_at__year__lt={year}')
        assert response.status_code == 200 
        assert len(json.loads(response.content)) == length
        
    def test_insurance_cases_filter_by_created_at_year_lt_bad_request(self, staff_user, insurance_cases_list, api_client):
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
    @pytest.mark.parametrize('status, length', [('accept', 1), ('reject', 1), ('process', 2)])
    def test_insurance_cases_filter_by_status_exact_success(self, staff_user, insurance_cases_list, api_client, status, length):
       api_client.force_authenticate(staff_user)
       response = api_client.get(f'{self.endpoint}?status={status}') 
       assert response.status_code == 200
       assert len(json.loads(response.content)) == length
      
    def test_insurance_cases_filter_by_status_exact_bad_request(self, staff_user, insurance_cases_list, api_client):
       api_client.force_authenticate(staff_user)
       response = api_client.get(f'{self.endpoint}?status=asd') 
       assert response.status_code == 400 
       
    @pytest.mark.parametrize('status, length', [('acc', 1), ('rej', 1), ('proc', 2), ('asd', 0)])
    def test_insurance_cases_filter_by_status_icontains_success(self, staff_user, insurance_cases_list, api_client, status, length):
       api_client.force_authenticate(staff_user)
       response = api_client.get(f'{self.endpoint}?status__icontains={status}') 
       assert response.status_code == 200
       assert len(json.loads(response.content)) == length
      