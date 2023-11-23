import pytest
import json


class TestTicketEndpoint:
    endpoint = '/api/help/tickets/'

    @pytest.mark.django_db
    def test_ticket_save_success(self, api_client):
        data = {
            "visitor_name": "Visitor",
            "visitor_email": "test@email.com",
            "visitor_message": "ticket text"
        }
        response = api_client.post(self.endpoint, data=data)
        assert response.status_code == 201

    @pytest.mark.django_db
    @pytest.mark.parametrize('name, email, message', [
        ("", "test@email.com", "ticket text"),
        (" ", "test@email.com", "ticket text"),
        ("Visitor", "", "ticket text"),
        ("Visitor", " ", "ticket text"),
        ("Visitor", "test", "ticket text"),
        ("Visitor", "test@email", "ticket text"),
        ("Visitor", "test@email.com", ""),
    ])
    def test_ticket_save_bad_request(self, api_client, name, email, message):
        data = {
            "visitor_name": name,
            "visitor_email": email,
            "visitor_message": message
        }
        response = api_client.post(self.endpoint, data=data)
        assert response.status_code == 400

    def test_ticket_list_staff_user_success(self, api_client, ticket_list, staff_user):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(ticket_list)

    def test_ticket_list_with_simple_user_forbidden(self, api_client, simple_user):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_ticket_list_with_provider_user_forbidden(self, api_client, provider_user):
        api_client.force_authenticate(provider_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_ticket_list_with_anonymous_user_forbidden(self, api_client):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_ticket_update_success(self, api_client, staff_user, ticket):
        api_client.force_authenticate(staff_user)
        patch_data = {
            "visitor_name": "Updated Visitor Name",
        }
        response = api_client.patch(f'{self.endpoint}{ticket.id}/', data=patch_data)
        assert response.status_code == 200

    def test_ticket_update_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        patch_data = {
            "visitor_name": "Non-Existent Visitor"
        }
        response = api_client.patch(f'{self.endpoint}9999999999999999999/', data=patch_data)
        assert response.status_code == 404

    def test_ticket_update_unauthorized(self, api_client, ticket):
        patch_data = {
            "visitor_name": "Unauthorized Visitor Update"
        }
        response = api_client.patch(f'{self.endpoint}{ticket.id}/', data=patch_data)
        assert response.status_code == 401

    def test_ticket_update_forbidden_for_simple_user(self, api_client, simple_user, ticket):
        api_client.force_authenticate(simple_user)
        patch_data = {
            "visitor_name": "Forbidden Visitor Update"
        }
        response = api_client.patch(f'{self.endpoint}{ticket.id}/', data=patch_data)
        assert response.status_code == 403

    def test_ticket_put_update_success(self, api_client, staff_user, ticket):
        api_client.force_authenticate(staff_user)
        put_data = {
            "visitor_name": "Visitor Updated",
            "visitor_email": "updated_visitor@example.com",
            "visitor_message": "Updated ticket text",
            "ticket_status": "new"
        }
        response = api_client.put(f'{self.endpoint}{ticket.id}/', data=put_data, format='json')
        assert response.status_code == 200

    def test_ticket_put_update_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        put_data = {
            "visitor_name": "Non-Existent Visitor"
        }
        response = api_client.put(f'{self.endpoint}9999999999999999999/', data=put_data, format='json')
        assert response.status_code == 404

    def test_ticket_put_update_unauthorized(self, api_client, ticket):
        put_data = {
            "visitor_name": "Unauthorized Visitor Update"
        }
        response = api_client.put(f'{self.endpoint}{ticket.id}/', data=put_data, format='json')
        assert response.status_code == 401

    def test_ticket_put_update_forbidden_for_simple_user(self, api_client, simple_user, ticket):
        api_client.force_authenticate(simple_user)
        put_data = {
            "visitor_name": "Forbidden Visitor Update"
        }
        response = api_client.put(f'{self.endpoint}{ticket.id}/', data=put_data, format='json')
        assert response.status_code == 403

    def test_ticket_delete_success(self, api_client, staff_user, ticket):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}{ticket.id}/')
        assert response.status_code == 204

    def test_ticket_delete_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}9999999999999999999/')
        assert response.status_code == 404

    def test_ticket_delete_unauthorized(self, api_client, ticket):
        response = api_client.delete(f'{self.endpoint}{ticket.id}/')
        assert response.status_code == 401

    def test_ticket_delete_forbidden_for_simple_user(self, api_client, simple_user, ticket):
        api_client.force_authenticate(simple_user)
        response = api_client.delete(f'{self.endpoint}{ticket.id}/')
        assert response.status_code == 403
        
class TestJobTicketEndpoints:
    endpoint = '/api/help/job-tickets/'

    def test_job_ticket_create_success(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        data = {
            "position": "Engineer",
            "first_name": "Alain",
            "last_name": "Bardot",
            "email": "alain@bardot.fr"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201
        assert 'id' in json.loads(response.content)

    def test_job_ticket_create_unauthorized(self, api_client, simple_user):
        api_client.force_authenticate(simple_user)
        data = {
            "position": "Engineer",
            "first_name": "Alain",
            "last_name": "Bardot",
            "email": ""
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 403

    def test_job_ticket_get_success(self, api_client, staff_user, job_ticket):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}{job_ticket.id}/')
        assert response.status_code == 200
        assert json.loads(response.content).get('id') == job_ticket.id

    def test_job_ticket_update_success(self, api_client, staff_user, job_ticket):
        api_client.force_authenticate(staff_user)
        updated_data = {
            "position": "Engineer",
            "first_name": "Alain",
            "last_name": "Bardot",
            "email": "alain@bardot.fr"
        }
        response = api_client.put(f'{self.endpoint}{job_ticket.id}/', data=updated_data, format='json')
        assert response.status_code == 200

    def test_job_ticket_delete_success(self api_client, staff_user):
        api_client.force_authenticate(staff_user)
        response = api_client.delete(f'{self.endpoint}{job_ticket.id}/')
        assert response.status_code == 204

class TestPartnerTicketEndpoints:
    endpoint = '/api/help/partner-tickets/'

    def test_partner_ticket_create_success(self, api_client, admin_user):
        api_client.force_authenticate(admin_user)
        data = {
            "name": "Engineer",
            "business_name": "Bardot SA",
            "email": "ceo@bardot.fr",
            "message": "Invoice Request",
            "url": "http://www.bardot.fr"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201
        assert 'id' in json.loads(response.content)

    def test_partner_ticket_create_unauthorized(self, simple_user, api_client):
        api_client.force_authenticate(simple_user)
        data = {
            "name": "Engineer",
            "business_name": "Bardot SA",
            "email": "",
            "message": "Invoice Request",
            "url": "http://www.bardot.fr"
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 403

    def test_partner_ticket_get_success(self, admin_user, api_client, partner_ticket):
        api_client.force_authenticate(admin_user)
        response = api_client.get(f'{self.endpoint}{partner_ticket.id}/')
        assert response.status_code == 200
        assert json.loads(response.content).get('id') == partner_ticket.id

    def test_partner_ticket_update_success(self, admin_user, api_client, partner_ticket):
        api_client.force_authenticate(admin_user)
        updated_data = {
            "name": "Engineer",
            "business_name": "Bardot SA",
            "email": "ceo@bardot.fr",
            "message": "Invoice Request",
            "url": "http://www.bardot.fr"
        }
        response = api_client.put(f'{self.endpoint}{partner_ticket.id}/', data=updated_data, format='json')
        assert response.status_code == 200

    def test_partner_ticket_delete_success(self, admin_user, api_client, partner_ticket):
        api_client.force_authenticate(admin_user)
        response = api_client.delete(f'{self.endpoint}{partner_ticket.id}/')
        assert response.status_code == 204

