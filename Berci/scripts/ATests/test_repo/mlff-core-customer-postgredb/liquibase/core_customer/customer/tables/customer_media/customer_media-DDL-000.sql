--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CUSTOMER_MEDIA-TBL-MLFFDEV-8134-01
--comment A customer_media tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = 'customer' AND tablename = 'customer_media'
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

CREATE TABLE customer_media (
	x__id varchar(30) NOT NULL, -- Unique identifier
	x__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date of creation
	x__insuser varchar(30) NOT NULL, -- Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Date of last modification
	x__moduser varchar(30) NULL, -- Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NOT NULL DEFAULT 0, -- Versioning of changes
	customer_id varchar(30) NOT NULL, -- Unique identifier of CUSTOMER (FK)
	document_id varchar(30) NOT NULL, -- Unique identifier of a document
	customer_document_type varchar(30) NOT NULL DEFAULT 'PROFILE_PICTURE'::character varying, -- Customer document's type ["PROFILE_PICTURE", "ID_CARD_FRONT_SIDE", "ID_CARD_BACK_SIDE"]
	document_name varchar(250) NOT NULL, -- Name of the document
	document_extension varchar(30) NOT NULL, -- Extension of the document
	CONSTRAINT ck_custmed_doctype CHECK (((customer_document_type)::text = ANY (ARRAY[('PROFILE_PICTURE'::character varying)::text, ('ID_CARD_FRONT_SIDE'::character varying)::text, ('ID_CARD_BACK_SIDE'::character varying)::text]))),
	CONSTRAINT pk_customer_media PRIMARY KEY (x__id),
	CONSTRAINT fk_custmed_cust_id FOREIGN KEY (customer_id) REFERENCES customer(x__id) ON DELETE CASCADE ON UPDATE RESTRICT DEFERRABLE
);
CREATE UNIQUE INDEX ixuk_custmed_custid_doctype ON customer_media USING btree (customer_id, customer_document_type);
COMMENT ON TABLE customer_media IS 'This table is for the customer media data. It contains information about which customer is related to which document and other data related to the document which''s id is stored. ';

-- Column comments

COMMENT ON COLUMN customer_media.x__id IS 'Unique identifier';
COMMENT ON COLUMN customer_media.x__insdate IS 'Date of creation';
COMMENT ON COLUMN customer_media.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_media.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN customer_media.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer_media.x__version IS 'Versioning of changes';
COMMENT ON COLUMN customer_media.customer_id IS 'Unique identifier of CUSTOMER (FK)';
COMMENT ON COLUMN customer_media.document_id IS 'Unique identifier of a document';
COMMENT ON COLUMN customer_media.customer_document_type IS 'Customer document''s type ["PROFILE_PICTURE", "ID_CARD_FRONT_SIDE", "ID_CARD_BACK_SIDE"]';
COMMENT ON COLUMN customer_media.document_name IS 'Name of the document';
COMMENT ON COLUMN customer_media.document_extension IS 'Extension of the document';

-- GRANT ==
call add_privileges_to_table('${schema_name}', 'customer_media');

COMMIT;

