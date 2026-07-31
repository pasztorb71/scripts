--liquibase formatted sql

--changeset bertalan.pasztor:0020
--comment AKP-602 stage_xtx_lane_configuration_header tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_lane_configuration_header (
   xtx_lane_configuration_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   physical_lane_number_label varchar,
   direction_code integer,
   lane_position_code integer,
   reverse_logical_lane_number_label varchar,
   vehicle_code integer,
   time_code integer,
   length_code integer,
   speed_code integer,
   axle_code integer,
   mass_code integer,
   sensor_spacing varchar,
   length_correction varchar,
   sensor_channel_number varchar
);


