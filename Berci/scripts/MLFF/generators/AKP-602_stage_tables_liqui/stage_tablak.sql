
CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_data_description_header (
   xtx_data_description_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   description varchar
);



CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_date_time_information_header (
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

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_instrument_description_header (
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
CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_lane_configuration_header (
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

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_lane_definition_header (
   xtx_lane_definition_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   number_of_logical_lanes integer,
   number_of_physical_lanes integer,
   drive_convention varchar,
   units varchar
);


CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_mass_and_axle_spacing_data (
   xtx_mass_and_axle_spacing_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   departure  timestamp(6),
   logical_lane_number varchar,   
   physical_lane_number varchar,
   direction_code integer,
   speed integer,
   length integer,
   chassis_height_code integer,
   tag_code integer,
   failure_code integer,
   vehicle_class_code integer,
   axle_pattern_code integer,
   number_of_axles integer,
   axle_spacing_1 integer,
   axle_spacing_2 integer,
   axle_spacing_3 integer,
   axle_spacing_4 integer,
   axle_spacing_5 integer,
   axle_spacing_6 integer,
   axle_spacing_7 integer,
   axle_spacing_8 integer,
   axle_spacing_9 integer,
   axle_spacing_10 integer,
   axle_spacing_11 integer,
   axle_spacing_12 integer,
   axle_spacing_13 integer,
   axle_spacing_14 integer,
   axle_spacing_15 integer,
   axle_spacing_16 integer,
   axle_spacing_17 integer,
   axle_spacing_18 integer,
   axle_spacing_19 integer,
   axle_spacing_20 integer,
   axle_weight_1 integer,
   axle_weight_2 integer,
   axle_weight_3 integer,
   axle_weight_4 integer,
   axle_weight_5 integer,
   axle_weight_6 integer,
   axle_weight_7 integer,
   axle_weight_8 integer,
   axle_weight_9 integer,
   axle_weight_10 integer,
   axle_weight_11 integer,
   axle_weight_12 integer,
   axle_weight_13 integer,
   axle_weight_14 integer,
   axle_weight_15 integer,
   axle_weight_16 integer,
   axle_weight_17 integer,
   axle_weight_18 integer,
   axle_weight_19 integer,
   axle_weight_20 integer,
   sensor_temperature integer
);

-- lakehouse.prototype_landing.xtx_sensor_description_header definition

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_sensor_description_header (
   xtx_sensor_description_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   lane_number varchar,
   sensor_type_code varchar,
   manufacturer varchar,
   sensor_type_name varchar,
   sensor_serial_number varchar,
   comments varchar
);



-- lakehouse.prototype_consolidated_old.stage_xtx_site_survey_identification_header definition

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_site_survey_identification_header (
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

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_speed_summary_20_data (
   xtx_speed_summary_20_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   end_date timestamp(6),
   duration integer,
   logical_lane_number varchar,
   number_in_speed_bin_1 integer,
   number_in_speed_bin_2 integer,
   number_in_speed_bin_3 integer,
   number_in_speed_bin_4 integer,
   number_in_speed_bin_5 integer,
   number_in_speed_bin_6 integer,
   number_in_speed_bin_7 integer,
   number_in_speed_bin_8 integer,
   number_in_speed_bin_9 integer,
   number_in_speed_bin_10 integer,
   sum_of_heavy_vehicles_speed integer,
   num_of_short_heavy_vehicles integer,
   num_of_medium_heavy_vehicles integer,
   num_of_long_heavy_vehicles integer,
   num_of_headway_shorter_than2sec integer,
   num_of_headway_shorter_than_prog_headway integer
);

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_speed_summary_23_data (
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

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_start_of_header (
   xtx_start_of_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   data_format_version varchar,
   data_compatibility_code varchar,
   description varchar
);

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_status_report_data (
   xtx_status_report_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   report_date timestamp(6),
   report_type varchar,
   equipment_error_code varchar,
   number_of_sensors integer,
   logger_voltage integer,
   temperature_correction_factor varchar,
   sensor_value_1 varchar,
   sensor_value_2 varchar,
   sensor_value_3 varchar,
   sensor_value_4 varchar,
   sensor_value_5 varchar,
   sensor_value_6 varchar,
   sensor_value_7 varchar,
   sensor_value_8 varchar,
   sensor_value_9 varchar,
   sensor_value_10 varchar,
   sensor_value_11 varchar,
   sensor_value_12 varchar,
   sensor_value_13 varchar,
   sensor_value_14 varchar,
   sensor_value_15 varchar
);

CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_summary_data (
   xtx_summary_data_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   edit_code varchar,
   end_date timestamp(6),
   duration integer,
   logical_lane_number varchar,
   physical_lane_number varchar,
   bin_value_1 integer,
   bin_value_2 integer,
   bin_value_3 integer,
   bin_value_4 integer,
   bin_value_5 integer,
   bin_value_6 integer,
   bin_value_7 integer,
   bin_value_8 integer,
   bin_value_9 integer,
   bin_value_10 integer,
   bin_value_11 integer,
   bin_value_12 integer,
   bin_value_13 integer,
   bin_value_14 integer,
   bin_value_15 integer,
   bin_value_16 integer,
   bin_value_17 integer,
   bin_value_18 integer,
   bin_value_19 integer,
   bin_value_20 integer
)
;



CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_summary_header (
   xtx_summary_header_id varchar,
   md_load_header_id varchar,
   md_insert_ts timestamp(6),
   data_line_identifier varchar,
   smallest_summary_interval varchar,
   largest_summary_interval varchar,
   units varchar,
   programmable_headway_bin integer,
   vehicle_classification_scheme varchar,
   number_of_vehicle_classes_in_classification_schema integer,
   number_of_sensors_per_lane integer,
   number_of_bins integer,
   bin_value_1 integer,
   bin_value_2 integer,
   bin_value_3 integer,
   bin_value_4 integer,
   bin_value_5 integer,
   bin_value_6 integer,
   bin_value_7 integer,
   bin_value_8 integer,
   bin_value_9 integer,
   bin_value_10 integer,
   bin_value_11 integer,
   bin_value_12 integer,
   bin_value_13 integer,
   bin_value_14 integer,
   bin_value_15 integer,
   bin_value_16 integer,
   bin_value_17 integer,
   bin_value_18 integer,
   bin_value_19 integer,
   bin_value_20 integer
);



CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_vehicle_data (
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


CREATE TABLE lakehouse.prototype_consolidated.stage_xtx_vehicle_header (
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




