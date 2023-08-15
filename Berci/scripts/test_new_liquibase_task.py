from unittest import TestCase
from Ticket import Ticket

class Test(TestCase):
    def test_read_ticket_title(self):
        t = Ticket(f'MLFFDEV-22109')
        self.assertTrue(':' not in t.branch)
