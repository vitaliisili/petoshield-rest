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