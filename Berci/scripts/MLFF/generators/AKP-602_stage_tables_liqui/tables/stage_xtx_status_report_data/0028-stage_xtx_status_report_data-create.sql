--liquibase formatted sql

--changeset bertalan.pasztor:0028
--comment AKP-602 stage_xtx_status_report_data tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_status_report_data (
   xtx_status_report_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   report_date timestamp(6),
   report_type varchar,
   equipment_error_code varchar,
   number_of_sensors integer,
   logger_voltage integer,
   temperature_correction_factor varchar,
   sensor_value_1 varchar,
   sensor_value_2 varchar,
   sensor_value_3 varchar,
   sensor_value_4 varchar,
   sensor_value_5 varchar,
   sensor_value_6 varchar,
   sensor_value_7 varchar,
   sensor_value_8 varchar,
   sensor_value_9 varchar,
   sensor_value_10 varchar,
   sensor_value_11 varchar,
   sensor_value_12 varchar,
   sensor_value_13 varchar,
   sensor_value_14 varchar,
   sensor_value_15 varchar
);


