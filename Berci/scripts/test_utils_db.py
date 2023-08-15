from unittest import TestCase

import Repository


class Test(TestCase):
    def test_get_repository_from_dbname(self):
        self.assertEqual(Repository.Repository('customer').name, Repository.get_repository_name_from_dbname('core_customer'))
