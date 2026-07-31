--liquibase formatted sql

--changeset bertalan.pasztor:0023
--comment AKP-602 stage_xtx_sensor_description_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_sensor_description_header (
   xtx_sensor_description_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   lane_number varchar,
   sensor_type_code varchar,
   manufacturer varchar,
   sensor_type_name varchar,
   sensor_serial_number varchar,
   comments varchar
);



-- lakehouse.prototype_consolidated_old.stage_xtx_site_survey_identification_header definition


