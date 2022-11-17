from unittest import TestCase

from Ticket import Ticket


class TestTicket(TestCase):
    def test_get_version(self):
        ticket = Ticket('MLFFDEV-7086')
        version = ticket.get_version()
        self.assertEqual('0.09.0', version)

    def test_get_version_newformat(self):
        ticket = Ticket('MLFFDEV-6438')
        version = ticket.get_version()
        self.assertEqual('0.09.0', version)

