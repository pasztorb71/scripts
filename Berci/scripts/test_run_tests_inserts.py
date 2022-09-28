from unittest import TestCase

from Repository import get_conn_service_user


class Test(TestCase):
    def test_get_conn_not_none(self):
        self.assertIsNotNone(get_conn_service_user('local', 'payment_account_info'))

    def test_get_conn_none(self):
        self.assertIsNone(get_conn_service_user('local', 'payment_account_infooo'))

