from unittest import TestCase

import Repository


class Test(TestCase):
    def test_get_label_in_file(self):
        file = 'test-repo\\mlff-core-analytic-postgredb\\liquibase\\core_analytic\\analytic\\tables\\plate_number_whitelist\\0002-plate_number_whitelist-create.sql'
        self.assertEqual('R0.21', Repository.Repository.get_release_label_release_of_file(file))

    def test_get_label_in_xml(self):
        file = 'test-repo\\mlff-core-customer-postgredb\\liquibase\\core_customer\\customer\\tables\customer\\0035-customer$hist-DDL.sql'
        self.assertEqual('R0.22', Repository.Repository.get_release_label_release_of_file(file))
