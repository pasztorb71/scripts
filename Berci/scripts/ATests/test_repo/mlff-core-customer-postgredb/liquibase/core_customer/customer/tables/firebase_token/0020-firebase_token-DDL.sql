--liquibase formatted sql

--changeset bertalan.pasztor:FIREBASE_TOKEN-DDL-MLFFDEV-17637-01
--comment Remove constraint fk_fito_user_session_id.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
ALTER TABLE firebase_token DROP CONSTRAINT fk_fito_user_session_id;
ALTER TABLE firebase_token ALTER COLUMN firebase_token DROP NOT NULL;

COMMIT;

