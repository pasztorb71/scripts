--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER-DDL-MLFFDEV-8676-01 endDelimiter:/
--comment Add column deletion_date_time.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('CUSTOMER-DDL-MLFFDEV-8676-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$
DECLARE
  v_schema_name text     := '${schema_name}';
  v_table_name  text     := 'customer';
  v_table_name_hist text := 'customer$hist';
BEGIN

  -- -- --
  IF table_exists(v_schema_name, v_table_name) AND NOT column_exists(v_schema_name, v_table_name, 'deletion_date_time')THEN
    ALTER TABLE customer ADD deletion_date_time timestamptz(6) NULL;
    COMMENT ON COLUMN customer.deletion_date_time IS 'Customer deletion date time';
  END IF;

  -- -- --
  IF table_exists(v_schema_name, v_table_name_hist) AND NOT column_exists(v_schema_name, v_table_name_hist, 'deletion_date_time') THEN
    ALTER TABLE customer$hist ADD deletion_date_time timestamptz(6) NULL;
    COMMENT ON COLUMN customer$hist.deletion_date_time IS 'Logged field: Customer deletion date time';
  END IF;
  
  -- -- --
  IF table_exists(v_schema_name, v_table_name) AND table_exists(v_schema_name, v_table_name_hist) THEN
    call ${schema_name}.HIST_TRIGGER_GENERATOR('${schema_name}', 'customer');
  END IF;

  -- -- --
  ALTER TABLE customer DROP CONSTRAINT IF EXISTS ck_cust_status;

  -- -- --
  IF NOT constraint_exists(v_schema_name, v_table_name, 'ck_cust_status') THEN
    ALTER TABLE customer ADD CONSTRAINT ck_cust_status CHECK (((customer_status)::text = ANY (ARRAY[
      ('TEMPORARY'::character varying)::text, 
      ('ACTIVE'::character varying)::text,
      ('TO_BE_DELETED'::character varying)::text,
      ('DELETED'::character varying)::text
      ])));
    COMMENT ON COLUMN customer.customer_status IS 'Customer''s status ["TEMPORARY","ACTIVE", "TO_BE_DELETED", "DELETED" ]';
    COMMENT ON COLUMN customer$hist.customer_status IS 'Logged field: Customer''s status ["TEMPORARY","ACTIVE", "TO_BE_DELETED", "DELETED" ]';
  END IF;

END
$$;
COMMIT;
/

---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER-DDL-MLFFDEV-9802-01 endDelimiter:/
--comment Change indexes.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('CUSTOMER-DDL-MLFFDEV-9802-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$
DECLARE
  v_schema_name text     := '${schema_name}';
BEGIN

  -- -- --
  DROP INDEX IF EXISTS ixuk_cust_email;
  CREATE UNIQUE INDEX ixuk_cust_email ON customer USING btree (email) WHERE ((customer_status)::text <> 'DELETED'::text);

  -- -- --
  DROP INDEX IF EXISTS ix_cust_email;
  CREATE INDEX ix_cust_email ON customer USING btree (email) WHERE ((customer_status)::text = 'DELETED'::text);

  -- -- --
  DROP INDEX IF EXISTS ixuk_cust_phone_number;
  CREATE UNIQUE INDEX ixuk_cust_phone_number ON customer USING btree (phone_number) WHERE ((customer_status)::text <> 'DELETED'::text);

  -- -- --
  DROP INDEX IF EXISTS ix_cust_phone_number;
  CREATE INDEX ix_cust_phone_number ON customer USING btree (phone_number) WHERE ((customer_status)::text = 'DELETED'::text);

END
$$;
COMMIT;
/

---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER-DDL-MLFFDEV-10380-01 endDelimiter:/
--comment Change indexes.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('CUSTOMER-DDL-MLFFDEV-10380-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$
DECLARE
  v_schema_name text     := '${schema_name}';
BEGIN

  -- -- --
  DROP INDEX IF EXISTS ix_cust_email;
  CREATE INDEX ix_cust_email ON customer USING hash (email);

  -- -- --
  DROP INDEX IF EXISTS ix_cust_phone_number;
  CREATE INDEX ix_cust_phone_number ON customer USING hash (phone_number);

END
$$;
COMMIT;
/

