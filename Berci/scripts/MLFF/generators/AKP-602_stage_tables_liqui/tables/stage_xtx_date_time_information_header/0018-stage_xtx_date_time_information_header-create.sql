--liquibase formatted sql

--changeset bertalan.pasztor:0018
--comment AKP-602 stage_xtx_date_time_information_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_date_time_information_header (
   xtx_date_time_information_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   starting_date timestamp(6),
   end_date timestamp(6),
   setup_date timestamp(6),
   hist_start_date timestamp(6),
   hist_end_date timestamp(6)
);


