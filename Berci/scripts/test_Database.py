from unittest import TestCase

from Database import Database


class TestDatabase(TestCase):
    def test_is_history_table_exist(self):
        self.assertTrue(Database('core_customer').has_history_table('customer', 'customer'))

    def test_is_history_table_not_exist(self):
        self.assertFalse(Database('core_customer').has_history_table('customer', 'user_session'))

