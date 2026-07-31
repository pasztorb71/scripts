--liquibase formatted sql

--changeset bertalan.pasztor:0029
--comment AKP-602 stage_xtx_summary_data tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_summary_data (
   xtx_summary_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   end_date timestamp(6),
   duration integer,
   logical_lane_number varchar,
   physical_lane_number varchar,
   bin_value_1 integer,
   bin_value_2 integer,
   bin_value_3 integer,
   bin_value_4 integer,
   bin_value_5 integer,
   bin_value_6 integer,
   bin_value_7 integer,
   bin_value_8 integer,
   bin_value_9 integer,
   bin_value_10 integer,
   bin_value_11 integer,
   bin_value_12 integer,
   bin_value_13 integer,
   bin_value_14 integer,
   bin_value_15 integer,
   bin_value_16 integer,
   bin_value_17 integer,
   bin_value_18 integer,
   bin_value_19 integer,
   bin_value_20 integer
)
;




