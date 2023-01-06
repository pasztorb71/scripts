from unittest import TestCase

from atszervezesek.Adatmigracio import is_database_in_instance


class Test(TestCase):
    def test_is_database_in_instance1(self):
        self.assertTrue(is_database_in_instance('document', 'pg-doc'))

    def test_is_database_in_instance2(self):
        self.assertTrue(is_database_in_instance('core_genos', 'pg-core-mqid'))
