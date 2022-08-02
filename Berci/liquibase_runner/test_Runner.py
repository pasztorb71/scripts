from unittest import TestCase
from Runner import Runner

class TestRunner(TestCase):
    def setUp(self) :
        base = 'c:/GIT/MLFF/'
        self.runner = Runner(base, 'fLXyFS0RpmIX9uxGII4N')
    def test_get_dbs(self):
        self.assertListEqual(self.runner.get_dbs('mlff-core-customer-postgredb'), ['core_customer'])
    def test_get_dbs1(self):
        self.assertListEqual(self.runner.get_dbs('mlff-core-notification-postgredb'),
                             ['core_notification_common', 'core_notification_email', 'core_notification_pn', 'core_notification_wa'])

    def test_kill(self):
        self.fail()