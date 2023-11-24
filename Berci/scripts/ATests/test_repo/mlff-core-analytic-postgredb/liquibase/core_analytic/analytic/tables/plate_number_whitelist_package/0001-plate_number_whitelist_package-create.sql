--liquibase formatted sql

--changeset ferenc.hrebenku:0001 labels:0.21
--comment MLFFSUP-5755 PLATE_NUMBER_WHITELIST_PACKAGE create
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE plate_number_whitelist_package (
	x__id varchar(30) NOT NULL, -- Unique identifier
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date of creation
	x__insuser varchar(30) NOT NULL, -- Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Date of last modification
	x__moduser varchar(30) NULL, -- Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NOT NULL DEFAULT 0, -- Versioning of changes
	ext_session_id          varchar(30)    NOT NULL,
  customer_last_mod_date  timestamptz(6) NULL,
  vehicle_last_mod_date   timestamptz(6) NULL,
  exemption_last_mod_date timestamptz(6) NULL,
  sanction_last_mod_date  timestamptz(6) NULL,
  psi_last_mod_date       timestamptz(6) NULL,
  CONSTRAINT pk_plate_number_whitelist_package PRIMARY KEY (x__id)
);

COMMENT ON TABLE plate_number_whitelist_package IS 'This table contains plate number whitelist packages.';

-- Column comments

COMMENT ON COLUMN plate_number_whitelist_package.x__id IS 'Unique identifier';
COMMENT ON COLUMN plate_number_whitelist_package.customer_last_mod_date IS 'Last mod date of Customer cache';
COMMENT ON COLUMN plate_number_whitelist_package.vehicle_last_mod_date IS 'Last mod date of Vehicle cache';
COMMENT ON COLUMN plate_number_whitelist_package.exemption_last_mod_date IS 'Last mod date of Exemption cache';
COMMENT ON COLUMN plate_number_whitelist_package.sanction_last_mod_date IS 'Last mod date of Sanction cache';
COMMENT ON COLUMN plate_number_whitelist_package.psi_last_mod_date IS 'Last mod date of Psi cache';
COMMENT ON COLUMN plate_number_whitelist_package.x__insdate IS 'Date of creation';
COMMENT ON COLUMN plate_number_whitelist_package.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN plate_number_whitelist_package.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN plate_number_whitelist_package.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN plate_number_whitelist_package.x__version IS 'Versioning of changes';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'plate_number_whitelist_package');

COMMIT;

