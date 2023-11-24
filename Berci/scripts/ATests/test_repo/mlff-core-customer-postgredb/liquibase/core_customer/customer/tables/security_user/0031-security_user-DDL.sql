--liquibase formatted sql

--changeset bertalan.pasztor:SECURITY_USER-DDL-MLFFDEV-21701-01
--comment Migrate username to lowercase
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

UPDATE security_user SET username = lower(username);

COMMIT;

