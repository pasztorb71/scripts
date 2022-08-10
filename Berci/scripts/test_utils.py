from unittest import TestCase

import utils
from utils import get_login_from_file


class Test(TestCase):
    def test_get_login_from_file(self):
        self.assertEqual(get_login_from_file()[0], 'bertalan.pasztor')

    def test_is_history_table_exist(self):
        self.assertTrue(utils.has_history_table('core_customer', 'customer', 'customer'))

    def test_is_history_table_not_exist(self):
        self.assertFalse(utils.has_history_table('core_customer', 'customer', 'user_session'))

    def test_get_tablename(self):
        tabname = utils.get_tablename_from_command('ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = 'payment_method'
        self.assertEqual(expected, tabname)

    def test_get_colname(self):
        colname = utils.get_columnname_from_command('ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = 'x__version'
        self.assertEqual(expected, colname)

    def test_password_from_file(self):
        self.assertEqual('fLXyFS0RpmIX9uxGII4N', utils.password_from_file('localhost', 5433))

    def test_password_from_file1(self):
        self.assertEqual('mysecretpassword', utils.password_from_file('localhost', 5432))
