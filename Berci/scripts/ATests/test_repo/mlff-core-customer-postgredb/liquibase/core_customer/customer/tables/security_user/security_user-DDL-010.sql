--liquibase formatted sql

---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:SECURITY_USER-DDL-MLFFDEV-9802-01 endDelimiter:/
--comment Change indexes.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$
DECLARE
  v_schema_name text     := '${schema_name}';
BEGIN

  -- -- --
  DROP INDEX IF EXISTS ixuk_secuser_username;
  CREATE UNIQUE INDEX ixuk_secuser_username ON security_user USING btree (lower((username)::text)) WHERE (active = true);

  -- -- --
  DROP INDEX IF EXISTS ix_secuser_username;
  CREATE INDEX ix_secuser_username ON security_user USING btree (lower((username)::text)) WHERE (active != true);

END $$;
COMMIT;
/

---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:SECURITY_USER-DDL-MLFFDEV-9877-01
--comment Migrate values.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('SECURITY_USER-DDL-MLFFDEV-9877-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

WITH t AS (
SELECT su.x__id 
FROM customer c 
JOIN customer_sec_user_relation csur 
  ON c.x__id = csur.customer_id 
JOIN security_user su 
  ON csur.security_user_id = su.x__id
WHERE c.customer_status IN ('TEMPORARY', 'ACTIVE', 'TO_BE_DELETED')
AND su.active = FALSE 
)
UPDATE security_user SET active = TRUE
WHERE x__id IN (SELECT x__id FROM t);

WITH t AS (
SELECT su.x__id 
FROM customer c 
JOIN customer_sec_user_relation csur 
  ON c.x__id = csur.customer_id 
JOIN security_user su 
  ON csur.security_user_id = su.x__id
WHERE c.customer_status IN ('DELETED')
AND su.active = TRUE 
)
UPDATE security_user SET active = FALSE
WHERE x__id IN (SELECT x__id FROM t);

COMMIT;
