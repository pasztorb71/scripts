from unittest import TestCase

from Repository import Repository


class TestRepository(TestCase):
    def test_get_name1(self):
        r = Repository()
        repo = r.find_name('psp-proxy')
        self.assertEqual('mlff-payment-psp-proxy-postgredb', repo)

    def test_get_name2(self):
        r = Repository()
        with self.assertRaises(Exception) as e:
            repo = r.find_name('enforcement')
        self.assertEqual("Nem egyértelmű a repository név!", str(e.exception))

    def test_get_db_name(self):
        r = Repository('mlff-payment-psp-proxy-postgredb')
        self.assertEqual('payment_psp_proxy', r.get_db_name())

    def test_is_table_file_exists_true(self):
        repo = Repository('trip')
        self.assertTrue(repo.is_table_file_exists('trip'))

    def test_is_table_file_exists_false(self):
        repo = Repository('trip')
        self.assertFalse(repo.is_table_file_exists('triptmp'))

    def test_get_tablename_from_indexname(self):
        repo = Repository('customer')
        value = repo.get_tablename_from_indexname('customer.ix_cust_cocallcode_linum')
        self.assertEqual('customer', value)
