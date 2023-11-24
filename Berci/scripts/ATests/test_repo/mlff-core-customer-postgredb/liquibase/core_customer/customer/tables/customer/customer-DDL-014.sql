--liquibase formatted sql

--changeset bertalan.pasztor:CUSTOMER-DDL-MLFFDEV-12800-01
--comment Create index ix_cust_deletion_date_time.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE INDEX ix_cust_deletion_date_time ON customer.customer (deletion_date_time) WHERE customer_status='TO_BE_DELETED';

COMMIT;

--changeset bertalan.pasztor:CUSTOMER-DDL-MLFFDEV-17012-01
--comment Drop column country_call_code.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER TABLE customer DROP COLUMN IF EXISTS country_call_code;
ALTER TABLE customer$hist DROP COLUMN IF EXISTS country_call_code;
CALL hist_trigger_generator('${schema_name}', 'customer');

COMMIT;

