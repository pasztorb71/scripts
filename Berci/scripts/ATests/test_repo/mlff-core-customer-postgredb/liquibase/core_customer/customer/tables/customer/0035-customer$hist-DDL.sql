--liquibase formatted sql
--changeset bertalan.pasztor:CUSTOMER$HIST_PART-DDL endDelimiter:/
--comment MLFFSUP-6021 Partition customer$hist table monthly
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$ 
DECLARE
  stmt TEXT;
  tablename TEXT := 'customer.customer$hist';
  newmonthstr TEXT;
BEGIN
ALTER TABLE customer."customer$hist" DROP CONSTRAINT "ck_customer$hist_op";
ALTER TABLE customer."customer$hist" DROP CONSTRAINT "pk_customer$hist";
ALTER TABLE customer."customer$hist" RENAME TO "customer$hist_p2020_01";
  
CREATE TABLE customer."customer$hist" (
  x__hist_ts timestamptz(6) NOT NULL DEFAULT clock_timestamp(), -- History timestamp, the moment of the DML operation.
  x__hist_state varchar(1) NOT NULL, -- History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).
  x__id varchar(30) NOT NULL, -- Logged field: Unique identifier
  x__insdate timestamptz(6) NULL, -- Logged field: Date of creation
  x__insuser varchar(30) NULL, -- Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
  x__moddate timestamptz(6) NULL, -- Logged field: Date of last modification
  x__moduser varchar(30) NULL, -- Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
  x__version int8 NULL, -- Logged field: Versioning of changes
  customer_name varchar(200) NULL, -- Logged field: Customer"s name
  date_of_birth date NULL, -- Logged field: Customer"s birthday
  phone_number varchar(30) NULL, -- Logged field: Customer"s phone number
  email varchar(200) NULL, -- Logged field: Customer"s email address
  customer_status varchar(30) NULL, -- Logged field: Customer's status ["TEMPORARY","ACTIVE", "TO_BE_DELETED", "DELETED" ]
  "language" varchar(10) NULL, -- Logged field: Application language ["ID","EN" ]
  nik_number varchar(16) NULL, -- Logged field: Customer"s NIK number
  deletion_date_time timestamptz(6) NULL, -- Logged field: Customer deletion date time
--  CONSTRAINT "ck_customer$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[]))),
  CONSTRAINT "pk_customer$hist" PRIMARY KEY (x__id, x__hist_ts)
) PARTITION BY RANGE (x__hist_ts);
COMMENT ON TABLE customer."customer$hist" IS 'History table, source description: This table describes the customer itself. ';

-- Column comments

COMMENT ON COLUMN customer."customer$hist".x__hist_ts IS 'History timestamp, the moment of the DML operation.';
COMMENT ON COLUMN customer."customer$hist".x__hist_state IS 'History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).';
COMMENT ON COLUMN customer."customer$hist".x__id IS 'Logged field: Unique identifier';
COMMENT ON COLUMN customer."customer$hist".x__insdate IS 'Logged field: Date of creation';
COMMENT ON COLUMN customer."customer$hist".x__insuser IS 'Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."customer$hist".x__moddate IS 'Logged field: Date of last modification';
COMMENT ON COLUMN customer."customer$hist".x__moduser IS 'Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."customer$hist".x__version IS 'Logged field: Versioning of changes';
COMMENT ON COLUMN customer."customer$hist".customer_name IS 'Logged field: Customer"s name';
COMMENT ON COLUMN customer."customer$hist".date_of_birth IS 'Logged field: Customer"s birthday';
COMMENT ON COLUMN customer."customer$hist".phone_number IS 'Logged field: Customer"s phone number';
COMMENT ON COLUMN customer."customer$hist".email IS 'Logged field: Customer"s email address';
COMMENT ON COLUMN customer."customer$hist".customer_status IS 'Logged field: Customer''s status ["TEMPORARY","ACTIVE", "TO_BE_DELETED", "DELETED" ]';
COMMENT ON COLUMN customer."customer$hist"."language" IS 'Logged field: Application language ["ID","EN" ]';
COMMENT ON COLUMN customer."customer$hist".nik_number IS 'Logged field: Customer"s NIK number';
COMMENT ON COLUMN customer."customer$hist".deletion_date_time IS 'Logged field: Customer deletion date time';

GRANT SELECT ON TABLE customer.customer$hist TO customer_sel;


  newmonthstr := TO_CHAR(CURRENT_TIMESTAMP + INTERVAL '1' month, 'yyyy-mm');
  stmt := 'ALTER TABLE ' || tablename 
    || ' ATTACH PARTITION ' || tablename ||'_p2020_01'
    || ' FOR VALUES FROM (''2020-01-01 00:00:00+01'') TO ('''||newmonthstr || '-01 00:00:00+01'')'; 
  EXECUTE stmt;

-- create partitions
PERFORM partman.create_parent(
  p_parent_table => 'customer.customer$hist',
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
WHERE parent_table = 'customer.customer$hist';
  
ALTER TABLE "customer$hist" ADD  CONSTRAINT "ck_customer$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[])));
  
END
$$;
COMMIT;
/

