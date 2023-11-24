--liquibase formatted sql

--changeset bertalan.pasztor:CUSTOMER_MEDIA-DDL-MLFFDEV-17047-01
--comment Add new column media_size.
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

ALTER TABLE customer_media ADD media_size varchar(30) NULL;
COMMENT ON COLUMN customer_media.media_size IS 'Size of image';

UPDATE customer_media SET media_size = 'ORIGINAL';
ALTER TABLE customer_media ALTER COLUMN media_size SET NOT NULL;

ALTER TABLE customer_media ADD CONSTRAINT ck_custmed_media_size
CHECK (((media_size)::text = ANY (ARRAY[
  ('ORIGINAL')::text, 
	('MEDIUM')::text, 
	('SMALL')::text
	])))
NOT VALID;

ALTER TABLE customer_media VALIDATE CONSTRAINT ck_custmed_media_size;

DROP INDEX IF EXISTS ixuk_custmed_custid_doctype;
CREATE UNIQUE INDEX uk_custmed_custid_doctype_medsize ON customer_media USING btree (customer_id, customer_document_type, media_size);

COMMIT;



