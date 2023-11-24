--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:VERIFICATION_CODE-DDL-MLFFDEV-9372-01 endDelimiter:/
--comment Modify constraint ck_vercode_subject_type.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
DO $$
DECLARE
  v_schema_name text := '${schema_name}';  
  v_table_name  text := 'verification_code';
BEGIN

  -- -- --
  IF constraint_exists(v_schema_name, v_table_name, 'ck_vercode_subject_type') THEN
    ALTER TABLE verification_code DROP CONSTRAINT ck_vercode_subject_type;
    ALTER TABLE verification_code ADD CONSTRAINT ck_vercode_subject_type 
    CHECK (((subject_type)::text = ANY (ARRAY[
    ('EMAIL'::character varying)::text, 
    ('PHONE'::character varying)::text,
    ('DELETE_CUSTOMER'::character varying)::text
    ])));
    COMMENT ON COLUMN verification_code.subject_type IS 'The subject to be verified by the code (''EMAIL'', ''PHONE'', ''DELETE_CUSTOMER'')';
  END IF;

  -- HISTORY ==
  IF column_exists(v_schema_name, v_table_name||'$hist', 'subject_type') THEN
    COMMENT ON COLUMN verification_code.subject_type IS 'Logged field: The subject to be verified by the code (''EMAIL'', ''PHONE'', ''DELETE_CUSTOMER'')';
  END IF;

END$$;
COMMIT;
/