from unittest import TestCase

import utils_repo
from utils_repo import get_all_repos


class Test(TestCase):
    def test_get_all_repos(self):
        self.assertTrue(len(get_all_repos()) > 0)

