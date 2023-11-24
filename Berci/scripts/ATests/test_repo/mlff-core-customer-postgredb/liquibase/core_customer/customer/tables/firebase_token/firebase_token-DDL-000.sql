--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:FIREBASE_TOKEN-TBL-MLFFDEV-8918-01
--comment A firebase_token tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'firebase_token'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE firebase_token (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	user_session_id varchar(30) NOT NULL,
	firebase_token varchar(512) NOT NULL,
	status varchar(30) NOT NULL DEFAULT 'ACTIVE',
	CONSTRAINT pk_firebase_token PRIMARY KEY (x__id),
	CONSTRAINT fk_fito_user_session_id FOREIGN KEY (user_session_id) REFERENCES user_session(x__id) DEFERRABLE,
  CONSTRAINT ck_fito_status CHECK (((status)::text = ANY (ARRAY[('ACTIVE'::character varying)::text, ('INACTIVE'::character varying)::text])))
);

CREATE INDEX ix_fito_userses_id ON firebase_token USING btree (user_session_id);
CREATE INDEX ix_fito_firebase_token ON firebase_token USING btree (firebase_token);
CREATE INDEX ix_fito_status ON firebase_token USING btree (status);

COMMENT ON TABLE firebase_token IS 'This table contains the stored firebase token for session of user.';

-- Column comments

COMMENT ON COLUMN firebase_token.x__id IS 'Unique identifier';
COMMENT ON COLUMN firebase_token.x__insdate IS 'Date of creation';
COMMENT ON COLUMN firebase_token.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN firebase_token.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN firebase_token.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN firebase_token.x__version IS 'Versioning of changes';
COMMENT ON COLUMN firebase_token.user_session_id IS 'Unique identifier of user_session (FK)';
COMMENT ON COLUMN firebase_token.firebase_token IS 'Firebase token in raw type';
COMMENT ON COLUMN firebase_token.status IS 'The status of Firebase token (''ACTIVE'', ''INACTIVE'')';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'firebase_token');

COMMIT;


--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:FIREBASE_TOKEN$HIST-TBL-MLFFDEV-8918-01
--comment A firebase_token$hist history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'firebase_token$hist'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_table_generator('${schema_name}', 'firebase_token');

-- GRANT$HIST ==
GRANT SELECT ON TABLE firebase_token$hist TO ${schema_name}_sel;

COMMIT;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:TR_FIREBASE_TOKEN$HIST-TBL-MLFFDEV-8918-01
--comment A tr_firebase_token$hist trigger létrehozása..
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_trigger_generator('${schema_name}', 'firebase_token');

COMMIT;

