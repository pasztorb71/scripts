from unittest import TestCase

from run_liquibase import get_dbs


class Test(TestCase):
    def test_get_dbs(self):
        self.assertListEqual(get_dbs('core-postgredb'), ['core_customer'])
    def test_get_dbs1(self):
        self.assertListEqual(get_dbs('notification-postgredb'),
                             ['core_notification_common', 'core_notification_email', 'core_notification_pn', 'core_notification_wa'])
