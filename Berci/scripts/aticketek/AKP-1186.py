def get_col_types():
    col_types = {}
    with open('#0067-station-create.sql', encoding='utf-8') as f:
        sql = f.read()
        # Find the CREATE TABLE statement
        match = re.search(r'CREATE TABLE.*?\((.*?)\);', sql, re.DOTALL | re.IGNORECASE)
        if match:
            cols = match.group(1).split(',')
            for col in cols:
                parts = col.strip().split()
                if len(parts) >= 2:
                    col_name = parts[0].strip('`"[]')
                    col_type = parts[1].upper()
                    col_types[col_name] = col_type
    return col_types


def format_value(val, col):
    col_types = get_col_types()
    if pd.isnull(val):
        return 'NULL'
    col_type = col_types.get(col, '')
    if any(t in col_type for t in ['CHAR', 'TEXT', 'DATE', 'TIME']):
        return str(val).replace(\"'\", \"''\")
    return str(val)

def teszt():
    import pandas as pd
    df = pd.read_excel(r'station.xlsx', sheet_name=0)
    # Drop columns BH to BS (inclusive)
    cols_to_drop = df.columns[df.columns.get_loc('Domborzat'):df.columns.get_loc('Megyei Jogú Város') + 1]
    df = df.drop(columns=cols_to_drop)
    table = 'akp_masterdata.station'
    with open('insert_commands.sql', 'w', encoding='utf-8') as f:
        xid = 1
        f.write('INSERT INTO station (x__id, x__insdate, station_external_id, station_external_id_2, organization_id, road_operator_external_id, engineering, sap_county, sap_engineering, road_number, road_category, international_road_sign_1, international_road_sign_2, international_road_sign_3, year_2023_2032, additional_counting_year, county_id, location_id, street, eov_x, eov_y, wgs_x, wgs_y, region, section_km, section_m, station_physical_type, validity_start_section_km, validity_start_section_m, validity_end_section_km, validity_end_section_m, validity_start_wgs_y, validity_start_wgs_x, validity_end_wgs_y, validity_end_wgs_x, validity_start_oka_id, validity_end_oka_id, validity_section_length, station_location, traffic_characteristics_1_id, traffic_characteristics_2_id, station_type, traffic_lane_count, continous_flow_lane_count, vehicle_traffic_lane_count, bicycle_lane_count, substitute_station_external_id, assigned_station_external_id, right_bicycle_path_external_id, left_bicycle_path_external_id, weight_limit, system, station_note, veda_external_id, ud_external_id, counting_cycle, related_stations_capacity_parallel, related_stations_capacity_adjacent, station_status, tourism, hpr_managed_section, bicycle_oka_id, affected_road, bicycle_station) VALUES\n')
        for _, row in df.iterrows():
            columns = ', '.join([f'"{col}"' for col in df.columns])
            #values = ', '.join([str(val) if pd.notnull(val) else 'NULL' for val in row])
            values = ', '.join([format_value(row[col], col) for col in df.columns])
            f.write(f'(CURRENT_TIMESTAMP, {values}),\n')
            xid += 1
            if xid > 10:
                break
        f.write(';\n')

def convert():
    with open('0068-station-DML.sql', 'r', encoding='utf-8') as f:
        lines = f.readlines()[0:]
    with open('insert_commands.sql', 'w', encoding='utf-8') as f:
        f.write('INSERT INTO station (x__id, station_external_id, station_external_id_2, organization_id, road_operator_external_id, engineering, sap_county, sap_engineering, road_number, road_category, international_road_sign_1, international_road_sign_2, international_road_sign_3, year_2023_2032, additional_counting_year, county_id, location_id, street, eov_x, eov_y, wgs_x, wgs_y, region, section_km, section_m, station_physical_type, validity_start_section_km, validity_start_section_m, validity_end_section_km, validity_end_section_m, validity_start_wgs_y, validity_start_wgs_x, validity_end_wgs_y, validity_end_wgs_x, validity_start_oka_id, validity_end_oka_id, validity_section_length, station_location, traffic_characteristics_1_id, traffic_characteristics_2_id, station_type, traffic_lane_count, continous_flow_lane_count, vehicle_traffic_lane_count, bicycle_lane_count, substitute_station_external_id, assigned_station_external_id, right_bicycle_path_external_id, left_bicycle_path_external_id, weight_limit, system, station_note, veda_external_id, ud_external_id, counting_cycle, related_stations_capacity_parallel, related_stations_capacity_adjacent, station_status, tourism, hpr_managed_section, bicycle_oka_id, affected_road, bicycle_station, x__insdate) VALUES\n')
        for line in [i for i in lines if i.startswith('INSERT INTO')]:
            arr = line.split(' VALUES ')[1].split(', ')
            f.write(', '.join(arr[0:64]) + '),\n')
        f.write(';\n')



if __name__ == '__main__':
    teszt()
    #convert()
