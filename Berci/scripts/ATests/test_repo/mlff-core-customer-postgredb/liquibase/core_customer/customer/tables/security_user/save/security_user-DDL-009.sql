--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:SECURITY_USER-DDL-MLFFDEV-8028-01
--comment Rename index.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER INDEX IF EXISTS customer.uk_secuser_username RENAME TO ixuk_secuser_username;
COMMIT;

