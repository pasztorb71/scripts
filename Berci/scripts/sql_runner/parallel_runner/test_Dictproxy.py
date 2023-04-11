from unittest import TestCase

from sql_runner.parallel_runner.Dictproxy import Dictproxy


class TestDictproxy(TestCase):
    def test_get_header(self):
        testdata = {'5840|doc_document': [['TABLE_NAME', 'COUNT'], ('document_meta.object_metadata', 176701)]}
        d = Dictproxy(testdata)
        self.assertListEqual(['TABLE_NAME', 'COUNT'], d.header)
