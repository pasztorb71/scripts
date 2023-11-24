--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_ADDRESS-DDL-MLFFDEV-11265-01
--comment Drop index ix_vercode_code_subject_type.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('CUSTOMER_ADDRESS-DDL-MLFFDEV-11265-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER TABLE customer_address DROP CONSTRAINT IF EXISTS fk_cusadd_customer_id;
ALTER TABLE customer_address ADD CONSTRAINT fk_cusadd_customer_id FOREIGN KEY (customer_id) REFERENCES customer(x__id) ON DELETE CASCADE ON UPDATE RESTRICT DEFERRABLE;

COMMIT;

---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_ADDRESS-DDL-MLFFDEV-11265-02
--comment modify columns.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('CUSTOMER_ADDRESS-DDL-MLFFDEV-11265-02')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER TABLE customer_address ALTER COLUMN province TYPE varchar(64) USING province::varchar;
ALTER TABLE customer_address ALTER COLUMN district TYPE varchar(128) USING district::varchar;
ALTER TABLE customer_address ALTER COLUMN subdistrict TYPE varchar(64) USING subdistrict::varchar;
ALTER TABLE customer_address ALTER COLUMN city TYPE varchar(64) USING city::varchar;

COMMIT;


--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_ADDRESS$HIST-TBL-MLFFDEV-11265-02
--comment A customer_address$hist history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer_address$hist'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_table_generator('${schema_name}', 'customer_address');

-- GRANT$HIST ==
GRANT SELECT ON TABLE customer_address$hist TO ${schema_name}_sel;

COMMIT;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:TR_CUSTOMER_ADDRESS$HIST-TBL-MLFFDEV-11265-02
--comment A tr_customer_address$hist trigger létrehozása..
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_trigger_generator('${schema_name}', 'customer_address');

COMMIT;

