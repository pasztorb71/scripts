--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset ferenc.hrebenku:REGISTRATION_USER_SESSION-TBL-MLFFDEV-20019-01
--comment A REGISTRATION_USER_SESSION tábla eldobása
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DROP TABLE registration_user_session;

COMMIT;
