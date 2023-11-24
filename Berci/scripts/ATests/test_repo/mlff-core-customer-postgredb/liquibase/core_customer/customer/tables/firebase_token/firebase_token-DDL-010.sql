--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:FIREBASE_TOKEN-DDL-MLFFDEV-9375-01 endDelimiter:/
--comment Add unique index uk_fito_usessid_fbastoken.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
DO $$
DECLARE
  v_schema_name text := '${schema_name}';  
  v_table_name  text := 'firebase_token';
BEGIN

  -- -- --
  IF column_exists(v_schema_name, v_table_name, 'user_session_id') 
    AND column_exists(v_schema_name, v_table_name, 'firebase_token') THEN
      DELETE FROM firebase_token
      WHERE x__id IN
        (SELECT x__id FROM
          (SELECT 
             x__id,
             ROW_NUMBER() OVER( PARTITION BY user_session_id, firebase_token ORDER BY x__id ) AS row_num
           FROM firebase_token ft) t
         WHERE t.row_num > 1);      
         
        CREATE UNIQUE INDEX IF NOT EXISTS uk_fito_usessid_fbastoken ON firebase_token USING btree (user_session_id, firebase_token);
  END IF;

  -- -- --
  DROP INDEX IF EXISTS ix_fito_userses_id;

END$$;
COMMIT;
/