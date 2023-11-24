--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset ferenc.hrebenku:VERIFICATION_CODE-DDL-MLFFDEV-19564-01
--comment Alter table verification_code
--
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER TABLE verification_code ALTER COLUMN customer_id DROP NOT NULL;

ALTER TABLE  verification_code ALTER COLUMN number_of_attempts_resend SET DEFAULT 0;

ALTER TABLE verification_code ADD COLUMN reserved_ttl timestamptz(6) NULL;

ALTER TABLE verification_code ADD COLUMN number_of_attempt int4 NOT NULL DEFAULT 0;

COMMENT ON COLUMN verification_code.number_of_attempt IS 'Number of attempts verification code get with wrong';

ALTER TABLE verification_code$hist ADD COLUMN reserved_ttl timestamptz(6) NULL;

ALTER TABLE verification_code$hist ADD COLUMN number_of_attempt int4 NOT NULL DEFAULT 0;

COMMENT ON COLUMN verification_code$hist.number_of_attempt IS 'Logged field: Number of attempts verification code get with wrong';

COMMIT;
