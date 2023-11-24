--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:VERIFICATION_CODE-TBL-MLFFDEV-8134-01
--comment A VERIFICATION_CODE tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'verification_code'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE verification_code (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	customer_id varchar(30) NOT NULL,
	subject_value varchar(255) NOT NULL,
	code varchar(30) NOT NULL,
	code_expiry timestamptz(6) NOT NULL,
	subject_type varchar(30) NOT NULL,
	number_of_attempts_resend int4 NOT NULL DEFAULT 0,
	resend_expiry timestamptz(6) NULL,
	CONSTRAINT ck_vercode_subject_type CHECK (((subject_type)::text = ANY (ARRAY[('EMAIL'::character varying)::text, ('PHONE'::character varying)::text]))),
	CONSTRAINT ck_vercode_subject_value CHECK (((((subject_type)::text = 'PHONE'::text) AND ((subject_value)::text ~ '^[0-9]*$'::text)) OR ((subject_type)::text <> 'PHONE'::text))),
	CONSTRAINT pk_verification_code PRIMARY KEY (x__id),
	CONSTRAINT fk_vercode_cust_id FOREIGN KEY (customer_id) REFERENCES customer(x__id) ON DELETE CASCADE ON UPDATE RESTRICT DEFERRABLE
);
CREATE INDEX ix_custmed_cust_id ON verification_code USING btree (customer_id);
CREATE INDEX ix_vercode_code_subject_type ON verification_code USING btree (code, subject_type);
CREATE INDEX ix_vercode_cust_id ON verification_code USING btree (customer_id);
CREATE INDEX ix_vercode_subject_value ON verification_code USING btree (subject_value);

COMMENT ON TABLE verification_code IS 'This table contains the generated code and its properties for the verification process.';

-- Column comments

COMMENT ON COLUMN verification_code.x__id IS 'Unique identifier';
COMMENT ON COLUMN verification_code.x__insdate IS 'Date of creation';
COMMENT ON COLUMN verification_code.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN verification_code.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN verification_code.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN verification_code.x__version IS 'Versioning of changes';
COMMENT ON COLUMN verification_code.customer_id IS 'Unique identifier of customer (FK)';
COMMENT ON COLUMN verification_code.subject_value IS 'Phone number or Email address';
COMMENT ON COLUMN verification_code.code IS 'Generated code';
COMMENT ON COLUMN verification_code.code_expiry IS 'Expiration date';
COMMENT ON COLUMN verification_code.subject_type IS 'The subject to be verified by the code (''EMAIL'', ''PHONE'')';
COMMENT ON COLUMN verification_code.number_of_attempts_resend IS 'Number of attempts verification code resend';
COMMENT ON COLUMN verification_code.resend_expiry IS 'Expiry of resend';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'verification_code');

COMMIT;


--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:VERIFICATION_CODE$HIST-TBL-MLFFDEV-8134-01
--comment A VERIFICATION_CODE$HIST history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'verification_code$hist'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_table_generator('${schema_name}', 'verification_code');

-- GRANT$HIST ==
GRANT SELECT ON TABLE verification_code$hist TO ${schema_name}_sel;

COMMIT;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:TR_VERIFICATION_CODE$HIST-TBL-MLFFDEV-8134-01
--comment A TR_VERIFICATION_CODE$HIST trigger létrehozása..
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_trigger_generator('${schema_name}', 'verification_code');

COMMIT;

