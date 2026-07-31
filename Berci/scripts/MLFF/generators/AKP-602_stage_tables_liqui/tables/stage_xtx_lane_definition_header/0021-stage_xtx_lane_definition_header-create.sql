--liquibase formatted sql

--changeset bertalan.pasztor:0021
--comment AKP-602 stage_xtx_lane_definition_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_lane_definition_header (
   xtx_lane_definition_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   number_of_logical_lanes integer,
   number_of_physical_lanes integer,
   drive_convention varchar,
   units varchar
);



