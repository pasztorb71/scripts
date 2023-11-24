--liquibase formatted sql

--changeset bertalan.pasztor:USER_SESSION-DDL-MLFFDEV-17638-01
--comment Add FK on firebase_token_id.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
ALTER TABLE user_session ADD CONSTRAINT fk_usession_firebase_token_id FOREIGN KEY (firebase_token_id) REFERENCES firebase_token(x__id);
    
COMMIT;

