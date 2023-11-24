from unittest import TestCase

from Database import Database
from Table import Table


class Test(TestCase):
    def setUp(self):
        self.db = Database('core_notification_wa')
        self.table = Table('notification_wa.staging_wa', self.db.conn)

    def test_is_check_constraint_on_column(self):
        self.assertTrue(self.table.is_check_constraint_on_column('processing_status'))

    def test_is_check_constraint_on_column_false(self):
        self.assertFalse(self.table.is_check_constraint_on_column('request_id'))

    def test_gen_drop_check_constraint_stmt(self):
        expected = "ALTER TABLE staging_wa DROP CONSTRAINT ck_staging_wa_processing_status;"
        actual = self.table.gen_drop_constraint_stmt('processing_status')
        self.assertEqual(expected, actual)

class Test(TestCase):
    def setUp(self):
        self.db = Database('core_customer')

    def test_is_history_table_exist(self):
        table = Table('customer.customer', self.db.conn)
        self.assertTrue(table.has_history())

    def test_is_history_table_not_exist(self):
        table = Table('customer.user_session', self.db.conn)
        self.assertFalse(table.has_history())

    def test_is_partitioned(self):
        table = Table('customer.customer', self.db.conn)
        self.assertFalse(table.has_partitions())

class Test_eligibility(TestCase):
    def setUp(self):
        self.db = Database('enforcement_eligibility', 5442)

    def test_is_partitioned1(self):
        table = Table('eligibility.detection_data', self.db.conn)
        self.assertTrue(table.has_partitions())
