--liquibase formatted sql
--changeset tibor.ivan:VERIFICATION_CODE_OUTBOX-DDL-MLFFDEV-19982-01
--comment Create verification_code_outbox table
SET search_path = ${schema_name};

CREATE TABLE verification_code_outbox (
   x__id varchar(30) NOT NULL,
   x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
   x__insuser varchar(30) NOT NULL,
   x__moddate timestamptz(6) NULL,
   x__moduser varchar(30) NULL,
   x__version int8 NOT NULL DEFAULT 0,
   verification_code_id varchar(30) NOT NULL,
   ttl timestamptz(6) NOT NULL,
   CONSTRAINT pk_verification_code_outbox PRIMARY KEY (x__id),
   CONSTRAINT fk_vercobx_verification_code_id FOREIGN KEY (verification_code_id) REFERENCES verification_code (x__id)
);
CREATE INDEX ix_vercobx_verification_code_id ON verification_code_outbox USING btree (verification_code_id);

COMMENT ON TABLE verification_code_outbox IS 'This table stores identifiers of VERIFICATION_CODE records, which should be deleted.';

-- Column comments

COMMENT ON COLUMN verification_code_outbox.x__id IS 'Unique identifier';
COMMENT ON COLUMN verification_code_outbox.x__insdate IS 'Date of creation';
COMMENT ON COLUMN verification_code_outbox.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN verification_code_outbox.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN verification_code_outbox.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN verification_code_outbox.x__version IS 'Versioning of changes';
COMMENT ON COLUMN verification_code_outbox.verification_code_id IS 'Refers to the x__id field of the corresponding verification_code record (FK)';
COMMENT ON COLUMN verification_code_outbox.ttl IS 'Outbox record''s time to live parameter';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'verification_code_outbox');

COMMIT;
