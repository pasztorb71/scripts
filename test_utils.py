from unittest import TestCase

import utils
from utils import get_login_from_file


class Test(TestCase):
    def test_get_login_from_file(self):
        self.assertEqual(get_login_from_file()[0], 'bertalan.pasztor')

    def test_is_history_table_exist(self):
        self.assertTrue(utils.is_history_table('core_customer','customer','customer'))

    def test_is_history_table_not_exist(self):
        self.assertFalse(utils.is_history_table('core_customer','customer','user_session'))


