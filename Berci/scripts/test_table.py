from unittest import TestCase

from table import Table


class Test(TestCase):
    def setUp(self):
        self.table = Table('local', 'core_notification_wa', 'notification_wa.staging')

    def test_is_check_constraint_on_column(self):
        self.assertTrue(self.table.is_check_constraint_on_column('staging_status'))

    def test_is_check_constraint_on_column_false(self):
        self.assertFalse(self.table.is_check_constraint_on_column('request_id'))

    def test_gen_drop_check_constraint_stmt(self):
        expected = "ALTER TABLE staging DROP CONSTRAINT ck_staging_staging_status;"
        actual = self.table.gen_drop_constraint_stmt('staging_status')
        self.assertEqual(expected, actual)
