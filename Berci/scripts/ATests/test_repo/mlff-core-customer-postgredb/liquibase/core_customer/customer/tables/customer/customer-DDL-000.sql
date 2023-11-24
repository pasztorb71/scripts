--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER-TBL-MLFFDEV-8134-01
--comment A CUSTOMER tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE customer (
	x__id varchar(30) NOT NULL, -- Unique identifier
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date of creation
	x__insuser varchar(30) NOT NULL, -- Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Date of last modification
	x__moduser varchar(30) NULL, -- Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NOT NULL DEFAULT 0, -- Versioning of changes
	customer_name varchar(200) NOT NULL, -- Customer's name
	date_of_birth date NOT NULL, -- Customer's birthday
	phone_number varchar(30) NULL, -- Customer's phone number
	email varchar(200) NULL, -- Customer's email address
	customer_status varchar(30) NOT NULL DEFAULT 'TEMPORARY'::character varying, -- Customer's status ["TEMPORARY","ACTIVE" ]
	"language" varchar(10) NOT NULL DEFAULT 'ID'::character varying, -- Application language ["ID","EN" ]
	nik_number varchar(16) NULL, -- Customer's NIK number
	country_call_code varchar(3) NULL, -- Country call code
	CONSTRAINT ck_cust_status CHECK (((customer_status)::text = ANY (ARRAY[('TEMPORARY'::character varying)::text, ('ACTIVE'::character varying)::text]))),
	CONSTRAINT ck_customer_language CHECK (((language)::text = ANY (ARRAY[('ID'::character varying)::text, ('EN'::character varying)::text]))),
	CONSTRAINT ck_customer_nik_number CHECK (((nik_number IS NULL) OR (length((nik_number)::text) = 16))),
	CONSTRAINT ck_customer_phone_number CHECK (((phone_number)::text ~ '^[0-9]*$'::text)),
	CONSTRAINT pk_customer PRIMARY KEY (x__id)
);
CREATE INDEX ix_cust_custname ON customer USING btree (customer_name);
CREATE INDEX ix_cust_date_of_birth ON customer USING btree (date_of_birth);
CREATE UNIQUE INDEX ixuk_cust_email ON customer USING btree (email);
CREATE UNIQUE INDEX ixuk_cust_phone_number ON customer USING btree (phone_number);
COMMENT ON TABLE customer IS 'This table describes the customer itself.';

-- Column comments

COMMENT ON COLUMN customer.x__id IS 'Unique identifier';
COMMENT ON COLUMN customer.x__insdate IS 'Date of creation';
COMMENT ON COLUMN customer.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN customer.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer.x__version IS 'Versioning of changes';
COMMENT ON COLUMN customer."language" IS 'Application language ["ID","EN" ]';
COMMENT ON COLUMN customer.customer_name IS 'Customer''s name';
COMMENT ON COLUMN customer.date_of_birth IS 'Customer''s birthday';
COMMENT ON COLUMN customer.phone_number IS 'Customer''s phone number';
COMMENT ON COLUMN customer.email IS 'Customer''s email address';
COMMENT ON COLUMN customer.customer_status IS 'Customer''s status ["TEMPORARY","ACTIVE" ]';
COMMENT ON COLUMN customer.nik_number IS 'Customer''s NIK number';
COMMENT ON COLUMN customer.country_call_code IS 'Country call code';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'customer');

COMMIT;


--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER$HIST-TBL-MLFFDEV-8134-01
--comment A CUSTOMER$HIST history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer$hist'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_table_generator('${schema_name}', 'customer');

-- GRANT$HIST ==
GRANT SELECT ON TABLE customer$hist TO ${schema_name}_sel;

COMMIT;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:TR_CUSTOMER$HIST-TBL-MLFFDEV-8134-01
--comment A TR_CUSTOMER$HIST trigger létrehozása..
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_trigger_generator('${schema_name}', 'customer');

COMMIT;

