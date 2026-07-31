--liquibase formatted sql

--changeset bertalan.pasztor:0031
--comment AKP-602 stage_xtx_vehicle_data tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_vehicle_data (
   xtx_vehicle_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   departure timestamp(6),
   logical_lane_number varchar,
   physical_lane_number varchar,
   direction_code varchar,
   occupancy_time varchar,
   speed integer,
   length integer,
   chassis_height_code integer,
   tag_code integer,
   failure_code integer,
   vehicle_class_code integer,
   icode varchar,
   axle_pattern_code varchar,
   number_of_axles integer
);



