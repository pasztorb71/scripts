from unittest import TestCase

from Environment import Env


class TestEnv(TestCase):
    def test_get_port_from_inst_test(self):
        self.assertEqual(5555, Env('mlff_test').get_port_from_inst(''))

    def test_get_port_from_inst1(self):
        self.assertEqual(5441, Env('sandbox').get_port_from_inst('pg-core'))
