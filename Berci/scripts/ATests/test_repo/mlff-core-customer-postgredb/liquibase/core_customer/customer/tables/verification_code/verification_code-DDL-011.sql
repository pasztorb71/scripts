--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:VERIFICATION_CODE-DDL-MLFFDEV-10791-01
--comment Drop index ix_vercode_code_subject_type.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('VERIFICATION_CODE-DDL-MLFFDEV-10791-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DROP INDEX IF EXISTS ix_vercode_code_subject_type;

COMMIT;
