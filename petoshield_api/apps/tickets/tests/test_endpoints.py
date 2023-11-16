import pytest

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
        
