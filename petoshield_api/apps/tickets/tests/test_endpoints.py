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

    @pytest.mark.django_db
    def test_job_ticket_create_success(self, api_client):
        data = {'position': 'test position name',
                'first_name': 'test-name',
                'last_name': 'test-last',
                'email': 'example@mail.com'}
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    @pytest.mark.parametrize('position, first_name, last_name, email', [
        ('', 'first', 'last', 'example@mail.com'),
        (' ', 'first', 'last', 'example@mail.com'),
        ('position', '', 'last', 'example@mail.com'),
        ('position', ' ', 'last', 'example@mail.com'),
        ('position', 'first', '', 'example@mail.com'),
        ('position', 'first', ' ', 'example@mail.com'),
        ('position', 'first', 'last', ''),
        ('position', 'first', 'last', ' '),
        ('position', 'first', 'last', '@mail.com'),
        ('position', 'first', 'last', 'A@b@c@example.com'),
        ('position', 'first', 'last', 'a"b(c)d,e:f;g<h>i[j\k]l@example.com'),
        ('position', 'first', 'last', 'just"not"right@example.com'),
        ('position', 'first', 'last', 'this\ still\"notallowed@example.com'),
    ])
    def test_job_ticket_create_bad_request(self, api_client, first_name, position, last_name, email):
        data = {'position': position,
                'first_name': first_name,
                'last_name': last_name,
                'email': email}
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 400

    def test_job_ticket_list_with_staff_user_success(self, staff_user, api_client, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(job_ticket_list)

    def test_job_ticket_list_with_simple_user_unauthorized(self, simple_user, api_client, job_ticket_list):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_job_ticket_list_with_provider_user_unauthorized(self, provider_user, api_client, job_ticket_list):
        api_client.force_authenticate(provider_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_job_ticket_list_with_anonymous_user_unauthorized(self, api_client, job_ticket_list):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    @pytest.mark.parametrize('page, size, count', [
        (1, 2, 2),
        (2, 2, 1),
        (1, 3, 3),
    ])
    def test_job_ticket_list_pagination_with_staff_user_success(self, api_client,
                                                                staff_user,
                                                                job_ticket_list,
                                                                page, size, count):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size={size}')
        assert response.status_code == 200
        assert len(json.loads(response.content).get('results')) == count

    @pytest.mark.parametrize('page, size', [
        (-1, 2),
        (2, -2),
    ])
    def test_job_ticket_list_pagination_not_found(self, api_client, staff_user, job_ticket_list, page, size):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size={size}')
        assert response.status_code == 404

    def test_job_ticket_put_success(self, api_client, staff_user, job_ticket):
        api_client.force_authenticate(staff_user)
        data = {'position': 'put position name',
                'first_name': 'put-name',
                'last_name': 'put-last',
                'email': 'put@mail.com'}
        response = api_client.put(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_job_ticket_put_with_simple_user_unauthorized(self, api_client, simple_user, job_ticket):
        api_client.force_authenticate(simple_user)
        data = {'position': 'put position name',
                'first_name': 'put-name',
                'last_name': 'put-last',
                'email': 'put@mail.com'}
        response = api_client.put(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_job_ticket_put_with_provider_user_unauthorized(self, api_client, provider_user, job_ticket):
        api_client.force_authenticate(provider_user)
        data = {'position': 'put position name',
                'first_name': 'put-name',
                'last_name': 'put-last',
                'email': 'put@mail.com'}
        response = api_client.put(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_job_ticket_put_with_anonymous_unauthorized(self, api_client, job_ticket):
        data = {'position': 'put position name',
                'first_name': 'put-name',
                'last_name': 'put-last',
                'email': 'put@mail.com'}
        response = api_client.put(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 401

    def test_job_ticket_put_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        data = {'position': 'put position name',
                'first_name': 'put-name',
                'last_name': 'put-last',
                'email': 'put@mail.com'}
        response = api_client.put(f'{self.endpoint}999999/', data=data, format='json')
        assert response.status_code == 404

    def test_job_ticket_patch_success(self, api_client, staff_user, job_ticket):
        api_client.force_authenticate(staff_user)
        data = {'position': 'patch position name'}
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_job_ticket_patch_with_simple_user_unauthorized(self, api_client, simple_user, job_ticket):
        api_client.force_authenticate(simple_user)
        data = {'position': 'patch position name'}
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_job_ticket_patch_with_provider_user_unauthorized(self, api_client, provider_user, job_ticket):
        api_client.force_authenticate(provider_user)
        data = {'position': 'patch position name'}
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_job_ticket_patch_with_anonymous_unauthorized(self, api_client, job_ticket):
        data = {'position': 'patch position name'}
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/', data=data, format='json')
        assert response.status_code == 401

    def test_job_ticket_patch_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        data = {'position': 'patch position name'}
        response = api_client.patch(f'{self.endpoint}999999/', data=data, format='json')
        assert response.status_code == 404

    def test_job_ticket_delete_success(self, api_client, staff_user, job_ticket):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/')
        assert response.status_code == 200

    def test_job_ticket_delete_with_simple_user_unauthorized(self, api_client, simple_user, job_ticket):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/')
        assert response.status_code == 403

    def test_job_ticket_delete_with_provider_user_unauthorized(self, api_client, provider_user, job_ticket):
        api_client.force_authenticate(provider_user)
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/')
        assert response.status_code == 403

    def test_job_ticket_delete_with_anonymous_unauthorized(self, api_client, job_ticket):
        response = api_client.patch(f'{self.endpoint}{job_ticket.id}/')
        assert response.status_code == 401

    def test_job_ticket_delete_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}999999/')
        assert response.status_code == 404

    @pytest.mark.parametrize('position, count', [
        ('developer', 2),
        ('insurance', 1),
        ('notexist', 0),
        ('er', 3),
    ])
    def test_job_ticket_search_by_position_success(self, api_client, staff_user, position, count, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?search={position}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == count

    def test_job_ticket_filter_by_last_name(self, api_client, staff_user, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?last_name={job_ticket_list[0].last_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_job_ticket_filter_by_last_name_not_exist(self, api_client, staff_user, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?last_name=notexist')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    def test_job_ticket_filter_by_first_name(self, api_client, staff_user, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?first_name={job_ticket_list[0].first_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_job_ticket_filter_by_first_name_not_exist(self, api_client, staff_user, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?first_name=notexist')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    def test_job_ticket_filter_by_email(self, api_client, staff_user, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?email={job_ticket_list[0].email}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_job_ticket_filter_by_email_not_exist(self, api_client, staff_user, job_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?email=notexist@mail.com')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0


class TestPartnerTicketEndpoints:
    endpoint = '/api/help/partner-tickets/'

    @pytest.mark.django_db
    def test_partner_ticket_create_success(self, api_client):
        data = {'name': 'test name',
                'business_name': 'test business name',
                'message': 'test message',
                'email': 'example@mail.com',
                'url': 'https://example.com'}
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    @pytest.mark.parametrize('name, business_name, message, email, url', [
        ('', 'business', 'message', 'example@mail.com', 'https://example.com'),
        (' ', 'business', 'message', 'example@mail.com', 'https://example.com'),
        ('name', '', 'message', 'example@mail.com', 'https://example.com'),
        ('name', ' ', 'message', 'example@mail.com', 'https://example.com'),
        ('name', 'business', '', 'example@mail.com', 'https://example.com'),
        ('name', 'business', ' ', 'example@mail.com', 'https://example.com'),
        ('name', 'business', 'message', '', 'https://example.com'),
        ('name', 'business', 'message', ' ', 'https://example.com'),
        ('name', 'business', 'message', 'example@mail.com', ''),
        ('name', 'business', 'message', 'example@mail.com', ' '),
        ('name', 'business', 'message', '@mail.com', 'https://example.com'),
        ('name', 'business', 'message', 'A@b@c@example.com', 'https://example.com'),
        ('name', 'business', 'message', 'a"b(c)d,e:f;g<h>i[j\k]l@example.com', 'https://example.com'),
        ('name', 'business', 'message', 'ust"not"right@example.com', 'https://example.com'),
        ('name', 'business', 'message', 'his is"not\allowed@example.com', 'https://example.com'),
        ('name', 'business', 'message', 'his\ still\"notallowed@example.com', 'https://example.com'),
        ('name', 'business', 'message', 'example@mail.com', 'htt://example.com'),
        ('name', 'business', 'message', 'example@mail.com', 'example.com'),
        ('name', 'business', 'message', 'example@mail.com', 'example'),
    ])
    def test_partner_ticket_create_bad_request(self, api_client, name, business_name, message, email, url):
        data = {'name': name,
                'business_name': business_name,
                'message': message,
                'email': email,
                'url': url}
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 400

    def test_partner_ticket_list_with_staff_user_success(self, staff_user, api_client, partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == len(partner_ticket_list)

    def test_partner_ticket_list_with_simple_user_unauthorized(self, simple_user, api_client, partner_ticket_list):
        api_client.force_authenticate(simple_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_partner_ticket_list_with_provider_user_unauthorized(self, provider_user, api_client, partner_ticket_list):
        api_client.force_authenticate(provider_user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 403

    def test_partner_ticket_list_with_anonymous_user_unauthorized(self, api_client, partner_ticket_list):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    @pytest.mark.parametrize('page, size, count', [
        (1, 2, 2),
        (2, 2, 1),
        (1, 3, 3),
    ])
    def test_partner_ticket_list_pagination_with_staff_user_success(self, api_client,
                                                                    staff_user,
                                                                    partner_ticket_list,
                                                                    page, size, count):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size={size}')
        assert response.status_code == 200
        assert len(json.loads(response.content).get('results')) == count

    @pytest.mark.parametrize('page, size', [
        (-1, 2),
        (2, -2),
    ])
    def test_partner_ticket_list_pagination_not_found(self, api_client, staff_user, partner_ticket_list, page, size):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?page={page}&page_size={size}')
        assert response.status_code == 404

    def test_partner_ticket_put_success(self, api_client, staff_user, partner_ticket):
        api_client.force_authenticate(staff_user)
        data = {'name': 'test name',
                'business_name': 'test business name',
                'message': 'test message',
                'email': 'example@mail.com',
                'url': 'https://example.com'}
        response = api_client.put(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_partner_ticket_put_with_simple_user_unauthorized(self, api_client, simple_user, partner_ticket):
        api_client.force_authenticate(simple_user)
        data = {'name': 'test name',
                'business_name': 'test business name',
                'message': 'test message',
                'email': 'example@mail.com',
                'url': 'https://example.com'}
        response = api_client.put(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_partner_ticket_put_with_provider_user_unauthorized(self, api_client, provider_user, partner_ticket):
        api_client.force_authenticate(provider_user)
        data = {'name': 'test name',
                'business_name': 'test business name',
                'message': 'test message',
                'email': 'example@mail.com',
                'url': 'https://example.com'}
        response = api_client.put(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_partner_ticket_put_with_anonymous_unauthorized(self, api_client, partner_ticket):
        data = {'name': 'test name',
                'business_name': 'test business name',
                'message': 'test message',
                'email': 'example@mail.com',
                'url': 'https://example.com'}
        response = api_client.put(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 401

    def test_partner_ticket_put_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        data = {'name': 'test name',
                'business_name': 'test business name',
                'message': 'test message',
                'email': 'example@mail.com',
                'url': 'https://example.com'}
        response = api_client.put(f'{self.endpoint}999999/', data=data, format='json')
        assert response.status_code == 404

    def test_partner_ticket_patch_success(self, api_client, staff_user, partner_ticket):
        api_client.force_authenticate(staff_user)
        data = {'name': 'patch name'}
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_partner_ticket_patch_with_simple_user_unauthorized(self, api_client, simple_user, partner_ticket):
        api_client.force_authenticate(simple_user)
        data = {'name': 'patch name'}
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_partner_ticket_patch_with_provider_user_unauthorized(self, api_client, provider_user, partner_ticket):
        api_client.force_authenticate(provider_user)
        data = {'name': 'patch name'}
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 403

    def test_partner_ticket_patch_with_anonymous_unauthorized(self, api_client, partner_ticket):
        data = {'name': 'patch name'}
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/', data=data, format='json')
        assert response.status_code == 401

    def test_partner_ticket_patch_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        data = {'name': 'patch name'}
        response = api_client.patch(f'{self.endpoint}999999/', data=data, format='json')
        assert response.status_code == 404

    def test_partner_ticket_delete_success(self, api_client, staff_user, partner_ticket):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/')
        assert response.status_code == 200

    def test_partner_ticket_delete_with_simple_user_unauthorized(self, api_client, simple_user, partner_ticket):
        api_client.force_authenticate(simple_user)
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/')
        assert response.status_code == 403

    def test_partner_ticket_delete_with_provider_user_unauthorized(self, api_client, provider_user, partner_ticket):
        api_client.force_authenticate(provider_user)
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/')
        assert response.status_code == 403

    def test_partner_ticket_delete_with_anonymous_unauthorized(self, api_client, partner_ticket):
        response = api_client.patch(f'{self.endpoint}{partner_ticket.id}/')
        assert response.status_code == 401

    def test_partner_ticket_delete_not_found(self, api_client, staff_user):
        api_client.force_authenticate(staff_user)
        response = api_client.patch(f'{self.endpoint}999999/')
        assert response.status_code == 404

    @pytest.mark.parametrize('business_name, count', [
        ('lina morex gbh', 1),
        ('gbh', 3),
        ('company', 2),
        ('sisters', 1),
    ])
    def test_partner_ticket_search_by_business_name_success(self, api_client, staff_user,
                                                            business_name, count,
                                                            partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?search={business_name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == count

    def test_partner_ticket_filter_by_name(self, api_client, staff_user, partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name={partner_ticket_list[0].name}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_partner_ticket_filter_by_name_not_exist(self, api_client, staff_user, partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?name=notexist')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    def test_partner_ticket_filter_by_url(self, api_client, staff_user, partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?url={partner_ticket_list[0].url}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_partner_ticket_filter_by_url_not_exist(self, api_client, staff_user, partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?url=notexist')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    def test_partner_ticket_filter_by_email(self, api_client, staff_user, partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?email={partner_ticket_list[0].email}')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_partner_ticket_filter_by_email_not_exist(self, api_client, staff_user, partner_ticket_list):
        api_client.force_authenticate(staff_user)
        response = api_client.get(f'{self.endpoint}?email=notexist@mail.com')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0
