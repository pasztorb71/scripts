--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_MEDIA-DDL-MLFFDEV-8028-01
--comment Rename indexes.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER INDEX IF EXISTS ix_custmed_custid_doctype RENAME TO ixuk_custmed_custid_doctype;
COMMIT;

