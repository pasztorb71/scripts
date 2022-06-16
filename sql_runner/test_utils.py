from unittest import TestCase

import utils_old


class Test(TestCase):
    def test_password_from_file(self):
        self.assertEqual('fLXyFS0RpmIX9uxGII4N', utils.password_from_file('localhost', 5433))