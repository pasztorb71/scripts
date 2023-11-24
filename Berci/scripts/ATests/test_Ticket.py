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

    def test_branch(self):
        t = Ticket('MLFFDEV-21725')
        self.assertEqual('feature/MLFFDEV-21725_DB_Genos_mustache', t.branch)

    def test_release(self):
        t = Ticket('MLFFDEV-21725')
        self.assertEqual('MLFF 0.19.0', t.release)

    def test_release_missing(self):
        t = Ticket('MLFFDEV-21701')
        self.assertEqual('MLFF 0.17.1', t.release)
