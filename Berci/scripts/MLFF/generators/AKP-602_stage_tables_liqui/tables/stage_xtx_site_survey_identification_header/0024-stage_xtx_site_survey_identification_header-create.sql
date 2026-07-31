--liquibase formatted sql

--changeset bertalan.pasztor:0024
--comment AKP-602 stage_xtx_site_survey_identification_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_site_survey_identification_header (
   xtx_site_survey_identification_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   site_identification integer,
   survey_identification integer,
   route varchar,
   distance_location double,
   type_of_site varchar,
   law_enforcement_activity varchar,
   location_description varchar
);




-- lakehouse.prototype_landing.xtx_speed_summary_20_data definition


