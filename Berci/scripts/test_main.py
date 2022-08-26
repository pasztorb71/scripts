from unittest import TestCase

from liquibase_gen.changelog_generator.tasks import new_enum


class Test(TestCase):
    def test_modify_constraint(self):
        actual = new_enum('dispatcher', 'notification_wa.event', 'event', ['REGISTRATION,PHONE_NUMBER_MODIFICATION,AD_HOC_TICKET_PAYMENT_SUCCESS'])
        self.assertEqual(3, len(actual))
