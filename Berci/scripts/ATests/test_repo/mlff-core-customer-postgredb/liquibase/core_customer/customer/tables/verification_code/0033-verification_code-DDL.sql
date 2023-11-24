--liquibase formatted sql

--changeset bertalan.pasztor:VERIFICATION_CODE-DDL-MLFFDEV-20702-01
--comment Drop column resend_expiry
--
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER TABLE verification_code DROP COLUMN resend_expiry;
ALTER TABLE verification_code$hist DROP COLUMN resend_expiry;

call hist_trigger_generator('${schema_name}', 'verification_code');

COMMIT;
