--liquibase formatted sql

--===============================================================================================--
-- DDL ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:SECURITY_USER-DDL-MLFFDEV-10791-01
--comment Change indexes.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

-- -- --
DROP INDEX IF EXISTS ixuk_secuser_username;
CREATE UNIQUE INDEX IF NOT EXISTS uk_secuser_username ON security_user  (lower((username)::text)) WHERE (active = true);

-- -- --
DROP INDEX IF EXISTS ix_secuser_username_lower;
CREATE INDEX IF NOT EXISTS ix_secuser_username_lower ON security_user (lower((username)::text));

-- -- --
DROP INDEX IF EXISTS ix_secuser_username;
CREATE INDEX IF NOT EXISTS ix_secuser_username ON security_user (username);

COMMIT;

