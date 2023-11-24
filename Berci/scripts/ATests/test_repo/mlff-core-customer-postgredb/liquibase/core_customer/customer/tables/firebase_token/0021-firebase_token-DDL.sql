--liquibase formatted sql

--changeset bertalan.pasztor:FIREBASE_TOKEN-DDL-MLFFDEV-17637-02
--comment Alter column user_session_id drop not null.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
ALTER TABLE firebase_token ALTER COLUMN firebase_token SET NOT NULL;
ALTER TABLE firebase_token ALTER COLUMN user_session_id DROP NOT NULL;

COMMIT;

