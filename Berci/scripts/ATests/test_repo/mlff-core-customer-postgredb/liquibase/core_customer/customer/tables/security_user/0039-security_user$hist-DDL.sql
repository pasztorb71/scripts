--liquibase formatted sql
--changeset bertalan.pasztor:security_user$hist_PART-DDL endDelimiter:/
--comment MLFFSUP-6021 Partition security_user$hist table monthly
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$ 
DECLARE
  stmt TEXT;
  tablename TEXT := 'customer.security_user$hist';
  newmonthstr TEXT;
BEGIN
ALTER TABLE customer."security_user$hist" DROP CONSTRAINT "ck_security_user$hist_op";
ALTER TABLE customer."security_user$hist" DROP CONSTRAINT "pk_security_user$hist";
ALTER TABLE customer."security_user$hist" RENAME TO "security_user$hist_p2020_01";
  
CREATE TABLE customer."security_user$hist" (
	x__hist_ts timestamptz(6) NOT NULL DEFAULT clock_timestamp(), -- History timestamp, the moment of the DML operation.
	x__hist_state varchar(1) NOT NULL, -- History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).
	x__id varchar(30) NOT NULL, -- Logged field: Unique identifier
	x__insdate timestamptz(6) NULL, -- Logged field: Date of creation
	x__insuser varchar(30) NULL, -- Logged field: Unique identifier of creator user
	x__moddate timestamptz(6) NULL, -- Logged field: Date of last modification
	x__moduser varchar(30) NULL, -- Logged field: Unique identifier of modifier user
	x__version int8 NULL, -- Logged field: Versioning of changes
	username varchar(32) NULL, -- Logged field: Login name of the user
	"password" varchar(255) NULL, -- Logged field: Hash value of the user"s password
	active bool NULL, -- Logged field: Security user"s status. ( Active or not active)
--	CONSTRAINT "ck_security_user$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[]))),
	CONSTRAINT "pk_security_user$hist" PRIMARY KEY (x__id, x__hist_ts)
) PARTITION BY RANGE (x__hist_ts);

COMMENT ON TABLE customer."security_user$hist" IS 'History table, source description: Contains user data what we need, to authorize the user. ';

-- Column comments

COMMENT ON COLUMN customer."security_user$hist".x__hist_ts IS 'History timestamp, the moment of the DML operation.';
COMMENT ON COLUMN customer."security_user$hist".x__hist_state IS 'History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).';
COMMENT ON COLUMN customer."security_user$hist".x__id IS 'Logged field: Unique identifier';
COMMENT ON COLUMN customer."security_user$hist".x__insdate IS 'Logged field: Date of creation';
COMMENT ON COLUMN customer."security_user$hist".x__insuser IS 'Logged field: Unique identifier of creator user';
COMMENT ON COLUMN customer."security_user$hist".x__moddate IS 'Logged field: Date of last modification';
COMMENT ON COLUMN customer."security_user$hist".x__moduser IS 'Logged field: Unique identifier of modifier user';
COMMENT ON COLUMN customer."security_user$hist".x__version IS 'Logged field: Versioning of changes';
COMMENT ON COLUMN customer."security_user$hist".username IS 'Logged field: Login name of the user';
COMMENT ON COLUMN customer."security_user$hist"."password" IS 'Logged field: Hash value of the user"s password';
COMMENT ON COLUMN customer."security_user$hist".active IS 'Logged field: Security user"s status. ( Active or not active)';

GRANT SELECT ON TABLE customer.security_user$hist TO customer_sel;


  newmonthstr := TO_CHAR(CURRENT_TIMESTAMP + INTERVAL '1' month, 'yyyy-mm');
  stmt := 'ALTER TABLE ' || tablename 
    || ' ATTACH PARTITION ' || tablename ||'_p2020_01'
    || ' FOR VALUES FROM (''2020-01-01 00:00:00+01'') TO ('''||newmonthstr || '-01 00:00:00+01'')'; 
  EXECUTE stmt;

-- create partitions
PERFORM partman.create_parent(
  p_parent_table => 'customer.security_user$hist',
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
WHERE parent_table = 'customer.security_user$hist';
  
ALTER TABLE "security_user$hist" ADD CONSTRAINT "ck_security_user$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[])));
  
END
$$;
/


COMMIT;
