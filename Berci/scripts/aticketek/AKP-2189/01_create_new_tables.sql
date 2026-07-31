CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_status_report_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_status_report_data;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_date_time_information_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_date_time_information_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_instrument_description_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_instrument_description_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_lane_configuration_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_lane_configuration_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_speed_summary_23_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_speed_summary_23_data;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_summary_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_summary_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_vehicle_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_vehicle_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_summary_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_summary_data;

CREATE TABLE lakehouse.consolidated.stage_manual_csv_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_csv_data;

CREATE TABLE lakehouse.consolidated.stage_manual_csv_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_csv_header;

CREATE TABLE lakehouse.consolidated.stage_manual_csv_ksh_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_csv_ksh_data;

CREATE TABLE lakehouse.consolidated.stage_manual_csv_nusz_veda_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_csv_nusz_veda_data;

CREATE TABLE lakehouse.consolidated.stage_manual_md_data_file_hashes_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_md_data_file_hashes;

CREATE TABLE lakehouse.consolidated.stage_manual_mnm_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_mnm_header;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_data_description_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_data_description_header;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_date_time_information_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_date_time_information_header;

CREATE TABLE lakehouse.consolidated.stage_manual_csv_qltc_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_csv_qltc_data;

CREATE TABLE lakehouse.consolidated.stage_manual_mnm_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_mnm_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_instrument_description_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_instrument_description_header;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_lane_definition_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_lane_definition_header;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_sensor_description_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_sensor_description_header;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_speed_summary_20_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_speed_summary_20_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_lane_configuration_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_lane_configuration_header;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_site_survey_identification_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_site_survey_identification_header;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_status_report_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_status_report_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_summary_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_summary_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_summary_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_summary_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_speed_summary_20_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_speed_summary_20_data;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_start_of_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_start_of_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_status_report_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_status_report_data;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_summary_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_summary_data;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_summary_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_summary_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_vehicle_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_vehicle_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_speed_summary_23_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_speed_summary_23_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_start_of_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_start_of_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_csv_nusz_veda_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_csv_nusz_veda_data;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_speed_summary_23_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_speed_summary_23_data;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_vehicle_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_vehicle_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_csv_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_csv_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_csv_qltc_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_csv_qltc_data;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_lane_definition_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_lane_definition_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_mass_and_axle_spacing_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_mass_and_axle_spacing_data;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_sensor_description_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_sensor_description_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_site_survey_identification_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_site_survey_identification_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_start_of_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_start_of_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_status_report_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_status_report_data;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_summary_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_summary_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_vehicle_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_vehicle_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_vehicle_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_vehicle_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_csv_qltc_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_csv_qltc_data;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_data_description_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_data_description_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_date_time_information_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_date_time_information_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_lane_definition_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_lane_definition_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_data_description_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_data_description_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_site_survey_identification_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_site_survey_identification_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_instrument_description_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_instrument_description_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_sensor_description_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_sensor_description_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_data_description_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_data_description_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_speed_summary_20_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_speed_summary_20_data;

CREATE TABLE lakehouse.consolidated.stage_nrt_md_data_file_hashes_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_md_data_file_hashes;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_lane_configuration_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_lane_configuration_header;

CREATE TABLE lakehouse.consolidated.stage_nrt_xtx_mass_and_axle_spacing_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_nrt_xtx_mass_and_axle_spacing_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_mnm_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_mnm_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_mnm_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_mnm_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_date_time_information_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_date_time_information_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_csv_ksh_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_csv_ksh_data;

CREATE TABLE lakehouse.consolidated.type_error_nrt_xtx_vehicle_header_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_xtx_vehicle_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_csv_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_csv_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_csv_nusz_veda_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_csv_nusz_veda_data;

CREATE TABLE lakehouse.consolidated.stage_xtx_individual_near_real_time_traffic_measurement_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_xtx_individual_near_real_time_traffic_measurement_data;

CREATE TABLE lakehouse.consolidated.stage_manual_xtx_mass_and_axle_spacing_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_manual_xtx_mass_and_axle_spacing_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_instrument_description_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_instrument_description_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_lane_configuration_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_lane_configuration_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_lane_definition_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_lane_definition_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_sensor_description_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_sensor_description_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_site_survey_identification_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_site_survey_identification_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_speed_summary_20_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_speed_summary_20_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_speed_summary_23_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_speed_summary_23_data;

CREATE TABLE lakehouse.consolidated.stage_xtx_aggregated_near_real_time_traffic_measurement_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_xtx_aggregated_near_real_time_traffic_measurement_data;

CREATE TABLE lakehouse.consolidated.error_summary_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.error_summary;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_mass_and_axle_spacing_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_mass_and_axle_spacing_data;

CREATE TABLE lakehouse.consolidated.stage_qltc_near_real_time_traffic_measurement_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_qltc_near_real_time_traffic_measurement_data;

CREATE TABLE lakehouse.consolidated.stage_veda_near_real_time_traffic_measurement_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.stage_veda_near_real_time_traffic_measurement_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_start_of_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_start_of_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_summary_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_summary_header;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_vehicle_data_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_vehicle_data;

CREATE TABLE lakehouse.consolidated.type_error_manual_xtx_vehicle_header_new
WITH (
    partitioning =  ARRAY['year(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_manual_xtx_vehicle_header;

CREATE TABLE lakehouse.consolidated.type_error_nrt_csv_nusz_veda_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_csv_nusz_veda_data;

CREATE TABLE lakehouse.consolidated.type_error_nrt_csv_qltc_data_new
WITH (
    partitioning =  ARRAY['day(md_process_date)'],
    sorted_by =  ARRAY['md_load_id ASC NULLS FIRST']
)
AS
SELECT * FROM lakehouse.consolidated.type_error_nrt_csv_qltc_data;

