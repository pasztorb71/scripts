--liquibase formatted sql

--changeset bertalan.pasztor:FIREBASE_TOKEN_OUTBOX-TBL-MLFFDEV-17637-01
--comment A firebase_token_outbox tábla létrehozása..
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE firebase_token_outbox (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	firebase_token_id varchar(30) NOT NULL,
	ttl timestamptz(6) NOT NULL,
	CONSTRAINT pk_firebase_token_outbox PRIMARY KEY (x__id),
	CONSTRAINT fk_firetokout_firebase_token_id FOREIGN KEY (firebase_token_id) REFERENCES firebase_token(x__id) DEFERRABLE
);

CREATE INDEX ix_firetokout_firebase_token_id ON firebase_token_outbox USING btree (firebase_token_id);

COMMENT ON TABLE firebase_token_outbox IS 'This table stores identifiers of FIREBASE_TOKEN records, which should be inactivated.';

-- Column comments

COMMENT ON COLUMN firebase_token_outbox.x__id IS 'Unique identifier';
COMMENT ON COLUMN firebase_token_outbox.x__insdate IS 'Date of creation';
COMMENT ON COLUMN firebase_token_outbox.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN firebase_token_outbox.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN firebase_token_outbox.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN firebase_token_outbox.x__version IS 'Versioning of changes';
COMMENT ON COLUMN firebase_token_outbox.firebase_token_id IS 'Refers to the x__id field of the corresponding record (FK)';
COMMENT ON COLUMN firebase_token_outbox.ttl IS 'Outbox record''s time to live parameter';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'firebase_token_outbox');

COMMIT;

