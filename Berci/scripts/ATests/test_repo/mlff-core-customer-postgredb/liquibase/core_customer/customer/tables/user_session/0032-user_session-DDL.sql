--liquibase formatted sql

--changeset bertalan.pasztor:USER_SESSION-DDL-MLFFDEV-21701-01
--comment Migrate username to lowercase
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
UPDATE user_session SET username = lower(username);
    
COMMIT;

