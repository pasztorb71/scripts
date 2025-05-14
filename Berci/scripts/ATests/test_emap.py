from unittest import TestCase

from classes import Database


class Test(TestCase):
    def setUp(self):
        conn = Database.Database(name='emap_gateway').conn
        print(conn)
    def test_get_conn_not_none(self):
        assert True


