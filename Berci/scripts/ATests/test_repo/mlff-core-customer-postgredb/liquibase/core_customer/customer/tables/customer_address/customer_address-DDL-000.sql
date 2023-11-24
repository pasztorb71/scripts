--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_ADDRESS-TBL-MLFFDEV-11265-01
--comment A customer_address tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer_address';
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE customer_address (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	customer_id varchar(30) NOT NULL,
	postal_code varchar(5) NOT NULL,
	province varchar(255) NOT NULL,
	district varchar(255) NOT NULL,
	subdistrict varchar(255) NOT NULL,
	city varchar(255) NOT NULL,
	address_line varchar(255) NOT NULL,
	CONSTRAINT pk_customer_address PRIMARY KEY (x__id),
	CONSTRAINT fk_cusadd_customer_id FOREIGN KEY (customer_id) REFERENCES customer(x__id) DEFERRABLE,
  CONSTRAINT ck_cusadd_postal_code CHECK(postal_code ~ '^[0-9]*$')
);

CREATE UNIQUE INDEX uk_cusadd_customer_id ON customer_address USING btree (customer_id);

COMMENT ON TABLE customer_address IS 'This table is for storing customer address data. ';

-- Column comments

COMMENT ON COLUMN customer_address.x__id IS 'Unique identifier';
COMMENT ON COLUMN customer_address.x__insdate IS 'Date of creation';
COMMENT ON COLUMN customer_address.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_address.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN customer_address.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_address.x__version IS 'Versioning of changes';
COMMENT ON COLUMN customer_address.customer_id IS 'Unique identifier of CUSTOMER (FK)';
COMMENT ON COLUMN customer_address.postal_code IS 'Postal code. It can only contain numbers from 0 to 9 as value.';
COMMENT ON COLUMN customer_address.province IS 'Province.';
COMMENT ON COLUMN customer_address.district IS 'District.';
COMMENT ON COLUMN customer_address.subdistrict IS 'Subdistrict.';
COMMENT ON COLUMN customer_address.city IS 'City.';
COMMENT ON COLUMN customer_address.address_line IS 'Address line.';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'customer_address');

COMMIT;

