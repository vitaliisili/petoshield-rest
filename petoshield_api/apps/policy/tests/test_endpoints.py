import json
import pytest  # noqa

class TestServiceProviderEndpoints:
    endpoint = 'api/insurance/service-providers/'
    
    @pytest.mark.parametrize('company_name, length', [('Service Provider 2', 1), ('Service Provider 3', 1), ('Service Provider 4',1)])
    def test_service_provider_filter_by_company_name_exact_success(self,staff_user, service_provider_list, api_client, company_name, length):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?company_name={company_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == length