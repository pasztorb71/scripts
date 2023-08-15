from unittest import TestCase

from liquibase_gen.gen_table.Confluence import Confluence


class TestConfluence(TestCase):
    def test_get_table_comment(self):
        conf = Confluence()
        html = conf.get_table_from_url('https://icellmobilsoft-int.atlassian.net/wiki/spaces/MLFF/pages/62734249/SANCTION+MULTIPLIER')
        table_comment = conf.get_table_comment()
        self.assertEqual('This table contains the sanction data.', table_comment)
