from unittest import TestCase

from changelog_header_generator import Changelog_header_generator


class TestChangelogHeaderGenerator(TestCase):
    def test_generate_header_for_drop_constraint(self):
        g = Changelog_header_generator('bertalan.pasztor', 'MLFFDEV-683')
        generated = g.generate_header('ALTER TABLE visual_check.check_package DROP CONSTRAINT ck_checkpack_status;')
        expected = '''---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CHECK_PACKAGE-DDL-0.1.0-MLFFDEV-683-12 runOnChange:true
--comment Drop constraint ck_checkpack_status.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema.table_constraints WHERE constraint_type = 'CHECK' AND constraint_schema = 'visual_check' AND table_name = 'check_package' AND constraint_name = 'ck_checkpack_status'
---------------------------------------------------------------------------------------------------
'''
        self.assertEqual(generated, expected)


    def test_generate_header_for_column(self):
        g = Changelog_header_generator('bertalan.pasztor', 'MLFFDEV-663')
        generated = g.generate_header('ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = '''---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:PAYMENT_METHOD-DDL-0.1.0-MLFFDEV-663-01 runOnChange:true
--comment Change column type on x__version column.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema.columns WHERE table_schema = 'account_info' AND table_name = 'payment_method' AND column_name = 'x__version'
---------------------------------------------------------------------------------------------------
'''
        self.assertEqual(generated, expected)

def test_generate_header_for_column_comment(self):
        g = Changelog_header_generator('bertalan.pasztor', 'MLFFDEV-663')
        generated = g.generate_header('ALTER TABLE account_info.payment_method ALTER COLUMN x__version TYPE int8 USING x__version::int8;')
        expected = '''--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:PAYMENT_METHOD-DDL-0.1.0-MLFFDEV-663-01 runOnChange:true
--comment A numeric cseréje int8-ra az x__version mezőn.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema.columns WHERE table_schema = 'account_info' AND table_name = 'payment_method' AND column_name = 'x__version'
---------------------------------------------------------------------------------------------------
'''
        self.assertEqual(generated, expected)