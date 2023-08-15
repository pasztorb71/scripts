from unittest import TestCase

from table import Table


class Test(TestCase):
    def setUp(self):
        self.table = Table('local', 'core_notification_wa', 'notification_wa.staging_wa')

    def test_is_check_constraint_on_column(self):
        self.assertTrue(self.table.is_check_constraint_on_column('processing_status'))

    def test_is_check_constraint_on_column_false(self):
        self.assertFalse(self.table.is_check_constraint_on_column('request_id'))

    def test_gen_drop_check_constraint_stmt(self):
        expected = "ALTER TABLE staging_wa DROP CONSTRAINT ck_staging_wa_processing_status;"
        actual = self.table.gen_drop_constraint_stmt('processing_status')
        self.assertEqual(expected, actual)

    def test_getfklist(self):
        t = Table('local', 'core_customer', 'customer.customer_outbox')
        a = t.getfklist()
        self.assertEqual(1, len(t.getfklist())
)
