--liquibase formatted sql
--changeset bertalan.pasztor:verification_code$hist_PART-DDL endDelimiter:/
--comment MLFFSUP-6021 Partition verification_code$hist table monthly
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

DO $$ 
DECLARE
  stmt TEXT;
  tablename TEXT := 'customer.verification_code$hist';
  newmonthstr TEXT;
BEGIN
ALTER TABLE customer."verification_code$hist" DROP CONSTRAINT "ck_verification_code$hist_op";
ALTER TABLE customer."verification_code$hist" DROP CONSTRAINT "pk_verification_code$hist";
ALTER TABLE customer."verification_code$hist" RENAME TO "verification_code$hist_p2020_01";
  
CREATE TABLE customer."verification_code$hist" (
	x__hist_ts timestamptz(6) NOT NULL DEFAULT clock_timestamp(), -- History timestamp, the moment of the DML operation.
	x__hist_state varchar(1) NOT NULL, -- History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).
	x__id varchar(30) NOT NULL, -- Logged field: Unique identifier
	x__insdate timestamptz(6) NULL, -- Logged field: Date of creation
	x__insuser varchar(30) NULL, -- Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__moddate timestamptz(6) NULL, -- Logged field: Date of last modification
	x__moduser varchar(30) NULL, -- Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)
	x__version int8 NULL, -- Logged field: Versioning of changes
	customer_id varchar(30) NULL, -- Logged field: Unique identifier of customer (FK)
	subject_value varchar(255) NULL, -- Logged field: Phone number or Email address
	code varchar(30) NULL, -- Logged field: Generated code
	code_expiry timestamptz(6) NULL, -- Logged field: Expiration date
	subject_type varchar(30) NULL, -- Logged field: The subject to be verified by the code ("EMAIL", "PHONE")
	number_of_attempts_resend int4 NULL, -- Logged field: Number of attempts verification code resend
	reserved_ttl timestamptz(6) NULL,
	number_of_attempt int4 NOT NULL DEFAULT 0, -- Logged field: Number of attempts verification code get with wrong
--	CONSTRAINT "ck_verification_code$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[]))),
	CONSTRAINT "pk_verification_code$hist" PRIMARY KEY (x__id, x__hist_ts)
) PARTITION BY RANGE (x__hist_ts);
COMMENT ON TABLE customer."verification_code$hist" IS 'History table, source description: This table contains the generated code and its properties for the verification process. ';

-- Column comments

COMMENT ON COLUMN customer."verification_code$hist".x__hist_ts IS 'History timestamp, the moment of the DML operation.';
COMMENT ON COLUMN customer."verification_code$hist".x__hist_state IS 'History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).';
COMMENT ON COLUMN customer."verification_code$hist".x__id IS 'Logged field: Unique identifier';
COMMENT ON COLUMN customer."verification_code$hist".x__insdate IS 'Logged field: Date of creation';
COMMENT ON COLUMN customer."verification_code$hist".x__insuser IS 'Logged field: Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."verification_code$hist".x__moddate IS 'Logged field: Date of last modification';
COMMENT ON COLUMN customer."verification_code$hist".x__moduser IS 'Logged field: Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN customer."verification_code$hist".x__version IS 'Logged field: Versioning of changes';
COMMENT ON COLUMN customer."verification_code$hist".customer_id IS 'Logged field: Unique identifier of customer (FK)';
COMMENT ON COLUMN customer."verification_code$hist".subject_value IS 'Logged field: Phone number or Email address';
COMMENT ON COLUMN customer."verification_code$hist".code IS 'Logged field: Generated code';
COMMENT ON COLUMN customer."verification_code$hist".code_expiry IS 'Logged field: Expiration date';
COMMENT ON COLUMN customer."verification_code$hist".subject_type IS 'Logged field: The subject to be verified by the code ("EMAIL", "PHONE")';
COMMENT ON COLUMN customer."verification_code$hist".number_of_attempts_resend IS 'Logged field: Number of attempts verification code resend';
COMMENT ON COLUMN customer."verification_code$hist".number_of_attempt IS 'Logged field: Number of attempts verification code get with wrong';

GRANT SELECT ON TABLE customer.verification_code$hist TO customer_sel;


  newmonthstr := TO_CHAR(CURRENT_TIMESTAMP + INTERVAL '1' month, 'yyyy-mm');
  stmt := 'ALTER TABLE ' || tablename 
    || ' ATTACH PARTITION ' || tablename ||'_p2020_01'
    || ' FOR VALUES FROM (''2020-01-01 00:00:00+01'') TO ('''||newmonthstr || '-01 00:00:00+01'')'; 
  EXECUTE stmt;

-- create partitions
PERFORM partman.create_parent(
  p_parent_table => 'customer.verification_code$hist',
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
WHERE parent_table = 'customer.verification_code$hist';
  
ALTER TABLE "verification_code$hist" ADD CONSTRAINT "ck_verification_code$hist_op" CHECK (((x__hist_state)::text = ANY ((ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying])::text[])));
  
END
$$;
/


COMMIT;
