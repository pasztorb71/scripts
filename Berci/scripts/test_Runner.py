from unittest import TestCase

from Repository import Repository
from liquibase_runner.Runner import Runner
from utils import get_ip_addresses_for_docker


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

    def test_get_ip_addresses_for_docker1(self):
        self.assertEqual('gateway.docker.internal:5434', get_ip_addresses_for_docker('mlff-core-customer-postgredb', 'dev'))

    def test_get_ip_addresses_for_docker_new_instances1(self):
        self.assertEqual('gateway.docker.internal:5641', get_ip_addresses_for_docker('mlff-core-customer-postgredb','new_fit'))


