from unittest import TestCase

from Database import Database


class TestDatabase(TestCase):
    def setUp(self) -> None:
        self.db = Database('enforcement_eligibility', 5442)

    def test__get_tables(self):
        tables = self.db.tables
        self.assertTrue(not any(['_p2' in t for t in tables.keys()]))
