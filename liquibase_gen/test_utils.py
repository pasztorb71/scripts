from unittest import TestCase

import utils


class Test(TestCase):
    def test_get_tablename(self):
        tabname = utils.get_tablename('ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = 'account_info.payment_method'
        self.assertEqual(expected, tabname)

    def test_get_colname(self):
        colname = utils.get_columnname('ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = 'x__version'
        self.assertEqual(expected, colname)
