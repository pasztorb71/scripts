--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset ferenc.hrebenku:CUSTOMER-DDL-MLFFDEV-20019-01
--comment Modify ck_cust_status constraint
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DELETE FROM customer_address
WHERE customer_id IN (select x__id from customer where customer_status = 'TEMPORARY');

DELETE FROM verification_code
WHERE customer_id IN (select x__id from customer where customer_status = 'TEMPORARY');

DELETE FROM customer_outbox
WHERE customer_id IN (select x__id from customer where customer_status = 'TEMPORARY');

DELETE FROM customer_media
WHERE customer_id IN (select x__id from customer where customer_status = 'TEMPORARY');

DELETE FROM customer_token
WHERE customer_id IN (select x__id from customer where customer_status = 'TEMPORARY');

-- A customer_sec_user_relation FK-án ON DELETE CASCADE van
DELETE FROM security_user
WHERE x__id IN (select security_user_id from customer_sec_user_relation where customer_id IN (select x__id from customer where customer_status = 'TEMPORARY'));

-- A customer_sec_user_relation FK-án ON DELETE CASCADE van
DELETE FROM customer WHERE customer_status = 'TEMPORARY';

ALTER TABLE customer DROP CONSTRAINT ck_cust_status;

ALTER TABLE customer ADD CONSTRAINT ck_cust_status CHECK (((customer_status)::text = ANY (ARRAY[
      ('ACTIVE'::character varying)::text,
      ('TO_BE_DELETED'::character varying)::text,
      ('DELETED'::character varying)::text
      ])));
      
COMMIT;
