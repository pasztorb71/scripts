--liquibase formatted sql

--changeset ferenc.hrebenku:0002 labels:0.21
--comment MLFFSUP-5755 PLATE_NUMBER_WHITELIST create
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE plate_number_whitelist (
	x__id varchar(30) NOT NULL, -- Unique identifier
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date of creation
	x__insuser varchar(30) NOT NULL, -- Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Date of last modification
	x__moduser varchar(30) NULL, -- Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NOT NULL DEFAULT 0, -- Versioning of changes
  plate_number_whitelist_package_id varchar(30)    NOT NULL,
  plate_number                      varchar(32)    NOT NULL,
  country_code                      varchar(3)     NULL,
  CONSTRAINT pk_plate_number_whitelist PRIMARY KEY (x__id),
  CONSTRAINT fk_planumwhitepack_plate_number_whitelist_package_id 
  FOREIGN KEY (plate_number_whitelist_package_id) REFERENCES plate_number_whitelist_package (x__id) DEFERRABLE
);

COMMENT ON TABLE plate_number_whitelist IS 'This table contains plate number whitelists.';

-- Column comments

COMMENT ON COLUMN plate_number_whitelist.x__id IS 'Unique identifier';
COMMENT ON COLUMN plate_number_whitelist.x__insdate IS 'Date of creation';
COMMENT ON COLUMN plate_number_whitelist.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN plate_number_whitelist.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN plate_number_whitelist.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN plate_number_whitelist.x__version IS 'Versioning of changes';
COMMENT ON COLUMN plate_number_whitelist.plate_number_whitelist_package_id IS 'Plate number whitelist package identifier (FK)';
COMMENT ON COLUMN plate_number_whitelist.plate_number IS 'Plate number of vehicle.';
COMMENT ON COLUMN plate_number_whitelist.country_code IS 'Country code of vehicles plate number';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'plate_number_whitelist');

COMMIT;

