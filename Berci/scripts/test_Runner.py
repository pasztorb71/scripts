from unittest import TestCase

from Repository import Repository
from liquibase_runner.Runner import Runner


class TestRunner(TestCase):
    def setUp(self):
        self.runner = Runner(Repository().get_base())

    def test_get_dbs(self):
        self.assertListEqual(self.runner.get_dbs('mlff-core-customer-postgredb'), ['core_customer'])

    def test_get_dbs1(self):
        self.assertListEqual(self.runner.get_dbs('doc-postgredb'),
                             ['document', ])

    def test_kill(self):
        pass

    def test_get_ip_addresses_for_docker(self):
        self.assertListEqual(['gateway.docker.internal'], self.runner.get_ip_addresses_for_docker('local'))

    def test_get_ip_addresses_for_docker1(self):
        self.assertListEqual(['gateway.docker.internal:5433', 'gateway.docker.internal:5434'], self.runner.get_ip_addresses_for_docker('remote'))
