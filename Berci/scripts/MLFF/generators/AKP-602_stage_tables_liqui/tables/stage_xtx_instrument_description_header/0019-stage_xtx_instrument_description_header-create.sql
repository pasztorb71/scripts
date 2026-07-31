--liquibase formatted sql

--changeset bertalan.pasztor:0019
--comment AKP-602 stage_xtx_instrument_description_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_instrument_description_header (
   xtx_instrument_description_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   first_lane_number varchar,
   last_lane_number varchar,
   instrument_type varchar,
   instrument_version varchar,
   instrument_serial_num varchar,
   data_translation_software_version varchar,
   data_extraction_tool varchar
);

--atnezni

