from unittest import TestCase

import utils_db
from Repository import Repository


class Test(TestCase):
    def test_get_repository_from_dbname(self):
        reponame = Repository('customer').name
        r = utils_db.get_repository_name_from_dbname('core_customer')
        self.assertEqual(Repository('customer').name, utils_db.get_repository_name_from_dbname('core_customer'))
