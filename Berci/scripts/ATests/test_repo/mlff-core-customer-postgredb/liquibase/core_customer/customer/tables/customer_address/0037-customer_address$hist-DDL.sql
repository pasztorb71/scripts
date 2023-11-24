--liquibase formatted sql
--changeset bertalan.pasztor:CUSTOMER_ADDRESS$HIST_PART-DDL endDelimiter:/
--comment MLFFSUP-6021 Partition customer_address$hist table monthly
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$ 
DECLARE
  stmt TEXT;
  tablename TEXT := 'customer.customer_address$hist';
  newmonthstr TEXT;
BEGIN
ALTER TABLE customer."customer_address$hist" DROP CONSTRAINT "ck_customer_address$hist_op";
ALTER TABLE customer."customer_address$hist" DROP CONSTRAINT "pk_customer_address$hist";
ALTER TABLE customer."customer_address$hist" RENAME TO "customer_address$hist_p2020_01";
  
CREATE TABLE customer."customer_address$hist" (
	x__hist_ts timestamptz(6) NOT NULL DEFAULT clock_timestamp(), -- History timestamp, the moment of the DML operation.
	x__hist_state varchar(1) NOT NULL, -- History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).
	x__id varchar(30) NOT NULL, -- Logged field: Unique identifier
	x__insdate timestamptz(6) NULL, -- Logged field: Date of creation
	x__insuser varchar(30) NULL, -- Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Logged field: Date of last modification
	x__moduser varchar(30) NULL, -- Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NULL, -- Logged field: Versioning of changes
	customer_id varchar(30) NULL, -- Logged field: Unique identifier of CUSTOMER (FK)
	postal_code varchar(5) NULL, -- Logged field: Postal code. It can only contain numbers from 0 to 9 as value.
	province varchar(64) NULL, -- Logged field: Province.
	district varchar(128) NULL, -- Logged field: District.
	subdistrict varchar(128) NULL, -- Logged field: Subdistrict.
	city varchar(64) NULL, -- Logged field: City.
	address_line varchar(255) NULL, -- Logged field: Address line.
--	CONSTRAINT "ck_customer_address$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[]))),
	CONSTRAINT "pk_customer_address$hist" PRIMARY KEY (x__id, x__hist_ts)
) PARTITION BY RANGE (x__hist_ts);

COMMENT ON TABLE customer."customer_address$hist" IS 'History table, source description: This table is for storing customer address data.  ';

-- Column comments

COMMENT ON COLUMN customer."customer_address$hist".x__hist_ts IS 'History timestamp, the moment of the DML operation.';
COMMENT ON COLUMN customer."customer_address$hist".x__hist_state IS 'History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).';
COMMENT ON COLUMN customer."customer_address$hist".x__id IS 'Logged field: Unique identifier';
COMMENT ON COLUMN customer."customer_address$hist".x__insdate IS 'Logged field: Date of creation';
COMMENT ON COLUMN customer."customer_address$hist".x__insuser IS 'Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."customer_address$hist".x__moddate IS 'Logged field: Date of last modification';
COMMENT ON COLUMN customer."customer_address$hist".x__moduser IS 'Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."customer_address$hist".x__version IS 'Logged field: Versioning of changes';
COMMENT ON COLUMN customer."customer_address$hist".customer_id IS 'Logged field: Unique identifier of CUSTOMER (FK)';
COMMENT ON COLUMN customer."customer_address$hist".postal_code IS 'Logged field: Postal code. It can only contain numbers from 0 to 9 as value.';
COMMENT ON COLUMN customer."customer_address$hist".province IS 'Logged field: Province.';
COMMENT ON COLUMN customer."customer_address$hist".district IS 'Logged field: District.';
COMMENT ON COLUMN customer."customer_address$hist".subdistrict IS 'Logged field: Subdistrict.';
COMMENT ON COLUMN customer."customer_address$hist".city IS 'Logged field: City.';
COMMENT ON COLUMN customer."customer_address$hist".address_line IS 'Logged field: Address line.';

GRANT SELECT ON TABLE customer.customer_address$hist TO customer_sel;


  newmonthstr := TO_CHAR(CURRENT_TIMESTAMP + INTERVAL '1' month, 'yyyy-mm');
  stmt := 'ALTER TABLE ' || tablename 
    || ' ATTACH PARTITION ' || tablename ||'_p2020_01'
    || ' FOR VALUES FROM (''2020-01-01 00:00:00+01'') TO ('''||newmonthstr || '-01 00:00:00+01'')'; 
  EXECUTE stmt;

-- create partitions
PERFORM partman.create_parent(
  p_parent_table => 'customer.customer_address$hist',
  p_control => 'x__hist_ts',
  p_type => 'native',
  p_interval=> 'monthly',
  p_premake => 5,
  p_start_partition => (now() + INTERVAL '1' month)::text
);

-- part maintenance
UPDATE partman.part_config
SET infinite_time_partitions = true,
    retention = null,
    retention_keep_table=true
WHERE parent_table = 'customer.customer_address$hist';
  
ALTER TABLE "customer_address$hist" ADD CONSTRAINT "ck_customer_address$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[])));
  
END
$$;
COMMIT;
/


