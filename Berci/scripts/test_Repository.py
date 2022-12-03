from unittest import TestCase

from Repository import Repository


class TestRepository(TestCase):
    def test_get_name1(self):
        r = Repository()
        repo = r.find_name('psp-proxy')
        self.assertEqual('mlff-payment-psp-proxy-postgredb', repo)

    def test_get_name2(self):
        r = Repository()
        with self.assertRaises(Exception) as e:
            repo = r.find_name('enforcement')
        self.assertEqual("Nem egyértelmű a repository név!", str(e.exception))

    def test_get_db_name(self):
        r = Repository('mlff-payment-psp-proxy-postgredb')
        self.assertEqual('payment_psp_proxy', r.get_db_name())

    def test_is_table_file_exists_true(self):
        repo = Repository('trip-postg')
        self.assertTrue(repo.is_table_file_exists('trip'))

    def test_is_table_file_exists_false(self):
        repo = Repository('trip-postgr')
        self.assertFalse(repo.is_table_file_exists('triptmp'))

    def test_get_tablename_from_indexname(self):
        repo = Repository('customer')
        value = repo.get_tablename_from_indexname('customer.ix_cust_custname')
        self.assertEqual('customer', value)

    def test_get_db_names_by_group(self):
        actual = Repository.get_db_names_by_group('K-Team')
        expected = ['enforcement_eligibility', 'enforcement_onsite_alert_subscribe']
        self.assertListEqual(expected, actual)

    def test_env_ver(self):
        self.assertEqual('0.11', Repository('transit').env_ver)

    def test_get_schema1(self):
        r = Repository('mlff-core-customer-postgredb')
        self.assertEqual('customer', r.get_schema())

    def test_get_schema2(self):
        r = Repository('mlff-enforcement-onsite-alert-subscribe-postgredb')
        self.assertEqual('subscribe', r.get_schema())

    def test_get_schema3(self):
        r = Repository('detection-alert')
        self.assertEqual('detection_alert', r.get_schema())

    def test_get_schema_version_content(self):
        r = Repository('-pn')
        c = r.get_schema_version_label_lines()
        self.assertTrue(len(c.splitlines()) == 0)

    def test_get_tables_dir1(self):
        r = Repository('customer')
        tabdir = 'c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/customer/tables'
        self.assertEqual(tabdir, r.get_tables_dir())

    def test_get_tables_dir2(self):
        r = Repository('detection-alert')
        tabdir = 'c:/GIT/MLFF/mlff-enforcement-detection-alert-postgredb/liquibase/enforcement_detection_alert/detection_alert/tables'
        self.assertEqual(tabdir, r.get_tables_dir())

    def test_last_component_ver(self):
        r = Repository('mlff-core-notification-wa-postgredb')
        self.assertEqual('0.10', r.last_component_ver)
