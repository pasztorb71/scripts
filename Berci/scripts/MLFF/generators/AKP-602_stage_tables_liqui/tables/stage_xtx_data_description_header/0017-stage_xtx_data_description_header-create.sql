--liquibase formatted sql

--changeset bertalan.pasztor:0017
--comment AKP-602 stage_xtx_data_description_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_data_description_header (
   xtx_data_description_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   description varchar
);




