--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:SECURITY_USER-TBL-MLFFDEV-8134-01 
--comment A SECURITY_USER tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'security_user'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE security_user (
	x__id varchar(30) NOT NULL, -- Unique identifier
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date of creation
	x__insuser varchar(30) NOT NULL, -- Unique identifier of creator user
	x__moddate timestamptz(6) NULL, -- Date of last modification
	x__moduser varchar(30) NULL, -- Unique identifier of modifier user
	x__version int8 NOT NULL DEFAULT 0, -- Versioning of changes
	username varchar(32) NOT NULL, -- Login name of the user
	"password" varchar(255) NULL, -- Hash value of the user's password
	active bool NOT NULL DEFAULT false, -- Security user's status. ( Active or not active)
	CONSTRAINT pk_security_user PRIMARY KEY (x__id)
);
CREATE UNIQUE INDEX ixuk_secuser_username ON security_user USING btree (lower((username)::text));
COMMENT ON TABLE security_user IS 'Contains user data what we need, to authorize the user.';

-- Column comments

COMMENT ON COLUMN security_user.x__id IS 'Unique identifier';
COMMENT ON COLUMN security_user.x__insdate IS 'Date of creation';
COMMENT ON COLUMN security_user.x__insuser IS 'Unique identifier of creator user';
COMMENT ON COLUMN security_user.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN security_user.x__moduser IS 'Unique identifier of modifier user';
COMMENT ON COLUMN security_user.x__version IS 'Versioning of changes';
COMMENT ON COLUMN security_user.username IS 'Login name of the user';
COMMENT ON COLUMN security_user."password" IS 'Hash value of the user''s password';
COMMENT ON COLUMN security_user.active IS 'Security user''s status. ( Active or not active)';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'security_user');

COMMIT;


--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:SECURITY_USER$HIST-TBL-MLFFDEV-8134-01
--comment A SECURITY_USER$HIST history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'security_user$hist'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_table_generator('${schema_name}', 'security_user');

-- GRANT$HIST ==
GRANT SELECT ON TABLE security_user$hist TO ${schema_name}_sel;

COMMIT;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:TR_SECURITY_USER$HIST -TBL-MLFFDEV-8134-01
--comment A SECURITY_USER$HIST  trigger létrehozása..
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call hist_trigger_generator('${schema_name}', 'security_user');

COMMIT;

