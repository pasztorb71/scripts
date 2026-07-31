MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M1', '2025-11-07 09:51:46.139398'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, 'Január', '2026', '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M10', '2025-11-07 09:51:46.139802'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, 'Október', '2026', '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M11', '2025-11-07 09:51:46.139808'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, 'November', '2026', '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M12', '2025-11-07 09:51:46.139814'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, 'December', '2026', '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M2', '2025-11-07 09:51:46.139742'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, 'Február', '2026', '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M3', '2025-11-07 09:51:46.139755'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, 'Március', '2026', '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M4', '2025-11-07 09:51:46.139761'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, 'Április', '2026', '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M5', '2025-11-07 09:51:46.139767'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, 'Május', '2026', '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M6', '2025-11-07 09:51:46.13978'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, 'Június', '2026', '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M7', '2025-11-07 09:51:46.139786'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, 'Július', '2026', '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M8', '2025-11-07 09:51:46.139791'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, 'Augusztus', '2026', '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
MERGE INTO traffic_calendar_month 
USING ( 
    SELECT '2026M9', '2025-11-07 09:51:46.139797'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, 'Szeptember', '2026', '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
ON (tmp.x__id = traffic_calendar_month.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, month_number, month_name, traffic_calendar_year_id, season_type_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.month_number, tmp.month_name, tmp.traffic_calendar_year_id, tmp.season_type_id);
