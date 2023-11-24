--liquibase formatted sql
--changeset bertalan.pasztor:firebase_token$hist_PART-DDL endDelimiter:/
--comment MLFFSUP-6021 Partition firebase_token$hist table monthly
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$ 
DECLARE
  stmt TEXT;
  tablename TEXT := 'customer.firebase_token$hist';
  newmonthstr TEXT;
BEGIN
ALTER TABLE customer."firebase_token$hist" DROP CONSTRAINT "ck_firebase_token$hist_op";
ALTER TABLE customer."firebase_token$hist" DROP CONSTRAINT "pk_firebase_token$hist";
ALTER TABLE customer."firebase_token$hist" RENAME TO "firebase_token$hist_p2020_01";
  
CREATE TABLE customer."firebase_token$hist" (
	x__hist_ts timestamptz(6) NOT NULL DEFAULT clock_timestamp(), -- History timestamp, the moment of the DML operation.
	x__hist_state varchar(1) NOT NULL, -- History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).
	x__id varchar(30) NOT NULL, -- Logged field: Unique identifier
	x__insdate timestamptz(6) NULL, -- Logged field: Date of creation
	x__insuser varchar(30) NULL, -- Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Logged field: Date of last modification
	x__moduser varchar(30) NULL, -- Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NULL, -- Logged field: Versioning of changes
	firebase_token text NULL, -- Logged field: Firebase token in raw type
	status varchar(30) NULL, -- Logged field: The status of Firebase token ("ACTIVE", "INACTIVE")
--	CONSTRAINT "ck_firebase_token$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[]))),
	CONSTRAINT "pk_firebase_token$hist" PRIMARY KEY (x__id, x__hist_ts)
) PARTITION BY RANGE (x__hist_ts);

COMMENT ON TABLE customer."firebase_token$hist" IS 'History table, source description: This table contains the stored firebase token for session of user. ';

-- Column comments

COMMENT ON COLUMN customer."firebase_token$hist".x__hist_ts IS 'History timestamp, the moment of the DML operation.';
COMMENT ON COLUMN customer."firebase_token$hist".x__hist_state IS 'History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).';
COMMENT ON COLUMN customer."firebase_token$hist".x__id IS 'Logged field: Unique identifier';
COMMENT ON COLUMN customer."firebase_token$hist".x__insdate IS 'Logged field: Date of creation';
COMMENT ON COLUMN customer."firebase_token$hist".x__insuser IS 'Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."firebase_token$hist".x__moddate IS 'Logged field: Date of last modification';
COMMENT ON COLUMN customer."firebase_token$hist".x__moduser IS 'Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."firebase_token$hist".x__version IS 'Logged field: Versioning of changes';
COMMENT ON COLUMN customer."firebase_token$hist".firebase_token IS 'Logged field: Firebase token in raw type';
COMMENT ON COLUMN customer."firebase_token$hist".status IS 'Logged field: The status of Firebase token ("ACTIVE", "INACTIVE")';

GRANT SELECT ON TABLE customer.firebase_token$hist TO customer_sel;


  newmonthstr := TO_CHAR(CURRENT_TIMESTAMP + INTERVAL '1' month, 'yyyy-mm');
  stmt := 'ALTER TABLE ' || tablename 
    || ' ATTACH PARTITION ' || tablename ||'_p2020_01'
    || ' FOR VALUES FROM (''2020-01-01 00:00:00+01'') TO ('''||newmonthstr || '-01 00:00:00+01'')'; 
  EXECUTE stmt;

-- create partitions
PERFORM partman.create_parent(
  p_parent_table => 'customer.firebase_token$hist',
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
WHERE parent_table = 'customer.firebase_token$hist';
  
ALTER TABLE "firebase_token$hist" ADD CONSTRAINT "ck_firebase_token$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[])));
  
END
$$;
/


COMMIT;
