--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_SEC_USER_RELATION-DDL-MLFFDEV-8028-01
--comment Rename index.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER INDEX IF EXISTS customer.uk_custsecu_cust_id RENAME TO ixuk_custsecu_cust_id;
COMMIT;

