import pathlib
from unittest import TestCase

import Environment
from utils import utils_sec
from Repository import Repository, get_all_repos, rel_to_num


class TestRepository(TestCase):
    def setUp(self) -> None:
        self.base = 'test_repo\\'

    def test_get_name1(self):
        r = Repository()
        repo = r.find_name('psp-proxy')
        self.assertEqual('mlff-payment-psp-proxy-postgredb', repo)

    def test_get_name_new_base(self):
        r = Repository(base='test_repo')
        repo = r.find_name('analytic')
        self.assertEqual('mlff-core-analytic-postgredb', repo)

    def test_get_db_name1(self):
        r = Repository('mlff-payment-psp-proxy-postgredb')
        self.assertEqual('payment_psp_proxy', r.get_db_name())

    def test_get_db_name2(self):
        r = Repository('doc-postgredb', base=self.base)
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
        self.assertEqual('0.23', Repository('analytic-', base='test_repo/').env_ver)

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
        r = Repository('doc-', base=self.base)
        c = r.get_schema_version_0_lines()
        self.assertEqual(34, len(c))

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
        r = Repository('doc-postgredb', base='test_repo/')
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
        repo = Repository('doc-postgredb', base=self.base)
        expected = f'docker-compose --env-file {self.base}doc-postgredb\\.env -f {self.base}doc-postgredb\\etc\\release\\docker-compose.yml build'
        self.assertEqual(expected, repo.image_build_command)

    def test_get_image_name_with_release(self):
        repo = Repository('doc-postgredb', base=self.base)
        expected = 'dockerhub.icellmobilsoft.hu/liquibase/mlff-document-postgredb:1.8.0'
        self.assertEqual(expected, repo.image_name_with_release)

    def test_get_run_command(self):
        repo = Repository('doc-postgredb', base=self.base)
        password = utils_sec.password_from_file('postgres', Environment.Env('local').get_port_from_repo(repo.name))
        expected = 'docker run --rm --network mlff-local-network -e DB_ADDRESS=gateway.docker.internal ' \
                   f'-e DB_PORT=5432 -e POSTGRES_PASSWORD={password} ' \
                   'dockerhub.icellmobilsoft.hu/liquibase/mlff-document-postgredb:1.8.0'
        self.assertEqual(expected, repo.image_run_command)

    def test_get_run_sh_eol_type(self):
        path = str(pathlib.Path().absolute()) + '/'
        r = Repository('test_repo', base=path)
        self.assertEqual('unix', r.run_sh_eol_type)

    def test_get_repository_from_dbname(self):
        self.assertEqual(Repository('customer').name, Repository.get_repository_name_from_dbname('core_customer'))

    def test_get_repo_from_filename(self):
        file = 'test_repo\\mlff-core-analytic-postgredb\\liquibase\\core_analytic\\analytic\\tables\\plate_number_whitelist\\0002-plate_number_whitelist-create.sql'
        self.assertEqual(Repository('core-analytic').name, Repository.get_repo_from_filename(file).name)

    def test_get_schema_version_0_lines(self):
        file = 'test_repo\\mlff-core-analytic-postgredb\\liquibase\\core_analytic\\analytic\\tables\\plate_number_whitelist\\0002-plate_number_whitelist-create.sql'
        r = Repository.get_repo_from_filename(file)
        actual = len(r.get_schema_version_0_lines())
        expected = 23
        self.assertEqual(expected, actual)

    def test_get_label_of_file_from_schema_version_None(self):
        file = 'test_repo\\mlff-core-analytic-postgredb\\liquibase\\core_analytic\\analytic\\tables\\plate_number_whitelist\\0002-plate_number_whitelist-create.sql'
        repo = Repository.get_repo_from_filename(file)
        self.assertIsNone(repo.get_label_of_file_from_schema_version(file))

    def test_get_label_of_file_from_schema_version(self):
        file = 'test_repo\\mlff-core-customer-postgredb\\liquibase\\core_customer\\customer\\tables\customer\\customer-DDL-014.sql'
        repo = Repository.get_repo_from_filename(file)
        file_name = file.rsplit('\\', 1)[1]
        self.assertIsNotNone(repo.get_label_of_file_from_schema_version(file_name))

