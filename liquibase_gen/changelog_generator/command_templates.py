tmp_add_column = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Add column !!colname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_comment_column = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Comment on column !!colname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_comment_table = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Comment on table !!table_lower!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_catalog.pg_tables WHERE schemaname = '!!schema!!' AND tablename = '!!table_lower!!'
---------------------------------------------------------------------------------------------------
"""
tmp_add_ck_constraint = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Add constraint !!consname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM information_schema.table_constraints WHERE constraint_type = 'CHECK' AND constraint_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND constraint_name = '!!consname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_add_fk_constraint = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Add constraint !!consname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM information_schema.table_constraints WHERE constraint_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND constraint_name = '!!consname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_drop_constraint = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Drop constraint !!consname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema.table_constraints WHERE constraint_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND constraint_name = '!!consname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_cre_index = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Add index !!indexname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_catalog.pg_indexes WHERE schemaname = '!!schema!!' AND indexname = '!!indexname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_update = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Update column !!colname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_delete = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Delete from !!table_lower!! table.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_catalog.pg_tables WHERE schemaname = '!!schema!!' AND tablename = '!!table_lower!!'
---------------------------------------------------------------------------------------------------
"""
tmp_set_default = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Set default on column !!colname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_drop_not_null = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Set !!colname!! column to NULL.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_set_not_null = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Alter column !!colname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_column_type = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Change type of !!colname!! column.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_drop_index = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Drop index !!indexname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_catalog.pg_indexes WHERE schemaname = '!!schema!!' AND indexname = '!!indexname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_cre_index = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Create index !!indexname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_catalog.pg_indexes WHERE schemaname = '!!schema!!' AND indexname = '!!indexname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_rename_column = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Rename column !!colname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_drop_table = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Drop table !!table_lower!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_catalog.pg_tables WHERE schemaname = '!!schema!!' AND tablename = '!!table_lower!!'
---------------------------------------------------------------------------------------------------
"""
tmp_drop_trigger = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Drop trigger !!trigger!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:3 SELECT count(*) FROM information_schema.triggers WHERE trigger_schema = '!!schema!!' AND trigger_name = '!!trigger!!'
---------------------------------------------------------------------------------------------------
"""
tmp_drop_column = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Drop column !!colname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM information_schema."columns" c WHERE table_schema = '!!schema!!' AND table_name = '!!table_lower!!' AND column_name = '!!colname!!'
---------------------------------------------------------------------------------------------------
"""
tmp_grant = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Grant on table !!table_lower!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_tables WHERE schemaname = '!!schema!!' AND tablename = '!!table_lower!!';
---------------------------------------------------------------------------------------------------
"""
tmp_rename_index = """---------------------------------------------------------------------------------------------------
--changeset !!author!!:!!table_upper!!-DDL-!!version!!-!!ticket!!-!!serial!! runOnChange:true
--comment Rename index !!indexname!!.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_catalog.pg_indexes WHERE schemaname = '!!schema!!' AND indexname = '!!indexname!!'
---------------------------------------------------------------------------------------------------
"""