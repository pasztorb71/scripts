--liquibase formatted sql

--changeset bertalan.pasztor:0026
--comment AKP-602 stage_xtx_speed_summary_23_data tábla_létrehozása

CREATE TABLE ${schema_name}.stage_xtx_speed_summary_23_data (
   xtx_speed_summary_23_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   end_date timestamp(6),
   duration integer,
   logical_lane_number varchar,
   num_of_light_vehicles_in_speed_bin_1 integer,
   num_of_light_vehicles_in_speed_bin_2 integer,
   num_of_light_vehicles_in_speed_bin_3 integer,
   num_of_light_vehicles_in_speed_bin_4 integer,
   num_of_light_vehicles_in_speed_bin_5 integer,
   num_of_light_vehicles_in_speed_bin_6 integer,
   num_of_light_vehicles_in_speed_bin_7 integer,
   num_of_light_vehicles_in_speed_bin_8 integer,
   num_of_light_vehicles_in_speed_bin_9 integer,
   num_of_light_vehicles_in_speed_bin_10 integer,
   num_of_heavy_vehicles_in_speed_bin_1 integer,
   num_of_heavy_vehicles_in_speed_bin_2 integer,
   num_of_heavy_vehicles_in_speed_bin_3 integer,
   num_of_heavy_vehicles_in_speed_bin_4 integer,
   num_of_heavy_vehicles_in_speed_bin_5 integer,
   num_of_heavy_vehicles_in_speed_bin_6 integer,
   num_of_heavy_vehicles_in_speed_bin_7 integer,
   num_of_heavy_vehicles_in_speed_bin_8 integer,
   num_of_heavy_vehicles_in_speed_bin_9 integer,
   num_of_heavy_vehicles_in_speed_bin_10 integer,
   num_of_medium_heavy_vehicles integer,
   num_of_long_heavy_vehicles integer,
   num_of_headway_shorter_than2sec integer
);


