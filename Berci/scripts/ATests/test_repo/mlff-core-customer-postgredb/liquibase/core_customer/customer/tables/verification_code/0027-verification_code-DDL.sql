--liquibase formatted sql
--changeset tibor.ivan:VERIFICATION_CODE-DDL-MLFFDEV-20021-01
--comment Add unique index to verification_code (subject_value, subject_type)
SET search_path = ${schema_name};

CREATE UNIQUE INDEX ixuk_vercode_subject_value_type ON verification_code USING btree (subject_value, subject_type);

COMMIT;
