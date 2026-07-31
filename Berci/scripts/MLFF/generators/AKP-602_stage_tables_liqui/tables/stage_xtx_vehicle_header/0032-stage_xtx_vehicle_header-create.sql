--liquibase formatted sql

--changeset bertalan.pasztor:0032
--comment AKP-602 stage_xtx_vehicle_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_vehicle_header (
   xtx_vehicle_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   units varchar,
   type_of_vehicles_recorded integer, 
   vehicle_classification_scheme varchar,
   number_of_vehicle_classes integer,
   departure_time_accuracy_code integer,
   max_number_of_axles integer,
   loop_spacing varchar,
   prev_vehicle_reference_number varchar
);





