from unittest import TestCase

from utils import password_from_file


class Test(TestCase):
    def test_password_from_file(self):
        self.assertEqual('fLXyFS0RpmIX9uxGII4N', password_from_file('localhost', 5433))