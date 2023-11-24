--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_ADDRESS-DDL-MLFFDEV-12204-01
--comment Modify subdistrict column.
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT public.public_changelog_row_count('CUSTOMER_ADDRESS-DDL-MLFFDEV-12204-01')
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER TABLE customer_address ALTER COLUMN subdistrict TYPE varchar(128) USING subdistrict::varchar;
ALTER TABLE customer_address$hist ALTER COLUMN subdistrict TYPE varchar(128) USING subdistrict::varchar;

COMMIT;

