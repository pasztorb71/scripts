--liquibase formatted sql

--changeset bertalan.pasztor:FIREBASE_TOKEN-DDL-MLFFDEV-17638-01
--comment Remove column user_session_id.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
ALTER TABLE firebase_token DROP COLUMN user_session_id;
ALTER TABLE firebase_token$hist DROP COLUMN user_session_id;

call hist_trigger_generator('${schema_name}', 'firebase_token');

COMMIT;

