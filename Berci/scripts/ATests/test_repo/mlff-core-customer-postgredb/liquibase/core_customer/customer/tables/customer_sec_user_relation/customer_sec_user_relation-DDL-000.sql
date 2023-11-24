--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_SEC_USER_RELATION-TBL-MLFFDEV-8134-01
--comment A CUSTOMER_SEC_USER_RELATION tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer_sec_user_relation'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE customer_sec_user_relation (
	x__id varchar(30) NOT NULL, -- Unique identifier
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date of creation
	x__insuser varchar(30) NOT NULL, -- Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Date of last modification
	x__moduser varchar(30) NULL, -- Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NOT NULL DEFAULT 0, -- Versioning of changes
	customer_id varchar(30) NOT NULL, -- Unique identifier of CUSTOMER (FK)
	security_user_id varchar(30) NOT NULL, -- Unique identifier of SECURITY_USER (FK)
	CONSTRAINT pk_customer_sec_user_relation PRIMARY KEY (x__id),
	CONSTRAINT fk_custsecu_cust_id FOREIGN KEY (customer_id) REFERENCES customer(x__id) ON DELETE CASCADE ON UPDATE RESTRICT DEFERRABLE,
	CONSTRAINT fk_custsecu_secu_id FOREIGN KEY (security_user_id) REFERENCES security_user(x__id) ON DELETE CASCADE ON UPDATE RESTRICT DEFERRABLE
);
CREATE INDEX ix_custsecu_secu_id ON customer_sec_user_relation USING btree (security_user_id);
CREATE UNIQUE INDEX ixuk_custsecu_cust_id ON customer_sec_user_relation USING btree (customer_id);
COMMENT ON TABLE customer_sec_user_relation IS 'It is a switch table between customer and security user.';

-- Column comments

COMMENT ON COLUMN customer_sec_user_relation.x__id IS 'Unique identifier';
COMMENT ON COLUMN customer_sec_user_relation.x__insdate IS 'Date of creation';
COMMENT ON COLUMN customer_sec_user_relation.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_sec_user_relation.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN customer_sec_user_relation.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_sec_user_relation.x__version IS 'Versioning of changes';
COMMENT ON COLUMN customer_sec_user_relation.customer_id IS 'Unique identifier of CUSTOMER (FK)';
COMMENT ON COLUMN customer_sec_user_relation.security_user_id IS 'Unique identifier of SECURITY_USER (FK)';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'customer_sec_user_relation');

COMMIT;

