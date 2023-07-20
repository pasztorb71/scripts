from unittest import TestCase

from gcloud import list_sql_instances


class Test(TestCase):
    def test_list_sql_instances(self):
        self.assertEqual(9, len(list_sql_instances('mlff-sb', 'mqid')))
