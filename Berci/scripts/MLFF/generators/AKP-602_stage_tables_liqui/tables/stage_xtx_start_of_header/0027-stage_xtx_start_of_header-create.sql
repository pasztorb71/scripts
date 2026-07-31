--liquibase formatted sql

--changeset bertalan.pasztor:0027
--comment AKP-602 stage_xtx_start_of_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_start_of_header (
   xtx_start_of_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   data_format_version varchar,
   data_compatibility_code varchar,
   description varchar
);


