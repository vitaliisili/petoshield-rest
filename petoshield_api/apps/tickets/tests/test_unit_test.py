class TestTicketUnitTest:
    def test_ticket_string_representation(self, ticket):
        assert str(ticket) == f'Ticket|{ticket.id}|{ticket.visitor_message[:50]}'
