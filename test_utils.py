from unittest import TestCase

from utils import get_login_from_file


class Test(TestCase):
    def test_get_login_from_file(self):
        self.assertEqual(get_login_from_file()[0],'bertalan.pasztor')