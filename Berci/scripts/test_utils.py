import os
from unittest import TestCase

import Database
import Environment
import utils
import utils_command
import utils_file
import utils_sec
from Repository import Repository
from utils import get_atlassian_login_from_file


class Test(TestCase):
    def test_get_login_from_file(self):
        self.assertEqual('bertalan.pasztor@icellmobilsoft.hu', get_atlassian_login_from_file()[0])

    def test_get_tablename(self):
        tabname = utils_command.get_tablename_from_command('',
                                                           'ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = 'payment_method'
        self.assertEqual(expected, tabname)

    def test_get_colname(self):
        colname = utils_command.get_columnname_from_command(
                'ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = 'x__version'
        self.assertEqual(expected, colname)

    def test_password_from_file1(self):
        self.assertEqual('mlffTitkosPassword123!',
                         utils_sec.password_from_file('notification_wa_service', 'localhost', 5433))

    def test_password_from_file2(self):
        self.assertEqual('mysecretpassword', utils_sec.password_from_file('postgres', 5432))

    def test_password_from_file3(self):
        self.assertEqual('mysecretpassword', utils_sec.password_from_file('postgres', 5432))

    def test_password_from_file_service(self):
        self.assertEqual('mlffTitkosPassword123!', utils_sec.password_from_file('detection_service', 5437))

    def test_password_from_file_all_hosts(self):
        self.assertEqual('mlffTitkosPassword123!', utils_sec.password_from_file('dwh_read', '*'))

    def test_password_from_file_all_hosts_stream(self):
        self.assertEqual('mlffTitkosPassword123!', utils_sec.password_from_file('dwh_stream', '*'))

    def test_get_schema_from_command(self):
        actual = utils_command.get_schema_from_command(
                "ALTER SCHEMA notification_common RENAME TO notification_dispacther;")
        self.assertEqual('notification_common', actual)

    def test_append_to_file_after_line_last_occurence_after_exists(self):
        fname = "c:/tmp/testfile.txt"
        with open(fname, 'w', encoding='utf-8') as f:
            f.write("""<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

    <!-- =================================================================================== -->
    <!-- A schema-hoz tartozó táblák létrehozása...                                          -->
    <!-- Részlegesen kötött sorrendben kell futtatni, a Foreign Key hivatkozások miatt!      -->
    <!-- =================================================================================== -->

    <include file="trip/trip.sql" relativeToChangelogFile="true"/>

</databaseChangeLog>
""")
        utils_file.append_to_file_after_line_last_occurence(fname, '    <include file=', '		testline')
        expected = """<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

    <!-- =================================================================================== -->
    <!-- A schema-hoz tartozó táblák létrehozása...                                          -->
    <!-- Részlegesen kötött sorrendben kell futtatni, a Foreign Key hivatkozások miatt!      -->
    <!-- =================================================================================== -->

    <include file="trip/trip.sql" relativeToChangelogFile="true"/>
		testline

</databaseChangeLog>
"""
        with open(fname, 'r', encoding='utf-8') as f:
            value = f.read()
        self.assertEqual(expected, value)

    def test_append_to_file_after_line_last_occurence_after_not_exists(self):
        fname = "c:/tmp/testfile.txt"
        with open(fname, 'w', encoding='utf-8') as f:
            f.write("""<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

    <!-- =================================================================================== -->
    <!-- A schema-hoz tartozó táblák létrehozása...                                          -->
    <!-- Részlegesen kötött sorrendben kell futtatni, a Foreign Key hivatkozások miatt!      -->
    <!-- =================================================================================== -->


</databaseChangeLog>
""")
        utils_file.append_to_file_after_line_last_occurence(fname, '    <include file=', '		testline')
        expected = """<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

    <!-- =================================================================================== -->
    <!-- A schema-hoz tartozó táblák létrehozása...                                          -->
    <!-- Részlegesen kötött sorrendben kell futtatni, a Foreign Key hivatkozások miatt!      -->
    <!-- =================================================================================== -->

		testline

</databaseChangeLog>
"""
        with open(fname, 'r', encoding='utf-8') as f:
            value = f.read()
        self.assertEqual(expected, value)

    def test_get_tablename_from_command1(self):
        command = "CREATE INDEX ix_trip_cust_id ON trip.trip USING btree (customer_id);"
        self.assertEqual('trip', utils_command.get_tablename_from_command(command))

    def test_get_tablename_from_command1(self):
        command = "CREATE INDEX ix_trip_cust_id ON trip.trip USING btree (customer_id);"
        self.assertEqual('trip', utils_command.get_tablename_from_command('', command))

    def test_get_indexname_from_command(self):
        index = utils_command.get_indexname_from_command(
                "ALTER INDEX tariff.ix_segsec_glied_id RENAME TO ix_section_glied_id;")
        self.assertEqual('ix_segsec_glied_id', index)

    def test_get_port(self):
        self.assertEqual(5544, Environment.Env('dev').get_port_from_repo(Repository('account-info').name))

    def test_get_instance_from_db_name(self):
        self.assertEqual('pg-doc', utils.get_instance_from_db_name('doc_document'))

    def test_get_ports_from_env1(self):
        self.assertEqual([5432], Environment.Env('local').get_ports())

    def test_get_ports_from_env2(self):
        self.assertEqual([5440, 5441, 5442, 5443, 5444, 5445, 5447], Environment.Env('sandbox').get_ports())

    def test_get_env(self):
        self.assertEqual('cantas_dev', Environment.Env.get_env_name_from_port(6041))


def test_get_port_from_env_inst():
    assert False
