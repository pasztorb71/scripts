--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER runOnChange:true
--comment A CUSTOMER tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer';
---------------------------------------------------------------------------------------------------

CREATE TABLE customer.customer (
	x__id varchar(30) NOT NULL,
	customer_name varchar(200) NOT NULL,
	date_of_birth date NOT NULL,
	phone_number varchar(30) NULL,
	email varchar(255) NULL,
	customer_status varchar(30) NOT NULL DEFAULT 'TEMPORARY'::character varying,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	CONSTRAINT ck_cust_status CHECK (((customer_status)::text = ANY ((ARRAY['TEMPORARY'::character varying, 'ACTIVE'::character varying])::text[]))),
	CONSTRAINT pk_customer PRIMARY KEY (x__id)
);

CREATE UNIQUE INDEX ix_cust_email ON customer.customer USING btree (email);
CREATE UNIQUE INDEX ix_cust_phone_number ON customer.customer USING btree (phone_number);

COMMENT ON TABLE customer.customer IS 'This table describes the customer itself.';

-- Column comments

COMMENT ON COLUMN customer.customer.x__id IS 'Unique identifier';
COMMENT ON COLUMN customer.customer.customer_name IS 'Customer''s name';
COMMENT ON COLUMN customer.customer.date_of_birth IS 'Customer''s birthday';
COMMENT ON COLUMN customer.customer.phone_number IS 'Customer''s phone number';
COMMENT ON COLUMN customer.customer.email IS 'Customer''s email address';
COMMENT ON COLUMN customer.customer.customer_status IS 'Customer''s status';
COMMENT ON COLUMN customer.customer.x__insdate IS 'Date of creation';
COMMENT ON COLUMN customer.customer.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer.customer.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN customer.customer.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer.customer.x__version IS 'Versioning of changes';


--===============================================================================================--
-- GRANT ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_GRANT runOnChange:true
--comment A CUSTOMER táblára jogosultságok kiosztása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer';
---------------------------------------------------------------------------------------------------

ALTER TABLE customer.customer OWNER TO ${schema_name}_tbl_own;

GRANT SELECT ON TABLE customer.customer TO ${schema_name}_sel;
GRANT INSERT, UPDATE ON TABLE customer.customer TO ${schema_name}_mod;
GRANT DELETE, TRUNCATE ON TABLE customer.customer TO ${schema_name}_del;


--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER$HIST runOnChange:true
--comment A CUSTOMER$HIST history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer$hist';
---------------------------------------------------------------------------------------------------

call ${schema_name}.HIST_TABLE_GENERATOR('${schema_name}', 'customer');


--===============================================================================================--
-- GRANT$HIST ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER$HIST_GRANT runOnChange:true
--comment A CUSTOMER$HIST táblára Select jog kiosztása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer$hist';
---------------------------------------------------------------------------------------------------

GRANT SELECT ON TABLE customer.customer$hist TO ${schema_name}_sel;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:TR_CUSTOMER$HIST runOnChange:true
--comment A TR_CUSTOMER$HIST trigger létrehozása..
---------------------------------------------------------------------------------------------------

call ${schema_name}.HIST_TRIGGER_GENERATOR('${schema_name}', 'customer');


