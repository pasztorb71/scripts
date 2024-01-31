from unittest import TestCase

from Environment import Env
from Repository import Repository


class TestEnv(TestCase):
    def test_get_port_from_inst_test(self):
        self.assertEqual(5555, Env('mlff_test').get_port_from_inst(''))

    def test_get_port_from_inst1(self):
        self.assertEqual(5441, Env('sandbox').get_port_from_inst('pg-core'))

    def test_build_list_of_envs_from_databases(self):
        e = Env
        Env.build_list_of_envs_from_databases()
        self.assertEqual(9, len(e.list_of_envs))

    def test_build_list_of_envs_from_databases_local(self):
        e = Env
        Env.build_list_of_envs_from_databases()
        for env in e.list_of_envs:
            if env['env_name'] == 'local':
                break
        self.assertEqual(1, len(env['domains']))

    def test_get_ports_from_env2(self):
        self.assertEqual([5440, 5441, 5442, 5443, 5444, 5445, 5447], Env('sandbox').get_ports())

    def test_get_ports_from_env1(self):
        self.assertEqual([5432], Env('local').get_ports())

    def test_get_port(self):
        self.assertEqual(5544, Env('dev').get_port_from_repo(Repository('account-info').name))

    def test_get_env(self):
        self.assertEqual('cantas_dev', Env.get_env_name_from_port(6041))
