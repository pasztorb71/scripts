from unittest import TestCase

import Environment
from utils import utils_sec
from Repository import Repository, get_all_repos, rel_to_num


class TestRepository(TestCase):
    def test_get_name1(self):
        r = Repository()
        repo = r.find_name('psp-proxy')
        self.assertEqual('mlff-payment-psp-proxy-postgredb', repo)

    def test_get_db_name1(self):
        r = Repository('mlff-payment-psp-proxy-postgredb')
        self.assertEqual('payment_psp_proxy', r.get_db_name())

    def test_get_db_name2(self):
        r = Repository('doc-postgredb')
        self.assertEqual('doc_document', r.get_db_name())

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
        self.assertEqual(6, len(actual))

    def test_env_ver(self):
        self.assertEqual('1.8', Repository('doc-').env_ver)

    def test_get_schema1(self):
        r = Repository('mlff-core-customer-postgredb')
        self.assertEqual('customer', r.get_schema())

    def test_get_schema2(self):
        r = Repository('mlff-enforcement-onsite-alert-subscribe-postgredb')
        self.assertEqual('onsite_alert_subscribe', r.get_schema())

    def test_get_schema3(self):
        r = Repository('detection-alert')
        self.assertEqual('detection_alert', r.get_schema())

    def test_get_schema4(self):
        r = Repository('eligibility')
        self.assertEqual('eligibility', r.get_schema())

    def test_get_schema_version_content(self):
        r = Repository('doc-')
        c = r.get_schema_version_label_lines()
        self.assertEqual(4, len(c.splitlines()))

    def test_get_tables_dir1(self):
        r = Repository('customer')
        tabdir = 'c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/customer/tables'
        self.assertEqual(tabdir, r.get_tables_dir())

    def test_get_tables_dir2(self):
        r = Repository('detection-alert')
        tabdir = 'c:/GIT/MLFF/mlff-enforcement-detection-alert-postgredb/liquibase/enforcement_detection_alert/detection_alert/tables'
        self.assertEqual(tabdir, r.get_tables_dir())

    def test_get_tables_dir3(self):
        r = Repository('eligibility')
        tabdir = 'c:/GIT/MLFF/mlff-enforcement-eligibility-postgredb/liquibase/enforcement_eligibility/eligibility/tables'
        self.assertEqual(tabdir, r.get_tables_dir())

    def test_get_tables_dir4(self):
        r = Repository('mlff-enforcement-onsite-inspection-postgredb')
        tabdir = 'c:/GIT/MLFF/mlff-enforcement-onsite-inspection-postgredb/liquibase/enforcement_onsite_inspection/onsite_inspection/tables'
        self.assertEqual(tabdir, r.get_tables_dir())

    def test_max_rel_to_num(self):
        self.assertEqual(0.14, rel_to_num('R0.14'))

    def test_max_rel_to_num_bugfix(self):
        self.assertEqual(0.14, rel_to_num('R0.14.1'))

    def test_last_component_ver(self):
        r = Repository('doc-postgredb')
        self.assertEqual(['1.8', 'R0.16.1'], r.last_component_ver())

    def test_last_component_ver_relfilter(self):
        r = Repository('mlff-core-genos-postgredb')
        self.assertEqual(['0.8', 'R0.18'], r.last_component_ver('R0.18'))

    def test_last_component_ver_relfilter_lessthan(self):
        r = Repository('mlff-core-notification-email-postgredb')
        self.assertEqual(['0.5', 'R0.14'], r.last_component_ver('R0.18'))

    def test_get_all_repos(self):
        self.assertTrue(len(get_all_repos()) > 0)

    def test_get_build_command(self):
        repo = Repository('doc-postgredb')
        expected = 'docker-compose --env-file c:\\GIT\\MLFF\\doc-postgredb\\.env -f c:\\GIT\\MLFF\\doc-postgredb\\etc\\release\\docker-compose.yml build'
        self.assertEqual(expected, repo.image_build_command)

    def test_get_image_name_with_release(self):
        repo = Repository('doc-postgredb')
        expected = 'dockerhub.icellmobilsoft.hu/liquibase/mlff-document-postgredb:1.8.0'
        self.assertEqual(expected, repo.image_name_with_release)

    def test_get_run_command(self):
        repo = Repository('doc-postgredb')
        password = utils_sec.password_from_file('postgres', Environment.Env('local').get_port_from_repo(repo.name))
        expected = 'docker run --rm --network mlff-local-network -e DB_ADDRESS=gateway.docker.internal ' \
                   f'-e DB_PORT=5432 -e POSTGRES_PASSWORD={password} ' \
                   'dockerhub.icellmobilsoft.hu/liquibase/mlff-document-postgredb:1.8.0'
        self.assertEqual(expected, repo.image_run_command)

