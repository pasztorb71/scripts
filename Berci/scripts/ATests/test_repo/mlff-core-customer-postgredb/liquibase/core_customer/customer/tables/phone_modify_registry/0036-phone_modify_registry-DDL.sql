--liquibase formatted sql

--changeset bertalan.pasztor:0036-PHONE_MODIFY_REGISTRY-TBL
--comment MLFFSUP-6059 phone_modify_registry tábla létrehozása..
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE phone_modify_registry (
	x__id varchar(30) NOT NULL,
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	x__insuser varchar(30) NOT NULL,
	x__moddate timestamptz(6) NULL,
	x__moduser varchar(30) NULL,
	x__version int8 NOT NULL DEFAULT 0,
	customer_id varchar(30) NOT NULL,
	phone_number varchar(30) NOT NULL,
	message_to_stream varchar(100) NOT NULL,
	message_to_stream_datetime timestamptz(6) NOT NULL,
	message_from_stream varchar(100) NULL,
	message_from_stream_datetime timestamptz(6) NULL,
	CONSTRAINT pk_phone_modify_registry PRIMARY KEY (x__id),
	CONSTRAINT fk_phomodreg_customer_id FOREIGN KEY (customer_id) REFERENCES customer(x__id)
);

CREATE INDEX ix_phomodreg_customer_id ON phone_modify_registry USING btree (customer_id);

COMMENT ON TABLE phone_modify_registry IS 'to record the comunication with the payment module (can be used to track other communications in the future)';

-- Column comments

COMMENT ON COLUMN phone_modify_registry.x__id IS 'Unique identifier';
COMMENT ON COLUMN phone_modify_registry.x__insdate IS 'Date of creation';
COMMENT ON COLUMN phone_modify_registry.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN phone_modify_registry.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN phone_modify_registry.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN phone_modify_registry.x__version IS 'Versioning of changes';
COMMENT ON COLUMN phone_modify_registry.customer_id IS 'Unique identifier of CUSTOMER (FK)';
COMMENT ON COLUMN phone_modify_registry.phone_number IS 'The verified new phoneNumber.';
COMMENT ON COLUMN phone_modify_registry.message_to_stream IS 'Name of the stream where the message was placed';
COMMENT ON COLUMN phone_modify_registry.message_to_stream_datetime IS 'Timestamp when the message was placed on the stream';
COMMENT ON COLUMN phone_modify_registry.message_from_stream IS 'Name of the stream where the message was placed';
COMMENT ON COLUMN phone_modify_registry.message_from_stream_datetime IS 'Timestamp when the message was placed on the stream';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'phone_modify_registry');

COMMIT;
