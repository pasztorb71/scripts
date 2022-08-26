from unittest import TestCase

from table import Table


class Test(TestCase):
    def test_is_check_constraint_on_column(self):
        t = Table('localhost', 5433, 'notification_wa.event')

        self.fail()


