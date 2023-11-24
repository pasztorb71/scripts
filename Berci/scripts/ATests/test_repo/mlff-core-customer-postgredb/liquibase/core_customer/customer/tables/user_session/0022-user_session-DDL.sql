--liquibase formatted sql

--changeset bertalan.pasztor:USER_SESSION-DDL-MLFFDEV-17637-01
--comment Add column firebase_token_id and FK.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
        
ALTER TABLE user_session ADD firebase_token_id varchar(30) NULL;
COMMENT ON COLUMN user_session.firebase_token_id IS 'Unique identifier of firebase_token (FK)';

update user_session us set firebase_token_id = nested.x__id 
    from (select ft.x__id, ft.user_session_id from firebase_token ft) nested
    where us.x__id = nested.user_session_id;
    
COMMIT;

