--liquibase formatted sql

--changeset bertalan.pasztor:0034 VERIFICATION_CODE
--comment MLFFSUP-5177 Set reserved_ttl column to current time where is null
SET search_path = ${schema_name};

UPDATE verification_code SET reserved_ttl = CURRENT_TIMESTAMP WHERE reserved_ttl IS NULL;

ALTER TABLE verification_code ALTER COLUMN reserved_ttl SET NOT NULL;

COMMIT;
