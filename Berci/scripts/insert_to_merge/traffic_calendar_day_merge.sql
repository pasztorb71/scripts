MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D1', '2025-11-07 09:51:46.330619'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W1', '2026M1', '5', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D2', '2025-11-07 09:51:46.330746'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W1', '2026M1', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D3', '2025-11-07 09:51:46.330763'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W1', '2026M1', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D4', '2025-11-07 09:51:46.330771'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W1', '2026M1', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D7', '2025-11-07 09:51:46.330795'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W2', '2026M1', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D8', '2025-11-07 09:51:46.330858'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W2', '2026M1', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D9', '2025-11-07 09:51:46.330886'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W2', '2026M1', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D10', '2025-11-07 09:51:46.330898'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W2', '2026M1', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D11', '2025-11-07 09:51:46.330905'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W2', '2026M1', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D12', '2025-11-07 09:51:46.330912'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W3', '2026M1', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D13', '2025-11-07 09:51:46.330919'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W3', '2026M1', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D14', '2025-11-07 09:51:46.330926'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W3', '2026M1', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D15', '2025-11-07 09:51:46.330937'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W3', '2026M1', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D16', '2025-11-07 09:51:46.330953'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W3', '2026M1', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D17', '2025-11-07 09:51:46.330968'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W3', '2026M1', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D18', '2025-11-07 09:51:46.330978'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W3', '2026M1', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D19', '2025-11-07 09:51:46.330988'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W4', '2026M1', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D20', '2025-11-07 09:51:46.330999'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W4', '2026M1', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D21', '2025-11-07 09:51:46.331011'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W4', '2026M1', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D22', '2025-11-07 09:51:46.331019'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W4', '2026M1', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D23', '2025-11-07 09:51:46.331026'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W4', '2026M1', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D24', '2025-11-07 09:51:46.331039'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W4', '2026M1', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D25', '2025-11-07 09:51:46.331058'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W4', '2026M1', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D6', '2025-11-07 09:51:46.330788'::timestamp, '*system*', '2026-01-15 20:30:49.256'::timestamp, 'akp-test', 2, 6, '2026W2', '2026M1', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D5', '2025-11-07 09:51:46.330778'::timestamp, '*system*', '2026-01-27 13:01:44.848'::timestamp, 'akp-test', 2, 5, '2026W2', '2026M1', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D26', '2025-11-07 09:51:46.331069'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W5', '2026M1', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D27', '2025-11-07 09:51:46.331079'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W5', '2026M1', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D28', '2025-11-07 09:51:46.331089'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W5', '2026M1', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D29', '2025-11-07 09:51:46.331099'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W5', '2026M1', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D30', '2025-11-07 09:51:46.331109'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W5', '2026M1', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D31', '2025-11-07 09:51:46.33112'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026W5', '2026M1', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D32', '2025-11-07 09:51:46.331133'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W5', '2026M2', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D34', '2025-11-07 09:51:46.331162'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W6', '2026M2', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D35', '2025-11-07 09:51:46.331173'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W6', '2026M2', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D36', '2025-11-07 09:51:46.331183'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W6', '2026M2', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D37', '2025-11-07 09:51:46.331193'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W6', '2026M2', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D38', '2025-11-07 09:51:46.331203'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W6', '2026M2', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D39', '2025-11-07 09:51:46.331215'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W6', '2026M2', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D40', '2025-11-07 09:51:46.331227'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W7', '2026M2', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D41', '2025-11-07 09:51:46.331268'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W7', '2026M2', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D42', '2025-11-07 09:51:46.33128'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W7', '2026M2', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D43', '2025-11-07 09:51:46.33129'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W7', '2026M2', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D44', '2025-11-07 09:51:46.3313'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W7', '2026M2', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D45', '2025-11-07 09:51:46.331313'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W7', '2026M2', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D46', '2025-11-07 09:51:46.331324'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W7', '2026M2', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D47', '2025-11-07 09:51:46.331338'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W8', '2026M2', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D48', '2025-11-07 09:51:46.331356'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W8', '2026M2', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D49', '2025-11-07 09:51:46.331367'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W8', '2026M2', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D50', '2025-11-07 09:51:46.331378'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W8', '2026M2', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D51', '2025-11-07 09:51:46.331389'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W8', '2026M2', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D52', '2025-11-07 09:51:46.331399'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W8', '2026M2', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D53', '2025-11-07 09:51:46.331409'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W8', '2026M2', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D54', '2025-11-07 09:51:46.331433'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W9', '2026M2', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D55', '2025-11-07 09:51:46.331453'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W9', '2026M2', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D56', '2025-11-07 09:51:46.331463'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W9', '2026M2', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D57', '2025-11-07 09:51:46.331474'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W9', '2026M2', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D58', '2025-11-07 09:51:46.331484'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W9', '2026M2', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D59', '2025-11-07 09:51:46.331499'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W9', '2026M2', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D60', '2025-11-07 09:51:46.33151'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W9', '2026M3', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D61', '2025-11-07 09:51:46.331527'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W10', '2026M3', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D62', '2025-11-07 09:51:46.331542'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W10', '2026M3', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D63', '2025-11-07 09:51:46.331558'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W10', '2026M3', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D64', '2025-11-07 09:51:46.331572'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W10', '2026M3', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D65', '2025-11-07 09:51:46.331582'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W10', '2026M3', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D66', '2025-11-07 09:51:46.331592'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W10', '2026M3', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D67', '2025-11-07 09:51:46.331602'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W10', '2026M3', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D68', '2025-11-07 09:51:46.331613'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W11', '2026M3', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D69', '2025-11-07 09:51:46.331627'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W11', '2026M3', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D70', '2025-11-07 09:51:46.331638'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W11', '2026M3', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D71', '2025-11-07 09:51:46.331649'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W11', '2026M3', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D72', '2025-11-07 09:51:46.331667'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W11', '2026M3', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D73', '2025-11-07 09:51:46.331679'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W11', '2026M3', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D74', '2025-11-07 09:51:46.331689'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W11', '2026M3', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D75', '2025-11-07 09:51:46.331701'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W12', '2026M3', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D76', '2025-11-07 09:51:46.331711'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W12', '2026M3', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D77', '2025-11-07 09:51:46.331721'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W12', '2026M3', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D78', '2025-11-07 09:51:46.331732'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W12', '2026M3', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D79', '2025-11-07 09:51:46.331746'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W12', '2026M3', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D80', '2025-11-07 09:51:46.331764'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W12', '2026M3', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D81', '2025-11-07 09:51:46.331777'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W12', '2026M3', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D82', '2025-11-07 09:51:46.331788'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W13', '2026M3', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D83', '2025-11-07 09:51:46.331798'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W13', '2026M3', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D84', '2025-11-07 09:51:46.331808'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W13', '2026M3', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D85', '2025-11-07 09:51:46.331845'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W13', '2026M3', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D86', '2025-11-07 09:51:46.331865'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W13', '2026M3', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D87', '2025-11-07 09:51:46.331877'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W13', '2026M3', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D88', '2025-11-07 09:51:46.331887'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W13', '2026M3', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D89', '2025-11-07 09:51:46.331897'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W14', '2026M3', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D90', '2025-11-07 09:51:46.331907'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026W14', '2026M3', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D91', '2025-11-07 09:51:46.331916'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W14', '2026M4', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D92', '2025-11-07 09:51:46.331931'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W14', '2026M4', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D93', '2025-11-07 09:51:46.331945'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W14', '2026M4', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D94', '2025-11-07 09:51:46.331959'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W14', '2026M4', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D95', '2025-11-07 09:51:46.331974'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W14', '2026M4', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D96', '2025-11-07 09:51:46.331989'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W15', '2026M4', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D97', '2025-11-07 09:51:46.332'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W15', '2026M4', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D98', '2025-11-07 09:51:46.332011'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W15', '2026M4', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D99', '2025-11-07 09:51:46.332023'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W15', '2026M4', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D100', '2025-11-07 09:51:46.33204'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W15', '2026M4', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D101', '2025-11-07 09:51:46.633547'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W15', '2026M4', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D102', '2025-11-07 09:51:46.633673'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W15', '2026M4', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D103', '2025-11-07 09:51:46.633685'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W16', '2026M4', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D104', '2025-11-07 09:51:46.633693'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W16', '2026M4', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D105', '2025-11-07 09:51:46.633701'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W16', '2026M4', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D106', '2025-11-07 09:51:46.633707'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W16', '2026M4', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D107', '2025-11-07 09:51:46.633714'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W16', '2026M4', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D108', '2025-11-07 09:51:46.633721'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W16', '2026M4', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D109', '2025-11-07 09:51:46.633728'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W16', '2026M4', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D110', '2025-11-07 09:51:46.633734'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W17', '2026M4', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D111', '2025-11-07 09:51:46.633741'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W17', '2026M4', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D112', '2025-11-07 09:51:46.633747'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W17', '2026M4', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D113', '2025-11-07 09:51:46.633754'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W17', '2026M4', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D114', '2025-11-07 09:51:46.63378'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W17', '2026M4', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D115', '2025-11-07 09:51:46.633795'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W17', '2026M4', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D116', '2025-11-07 09:51:46.633811'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W17', '2026M4', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D117', '2025-11-07 09:51:46.633847'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W18', '2026M4', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D118', '2025-11-07 09:51:46.63386'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W18', '2026M4', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D119', '2025-11-07 09:51:46.633867'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W18', '2026M4', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D120', '2025-11-07 09:51:46.633874'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W18', '2026M4', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D121', '2025-11-07 09:51:46.63388'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W18', '2026M5', '5', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D122', '2025-11-07 09:51:46.633887'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W18', '2026M5', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D123', '2025-11-07 09:51:46.633894'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W18', '2026M5', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D124', '2025-11-07 09:51:46.6339'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W19', '2026M5', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D125', '2025-11-07 09:51:46.633907'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W19', '2026M5', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D126', '2025-11-07 09:51:46.633913'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W19', '2026M5', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D127', '2025-11-07 09:51:46.63392'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W19', '2026M5', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D128', '2025-11-07 09:51:46.633927'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W19', '2026M5', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D129', '2025-11-07 09:51:46.633933'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W19', '2026M5', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D130', '2025-11-07 09:51:46.63394'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W19', '2026M5', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D131', '2025-11-07 09:51:46.633946'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W20', '2026M5', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D132', '2025-11-07 09:51:46.633953'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W20', '2026M5', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D133', '2025-11-07 09:51:46.633959'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W20', '2026M5', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D134', '2025-11-07 09:51:46.633965'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W20', '2026M5', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D135', '2025-11-07 09:51:46.633972'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W20', '2026M5', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D136', '2025-11-07 09:51:46.633978'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W20', '2026M5', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D137', '2025-11-07 09:51:46.633984'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W20', '2026M5', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D138', '2025-11-07 09:51:46.633991'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W21', '2026M5', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D139', '2025-11-07 09:51:46.633997'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W21', '2026M5', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D140', '2025-11-07 09:51:46.634004'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W21', '2026M5', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D141', '2025-11-07 09:51:46.634011'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W21', '2026M5', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D142', '2025-11-07 09:51:46.634017'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W21', '2026M5', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D143', '2025-11-07 09:51:46.634024'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W21', '2026M5', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D144', '2025-11-07 09:51:46.63403'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W21', '2026M5', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D145', '2025-11-07 09:51:46.634037'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W22', '2026M5', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D146', '2025-11-07 09:51:46.634043'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W22', '2026M5', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D147', '2025-11-07 09:51:46.63405'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W22', '2026M5', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D148', '2025-11-07 09:51:46.634056'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W22', '2026M5', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D149', '2025-11-07 09:51:46.634062'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W22', '2026M5', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D150', '2025-11-07 09:51:46.634069'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W22', '2026M5', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D151', '2025-11-07 09:51:46.634075'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026W22', '2026M5', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D152', '2025-11-07 09:51:46.634081'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W23', '2026M6', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D153', '2025-11-07 09:51:46.634088'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W23', '2026M6', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D154', '2025-11-07 09:51:46.634095'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W23', '2026M6', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D155', '2025-11-07 09:51:46.634101'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W23', '2026M6', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D156', '2025-11-07 09:51:46.634108'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W23', '2026M6', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D157', '2025-11-07 09:51:46.634114'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W23', '2026M6', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D158', '2025-11-07 09:51:46.63412'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W23', '2026M6', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D159', '2025-11-07 09:51:46.634127'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W24', '2026M6', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D160', '2025-11-07 09:51:46.634133'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W24', '2026M6', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D161', '2025-11-07 09:51:46.63414'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W24', '2026M6', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D162', '2025-11-07 09:51:46.634146'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W24', '2026M6', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D163', '2025-11-07 09:51:46.634153'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W24', '2026M6', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D164', '2025-11-07 09:51:46.634159'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W24', '2026M6', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D165', '2025-11-07 09:51:46.634166'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W24', '2026M6', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D166', '2025-11-07 09:51:46.634172'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W25', '2026M6', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D167', '2025-11-07 09:51:46.634178'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W25', '2026M6', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D168', '2025-11-07 09:51:46.634185'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W25', '2026M6', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D169', '2025-11-07 09:51:46.634191'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W25', '2026M6', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D170', '2025-11-07 09:51:46.634198'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W25', '2026M6', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D171', '2025-11-07 09:51:46.634204'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W25', '2026M6', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D172', '2025-11-07 09:51:46.634211'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W25', '2026M6', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D173', '2025-11-07 09:51:46.634217'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W26', '2026M6', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D174', '2025-11-07 09:51:46.634224'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W26', '2026M6', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D175', '2025-11-07 09:51:46.63423'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W26', '2026M6', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D176', '2025-11-07 09:51:46.634237'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W26', '2026M6', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D177', '2025-11-07 09:51:46.634243'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W26', '2026M6', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D178', '2025-11-07 09:51:46.634249'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W26', '2026M6', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D179', '2025-11-07 09:51:46.634256'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W26', '2026M6', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D180', '2025-11-07 09:51:46.634262'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W27', '2026M6', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D181', '2025-11-07 09:51:46.634268'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W27', '2026M6', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D182', '2025-11-07 09:51:46.634275'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W27', '2026M7', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D183', '2025-11-07 09:51:46.634282'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W27', '2026M7', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D184', '2025-11-07 09:51:46.634288'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W27', '2026M7', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D185', '2025-11-07 09:51:46.634295'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W27', '2026M7', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D186', '2025-11-07 09:51:46.634301'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W27', '2026M7', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D187', '2025-11-07 09:51:46.634308'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W28', '2026M7', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D188', '2025-11-07 09:51:46.634314'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W28', '2026M7', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D189', '2025-11-07 09:51:46.634321'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W28', '2026M7', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D190', '2025-11-07 09:51:46.634327'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W28', '2026M7', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D191', '2025-11-07 09:51:46.634334'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W28', '2026M7', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D192', '2025-11-07 09:51:46.63434'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W28', '2026M7', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D193', '2025-11-07 09:51:46.634347'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W28', '2026M7', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D194', '2025-11-07 09:51:46.634353'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W29', '2026M7', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D195', '2025-11-07 09:51:46.63436'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W29', '2026M7', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D196', '2025-11-07 09:51:46.634367'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W29', '2026M7', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D197', '2025-11-07 09:51:46.634373'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W29', '2026M7', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D198', '2025-11-07 09:51:46.634379'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W29', '2026M7', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D199', '2025-11-07 09:51:46.634386'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W29', '2026M7', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D200', '2025-11-07 09:51:46.634392'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W29', '2026M7', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D201', '2025-11-07 09:51:46.935721'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W30', '2026M7', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D202', '2025-11-07 09:51:46.935967'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W30', '2026M7', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D203', '2025-11-07 09:51:46.935992'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W30', '2026M7', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D204', '2025-11-07 09:51:46.936008'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W30', '2026M7', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D205', '2025-11-07 09:51:46.936048'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W30', '2026M7', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D206', '2025-11-07 09:51:46.936064'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W30', '2026M7', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D207', '2025-11-07 09:51:46.93608'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W30', '2026M7', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D208', '2025-11-07 09:51:46.936096'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W31', '2026M7', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D209', '2025-11-07 09:51:46.936109'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W31', '2026M7', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D210', '2025-11-07 09:51:46.93612'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W31', '2026M7', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D211', '2025-11-07 09:51:46.93613'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W31', '2026M7', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D212', '2025-11-07 09:51:46.93614'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026W31', '2026M7', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D213', '2025-11-07 09:51:46.936169'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W31', '2026M8', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D214', '2025-11-07 09:51:46.93618'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W31', '2026M8', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D215', '2025-11-07 09:51:46.936191'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W32', '2026M8', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D216', '2025-11-07 09:51:46.936201'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W32', '2026M8', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D217', '2025-11-07 09:51:46.936212'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W32', '2026M8', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D218', '2025-11-07 09:51:46.936223'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W32', '2026M8', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D219', '2025-11-07 09:51:46.936234'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W32', '2026M8', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D220', '2025-11-07 09:51:46.936246'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W32', '2026M8', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D221', '2025-11-07 09:51:46.936275'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W32', '2026M8', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D222', '2025-11-07 09:51:46.936286'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W33', '2026M8', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D223', '2025-11-07 09:51:46.936295'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W33', '2026M8', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D224', '2025-11-07 09:51:46.936304'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W33', '2026M8', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D225', '2025-11-07 09:51:46.936313'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W33', '2026M8', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D226', '2025-11-07 09:51:46.936321'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W33', '2026M8', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D227', '2025-11-07 09:51:46.936331'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W33', '2026M8', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D228', '2025-11-07 09:51:46.936344'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W33', '2026M8', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D229', '2025-11-07 09:51:46.93636'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W34', '2026M8', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D230', '2025-11-07 09:51:46.936378'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W34', '2026M8', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D231', '2025-11-07 09:51:46.936392'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W34', '2026M8', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D232', '2025-11-07 09:51:46.936408'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W34', '2026M8', '5', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D233', '2025-11-07 09:51:46.936423'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W34', '2026M8', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D234', '2025-11-07 09:51:46.936442'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W34', '2026M8', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D235', '2025-11-07 09:51:46.93647'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W34', '2026M8', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D236', '2025-11-07 09:51:46.936481'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W35', '2026M8', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D237', '2025-11-07 09:51:46.936491'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W35', '2026M8', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D238', '2025-11-07 09:51:46.936502'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W35', '2026M8', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D239', '2025-11-07 09:51:46.936517'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W35', '2026M8', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D240', '2025-11-07 09:51:46.936528'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W35', '2026M8', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D241', '2025-11-07 09:51:46.936542'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W35', '2026M8', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D242', '2025-11-07 09:51:46.936718'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W35', '2026M8', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D243', '2025-11-07 09:51:46.936777'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026W36', '2026M8', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D244', '2025-11-07 09:51:46.936786'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W36', '2026M9', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D245', '2025-11-07 09:51:46.936796'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W36', '2026M9', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D246', '2025-11-07 09:51:46.936806'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W36', '2026M9', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D247', '2025-11-07 09:51:46.936816'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W36', '2026M9', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D248', '2025-11-07 09:51:46.936847'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W36', '2026M9', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D249', '2025-11-07 09:51:46.936859'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W36', '2026M9', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D250', '2025-11-07 09:51:46.936869'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W37', '2026M9', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D251', '2025-11-07 09:51:46.93688'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W37', '2026M9', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D252', '2025-11-07 09:51:46.936891'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W37', '2026M9', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D253', '2025-11-07 09:51:46.936902'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W37', '2026M9', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D254', '2025-11-07 09:51:46.936913'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W37', '2026M9', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D255', '2025-11-07 09:51:46.936923'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W37', '2026M9', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D256', '2025-11-07 09:51:46.936934'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W37', '2026M9', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D257', '2025-11-07 09:51:46.936944'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W38', '2026M9', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D258', '2025-11-07 09:51:46.936955'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W38', '2026M9', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D259', '2025-11-07 09:51:46.936965'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W38', '2026M9', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D260', '2025-11-07 09:51:46.936976'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W38', '2026M9', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D261', '2025-11-07 09:51:46.936986'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W38', '2026M9', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D262', '2025-11-07 09:51:46.936996'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W38', '2026M9', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D263', '2025-11-07 09:51:46.937007'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W38', '2026M9', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D264', '2025-11-07 09:51:46.937018'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W39', '2026M9', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D265', '2025-11-07 09:51:46.937028'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W39', '2026M9', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D266', '2025-11-07 09:51:46.937037'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W39', '2026M9', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D267', '2025-11-07 09:51:46.937048'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W39', '2026M9', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D268', '2025-11-07 09:51:46.937058'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W39', '2026M9', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D269', '2025-11-07 09:51:46.937068'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W39', '2026M9', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D270', '2025-11-07 09:51:46.937078'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W39', '2026M9', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D271', '2025-11-07 09:51:46.937089'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W40', '2026M9', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D272', '2025-11-07 09:51:46.937099'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W40', '2026M9', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D273', '2025-11-07 09:51:46.937109'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W40', '2026M9', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D274', '2025-11-07 09:51:46.937118'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W40', '2026M10', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D275', '2025-11-07 09:51:46.937127'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W40', '2026M10', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D276', '2025-11-07 09:51:46.937136'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W40', '2026M10', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D277', '2025-11-07 09:51:46.937145'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W40', '2026M10', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D278', '2025-11-07 09:51:46.937156'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W41', '2026M10', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D279', '2025-11-07 09:51:46.937167'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W41', '2026M10', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D280', '2025-11-07 09:51:46.937177'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W41', '2026M10', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D281', '2025-11-07 09:51:46.937188'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W41', '2026M10', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D282', '2025-11-07 09:51:46.937199'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W41', '2026M10', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D283', '2025-11-07 09:51:46.93721'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W41', '2026M10', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D284', '2025-11-07 09:51:46.93722'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W41', '2026M10', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D285', '2025-11-07 09:51:46.937229'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W42', '2026M10', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D286', '2025-11-07 09:51:46.937238'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W42', '2026M10', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D287', '2025-11-07 09:51:46.937247'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W42', '2026M10', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D288', '2025-11-07 09:51:46.937258'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W42', '2026M10', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D289', '2025-11-07 09:51:46.937267'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W42', '2026M10', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D290', '2025-11-07 09:51:46.937277'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W42', '2026M10', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D291', '2025-11-07 09:51:46.937287'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W42', '2026M10', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D292', '2025-11-07 09:51:46.937297'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W43', '2026M10', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D293', '2025-11-07 09:51:46.937307'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W43', '2026M10', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D294', '2025-11-07 09:51:46.937317'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W43', '2026M10', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D295', '2025-11-07 09:51:46.937328'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W43', '2026M10', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D296', '2025-11-07 09:51:46.937338'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W43', '2026M10', '5', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D297', '2025-11-07 09:51:46.937348'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W43', '2026M10', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D298', '2025-11-07 09:51:46.937359'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W43', '2026M10', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D299', '2025-11-07 09:51:46.93737'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W44', '2026M10', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D300', '2025-11-07 09:51:46.93738'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W44', '2026M10', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D301', '2025-11-07 09:51:47.327086'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W44', '2026M10', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D302', '2025-11-07 09:51:47.327217'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W44', '2026M10', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D303', '2025-11-07 09:51:47.327227'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W44', '2026M10', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D304', '2025-11-07 09:51:47.327234'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026W44', '2026M10', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D305', '2025-11-07 09:51:47.327241'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W44', '2026M11', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D306', '2025-11-07 09:51:47.327248'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W45', '2026M11', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D307', '2025-11-07 09:51:47.327255'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W45', '2026M11', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D308', '2025-11-07 09:51:47.327262'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W45', '2026M11', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D309', '2025-11-07 09:51:47.327268'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W45', '2026M11', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D310', '2025-11-07 09:51:47.327275'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W45', '2026M11', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D311', '2025-11-07 09:51:47.327281'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W45', '2026M11', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D312', '2025-11-07 09:51:47.327287'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W45', '2026M11', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D313', '2025-11-07 09:51:47.327295'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W46', '2026M11', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D314', '2025-11-07 09:51:47.327303'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W46', '2026M11', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D315', '2025-11-07 09:51:47.327309'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W46', '2026M11', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D316', '2025-11-07 09:51:47.327316'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W46', '2026M11', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D317', '2025-11-07 09:51:47.327322'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W46', '2026M11', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D318', '2025-11-07 09:51:47.327328'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W46', '2026M11', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D319', '2025-11-07 09:51:47.327335'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W46', '2026M11', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D320', '2025-11-07 09:51:47.327341'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W47', '2026M11', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D321', '2025-11-07 09:51:47.327348'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W47', '2026M11', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D322', '2025-11-07 09:51:47.327354'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W47', '2026M11', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D323', '2025-11-07 09:51:47.32736'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W47', '2026M11', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D324', '2025-11-07 09:51:47.327367'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W47', '2026M11', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D325', '2025-11-07 09:51:47.327373'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W47', '2026M11', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D326', '2025-11-07 09:51:47.327379'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W47', '2026M11', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D327', '2025-11-07 09:51:47.327386'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W48', '2026M11', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D328', '2025-11-07 09:51:47.327392'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W48', '2026M11', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D329', '2025-11-07 09:51:47.327399'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W48', '2026M11', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D330', '2025-11-07 09:51:47.327405'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W48', '2026M11', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D331', '2025-11-07 09:51:47.327411'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W48', '2026M11', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D332', '2025-11-07 09:51:47.327418'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W48', '2026M11', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D333', '2025-11-07 09:51:47.327424'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W48', '2026M11', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D334', '2025-11-07 09:51:47.32743'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W49', '2026M11', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D335', '2025-11-07 09:51:47.327437'::timestamp, '*system*', NULL::timestamp, NULL, 0, 1, '2026W49', '2026M12', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D336', '2025-11-07 09:51:47.327443'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026W49', '2026M12', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D337', '2025-11-07 09:51:47.32745'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026W49', '2026M12', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D338', '2025-11-07 09:51:47.327457'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026W49', '2026M12', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D339', '2025-11-07 09:51:47.327463'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026W49', '2026M12', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D340', '2025-11-07 09:51:47.327469'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026W49', '2026M12', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D341', '2025-11-07 09:51:47.327475'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026W50', '2026M12', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D342', '2025-11-07 09:51:47.327482'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026W50', '2026M12', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D343', '2025-11-07 09:51:47.327489'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026W50', '2026M12', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D344', '2025-11-07 09:51:47.327495'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026W50', '2026M12', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D345', '2025-11-07 09:51:47.327501'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026W50', '2026M12', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D346', '2025-11-07 09:51:47.327508'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026W50', '2026M12', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D347', '2025-11-07 09:51:47.327514'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026W50', '2026M12', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D348', '2025-11-07 09:51:47.327522'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026W51', '2026M12', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D349', '2025-11-07 09:51:47.327532'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026W51', '2026M12', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D350', '2025-11-07 09:51:47.327542'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026W51', '2026M12', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D351', '2025-11-07 09:51:47.327551'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026W51', '2026M12', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D352', '2025-11-07 09:51:47.32756'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026W51', '2026M12', '3', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D353', '2025-11-07 09:51:47.327569'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026W51', '2026M12', '4', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D354', '2025-11-07 09:51:47.327576'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026W51', '2026M12', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D355', '2025-11-07 09:51:47.327582'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026W52', '2026M12', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D356', '2025-11-07 09:51:47.327589'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026W52', '2026M12', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D357', '2025-11-07 09:51:47.327595'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026W52', '2026M12', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D358', '2025-11-07 09:51:47.327602'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026W52', '2026M12', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D359', '2025-11-07 09:51:47.327608'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026W52', '2026M12', '5', NULL, NULL, '5') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D360', '2025-11-07 09:51:47.327614'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026W52', '2026M12', '5', NULL, NULL, '6') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D361', '2025-11-07 09:51:47.327621'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026W52', '2026M12', '5', NULL, NULL, '7') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D362', '2025-11-07 09:51:47.327628'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026W53', '2026M12', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D363', '2025-11-07 09:51:47.327634'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026W53', '2026M12', '2', NULL, NULL, '2') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D364', '2025-11-07 09:51:47.327641'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026W53', '2026M12', '2', NULL, NULL, '3') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D365', '2025-11-07 09:51:47.327647'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026W53', '2026M12', '2', NULL, NULL, '4') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
MERGE INTO traffic_calendar_day 
USING ( 
    SELECT '2026D33', '2025-11-07 09:51:46.331151'::timestamp, '*system*', '2026-02-02 14:32:21.079'::timestamp, 'akp-test', 4, 2, '2026W6', '2026M2', '1', NULL, NULL, '1') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
ON (tmp.x__id = traffic_calendar_day.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "date", traffic_calendar_week_id, traffic_calendar_month_id, day_type_id, moveable_feast_type_id, daylight_saving_time_type_id, day_of_week_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."date", tmp.traffic_calendar_week_id, tmp.traffic_calendar_month_id, tmp.day_type_id, tmp.moveable_feast_type_id, tmp.daylight_saving_time_type_id, tmp.day_of_week_id);
