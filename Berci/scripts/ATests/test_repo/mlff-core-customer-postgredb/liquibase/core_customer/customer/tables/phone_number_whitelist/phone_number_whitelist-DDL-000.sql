--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:PHONE_NUMBER_WHITELIST-TBL-MLFFDEV-11209-01
--comment A phone_number_whitelist tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'phone_number_whitelist';
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE phone_number_whitelist (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	phone_number varchar(30) NOT NULL UNIQUE,
	CONSTRAINT pk_phone_number_whitelist PRIMARY KEY (x__id),
	CONSTRAINT uk_phonumwhite_phone_number UNIQUE (phone_number)
);

COMMENT ON TABLE phone_number_whitelist IS 'This table stores the whitelisted phone numbers.';

-- Column comments

COMMENT ON COLUMN phone_number_whitelist.x__id IS 'Unique identifier';
COMMENT ON COLUMN phone_number_whitelist.x__insdate IS 'Date of creation';
COMMENT ON COLUMN phone_number_whitelist.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN phone_number_whitelist.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN phone_number_whitelist.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN phone_number_whitelist.x__version IS 'Versioning of changes';
COMMENT ON COLUMN phone_number_whitelist.phone_number IS 'Customer''s phone number';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'phone_number_whitelist');

COMMIT;

