--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:REGISTRATION_USER_SESSION-TBL-MLFFDEV-8134-01
--comment A REGISTRATION_USER_SESSION tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'registration_user_session'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE registration_user_session (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	security_user_id varchar(30) NOT NULL,
	username varchar(32) NOT NULL,
	session_token varchar(50) NOT NULL,
	session_token_expiry timestamptz(6) NOT NULL,
	CONSTRAINT pk_registration_user_session PRIMARY KEY (x__id),
	CONSTRAINT fk_reguser_secu_id FOREIGN KEY (security_user_id) REFERENCES security_user(x__id) ON DELETE CASCADE ON UPDATE RESTRICT DEFERRABLE
);
CREATE INDEX ix_reguser_secu_id ON registration_user_session USING btree (security_user_id);
CREATE INDEX ix_reguser_session_token ON registration_user_session USING btree (session_token);
CREATE INDEX ix_reguser_username ON registration_user_session USING btree (username);

COMMENT ON TABLE registration_user_session IS 'This table contains every logged in user''s session data.';

-- Column comments

COMMENT ON COLUMN registration_user_session.x__id IS 'Unique identifier';
COMMENT ON COLUMN registration_user_session.x__insdate IS 'Date of creation';
COMMENT ON COLUMN registration_user_session.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN registration_user_session.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN registration_user_session.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN registration_user_session.x__version IS 'Versioning of changes';
COMMENT ON COLUMN registration_user_session.username IS 'Login name of the user';
COMMENT ON COLUMN registration_user_session.session_token IS 'Session token identifier';
COMMENT ON COLUMN registration_user_session.session_token_expiry IS 'Expiration date of session token';
        
-- GRANT ==
call add_privileges_to_table('${schema_name}', 'registration_user_session');

COMMIT;

