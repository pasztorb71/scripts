from unittest import TestCase

from liquibase_gen.changelog_generator.tasks import new_enum


class Test(TestCase):
    def test_new_enum(self):
        res = new_enum('customer.customer', 'customer_status', 'TESZT')
        self.assertEqual(3, len(res))
