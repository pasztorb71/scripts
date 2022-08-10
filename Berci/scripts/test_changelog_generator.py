from unittest import TestCase

from liquibase_gen.changelog_generator.main import is_history_related_command, gen_history_command_from_command


class Test(TestCase):
    def test_is_history_related_command(self):
        stmt = "ALTER TABLE psp_clearing.psp_correction ADD psp_settlement_batch_id varchar(30) NULL;"
        self.assertTrue(is_history_related_command(stmt))

    def test_gen_history_command_from_command(self):
        stmt = "ALTER TABLE psp_clearing.psp_correction ADD psp_settlement_batch_id varchar(30) NULL;"
        expected = "ALTER TABLE psp_clearing.psp_correction$hist ADD psp_settlement_batch_id varchar(30) NULL;"
        self.assertEqual(gen_history_command_from_command(stmt), expected)

    def test_gen_history_command_from_command_same_schema_table(self):
        stmt = "ALTER TABLE psp_clearing.psp_clearing ADD psp_settlement_batch_id varchar(30) NULL;"
        expected = "ALTER TABLE psp_clearing.psp_clearing$hist ADD psp_settlement_batch_id varchar(30) NULL;"
        self.assertEqual(gen_history_command_from_command(stmt), expected)

    def test_gen_history_command_from_command_comment(self):
        stmt = "COMMENT ON COLUMN psp_clearing.psp_correction.psp_settlement_batch_id IS 'Identifier of settlement batch record (x__id from the psp_clearing.psp_settlement_batch) (for conciliation)';"
        expected = "COMMENT ON COLUMN psp_clearing.psp_correction$hist.psp_settlement_batch_id IS 'Logged field: Identifier of settlement batch record (x__id from the psp_clearing.psp_settlement_batch) (for conciliation)';"
        self.assertEqual(gen_history_command_from_command(stmt), expected)

