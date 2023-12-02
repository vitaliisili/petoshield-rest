class TestTicketUnitTest:
    def test_ticket_string_representation(self, ticket):
        assert str(ticket) == f'Ticket|{ticket.id}|{ticket.visitor_message[:50]}'


class TestPartnerTicketUnitTest:
    def test_partner_ticket_string_representation(self, partner_ticket):
        assert str(partner_ticket) == partner_ticket.business_name


class TestJobTicketUnitTest:
    def test_job_ticket_string_representation(self, job_ticket):
        assert str(job_ticket) == job_ticket.position
