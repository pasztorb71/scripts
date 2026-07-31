--liquibase formatted sql

--changeset bertalan.pasztor:0030
--comment AKP-602 stage_xtx_summary_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_summary_header (
   xtx_summary_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   smallest_summary_interval varchar,
   largest_summary_interval varchar,
   units varchar,
   programmable_headway_bin integer,
   vehicle_classification_scheme varchar,
   number_of_vehicle_classes_in_classification_schema integer,
   number_of_sensors_per_lane integer,
   number_of_bins integer,
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
);




