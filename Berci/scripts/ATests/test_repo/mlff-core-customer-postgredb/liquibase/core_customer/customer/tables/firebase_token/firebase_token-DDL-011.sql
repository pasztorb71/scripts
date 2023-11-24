--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:FIREBASE_TOKEN-DDL-MLFFDEV-10823-01 endDelimiter:/
--comment Change column length firebase_token.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('FIREBASE_TOKEN-DDL-MLFFDEV-10823-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
DO $$
DECLARE
  v_schema_name text := '${schema_name}';  
  v_table_name  text := 'firebase_token';
BEGIN

  -- -- --
  IF column_exists(v_schema_name, v_table_name, 'firebase_token') THEN
    ALTER TABLE firebase_token ALTER COLUMN firebase_token TYPE text USING firebase_token::text;
  END IF;

  -- HISTORY --
  IF column_exists(v_schema_name, 'firebase_token$hist', 'firebase_token') THEN
    ALTER TABLE firebase_token$hist ALTER COLUMN firebase_token TYPE text USING firebase_token::text;
  END IF;

END$$;
COMMIT;
/