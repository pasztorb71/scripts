from unittest import TestCase

from liquibase_gen.gen_table.Confluence import Confluence


class TestConfluence(TestCase):
    def test_get_table_comment(self):
        conf = Confluence()
        html = conf.get_table_from_url('https://confluence.icellmobilsoft.hu/pages/viewpage.action?spaceKey=MLFF&title=SANCTION_MULTIPLIER')
        table_comment = conf.get_table_comment()
        self.assertEqual('This table contains the sanction data.', table_comment)
