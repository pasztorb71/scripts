--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_TOKEN-DDL-MLFFDEV-10449-01
--comment A customer_token tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer_token';
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE customer_token (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	customer_id varchar(30) NOT NULL,
	token varchar(128) NOT NULL,
	token_type varchar(30) NOT NULL,
	token_expiry timestamptz(6) NOT NULL,
	CONSTRAINT pk_customer_token PRIMARY KEY (x__id),
	CONSTRAINT fk_custo_customer_id FOREIGN KEY (customer_id) REFERENCES customer(x__id) DEFERRABLE,
	CONSTRAINT ck_custo_token_type CHECK (((token_type)::text = ANY (ARRAY[('FORGOT_PASSWORD'::character varying)::text])))
);

CREATE INDEX ix_custo_customer_id ON customer_token USING btree (customer_id);

COMMENT ON TABLE customer_token IS 'This table is for storing customer token data. It contains information about tokens related to customers, their types and their expiry dates.';

-- Column comments

COMMENT ON COLUMN customer_token.x__id IS 'Unique identifier';
COMMENT ON COLUMN customer_token.x__insdate IS 'Date of creation';
COMMENT ON COLUMN customer_token.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_token.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN customer_token.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_token.x__version IS 'Versioning of changes';
COMMENT ON COLUMN customer_token.customer_id IS 'Unique identifier of CUSTOMER (FK)';
COMMENT ON COLUMN customer_token.token IS 'Token that is related to a customer.';
COMMENT ON COLUMN customer_token.token_type IS 'Token''s type ["FORGOT_PASSWORD"]';
COMMENT ON COLUMN customer_token.token_expiry IS 'The token expires at this date time.';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'customer_token');

COMMIT;
