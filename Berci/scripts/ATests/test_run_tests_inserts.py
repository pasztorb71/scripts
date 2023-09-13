from unittest import TestCase

from Environment import Env


class Test(TestCase):
    def test_get_conn_not_none(self):
        self.assertIsNotNone(Env().get_conn_service_user('payment_account_info'))

    def test_get_conn_none(self):
        self.assertIsNone(Env().get_conn_service_user('payment_account_infooo'))

