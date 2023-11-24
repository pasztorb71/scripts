--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_OUTBOX-TBL-MLFFDEV-8736-01
--comment A customer_outbox tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer_outbox'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE customer_outbox (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	customer_id varchar(30) NOT NULL,
	ttl timestamptz(6) NOT NULL,
	CONSTRAINT pk_customer_outbox PRIMARY KEY (x__id),
	CONSTRAINT fk_cusout_customer_id FOREIGN KEY (customer_id) REFERENCES customer(x__id) DEFERRABLE
);

CREATE INDEX ix_cusout_customer_id ON customer_outbox USING btree (customer_id);

COMMENT ON TABLE customer_outbox IS 'This table describes the customer outbox itself. ';

-- Column comments

COMMENT ON COLUMN customer_outbox.x__id IS 'Unique identifier';
COMMENT ON COLUMN customer_outbox.x__insdate IS 'Date of creation';
COMMENT ON COLUMN customer_outbox.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_outbox.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN customer_outbox.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_outbox.x__version IS 'Versioning of changes';
COMMENT ON COLUMN customer_outbox.customer_id IS 'Customer''s identification';
COMMENT ON COLUMN customer_outbox.ttl IS 'Time to leave';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'customer_outbox');

COMMIT;

