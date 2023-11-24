--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER-DDL-MLFFDEV-8028-01
--comment Rename indexes.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER INDEX IF EXISTS ix_cust_email RENAME TO ixuk_cust_email;
ALTER INDEX IF EXISTS ix_cust_phone_number RENAME TO ixuk_cust_phone_number;
COMMIT;

