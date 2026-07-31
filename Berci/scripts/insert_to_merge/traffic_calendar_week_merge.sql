MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W1', '2025-05-21 15:51:17.071865'::timestamp, '0', NULL::timestamp, NULL, 0, 1, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W10', '2025-11-07 09:51:46.185117'::timestamp, '*system*', NULL::timestamp, NULL, 0, 10, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W11', '2025-11-07 09:51:46.185122'::timestamp, '*system*', NULL::timestamp, NULL, 0, 11, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W12', '2025-11-07 09:51:46.185126'::timestamp, '*system*', NULL::timestamp, NULL, 0, 12, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W13', '2025-11-07 09:51:46.185131'::timestamp, '*system*', NULL::timestamp, NULL, 0, 13, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W14', '2025-11-07 09:51:46.185137'::timestamp, '*system*', NULL::timestamp, NULL, 0, 14, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W15', '2025-11-07 09:51:46.185141'::timestamp, '*system*', NULL::timestamp, NULL, 0, 15, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W16', '2025-11-07 09:51:46.185146'::timestamp, '*system*', NULL::timestamp, NULL, 0, 16, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W17', '2025-11-07 09:51:46.185151'::timestamp, '*system*', NULL::timestamp, NULL, 0, 17, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W18', '2025-11-07 09:51:46.185156'::timestamp, '*system*', NULL::timestamp, NULL, 0, 18, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W19', '2025-11-07 09:51:46.18516'::timestamp, '*system*', NULL::timestamp, NULL, 0, 19, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W2', '2025-11-07 09:51:46.184996'::timestamp, '*system*', NULL::timestamp, NULL, 0, 2, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W20', '2025-11-07 09:51:46.185166'::timestamp, '*system*', NULL::timestamp, NULL, 0, 20, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W21', '2025-11-07 09:51:46.18517'::timestamp, '*system*', NULL::timestamp, NULL, 0, 21, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W22', '2025-11-07 09:51:46.185175'::timestamp, '*system*', NULL::timestamp, NULL, 0, 22, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W23', '2025-11-07 09:51:46.18518'::timestamp, '*system*', NULL::timestamp, NULL, 0, 23, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W24', '2025-11-07 09:51:46.185184'::timestamp, '*system*', NULL::timestamp, NULL, 0, 24, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W25', '2025-11-07 09:51:46.185189'::timestamp, '*system*', NULL::timestamp, NULL, 0, 25, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W26', '2025-11-07 09:51:46.185194'::timestamp, '*system*', NULL::timestamp, NULL, 0, 26, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W27', '2025-11-07 09:51:46.185199'::timestamp, '*system*', NULL::timestamp, NULL, 0, 27, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W28', '2025-11-07 09:51:46.185203'::timestamp, '*system*', NULL::timestamp, NULL, 0, 28, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W29', '2025-11-07 09:51:46.185208'::timestamp, '*system*', NULL::timestamp, NULL, 0, 29, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W3', '2025-11-07 09:51:46.185081'::timestamp, '*system*', NULL::timestamp, NULL, 0, 3, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W30', '2025-11-07 09:51:46.185213'::timestamp, '*system*', NULL::timestamp, NULL, 0, 30, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W31', '2025-11-07 09:51:46.185218'::timestamp, '*system*', NULL::timestamp, NULL, 0, 31, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W32', '2025-11-07 09:51:46.185222'::timestamp, '*system*', NULL::timestamp, NULL, 0, 32, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W33', '2025-11-07 09:51:46.185227'::timestamp, '*system*', NULL::timestamp, NULL, 0, 33, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W34', '2025-11-07 09:51:46.185232'::timestamp, '*system*', NULL::timestamp, NULL, 0, 34, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W35', '2025-11-07 09:51:46.185236'::timestamp, '*system*', NULL::timestamp, NULL, 0, 35, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W36', '2025-11-07 09:51:46.185241'::timestamp, '*system*', NULL::timestamp, NULL, 0, 36, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W37', '2025-11-07 09:51:46.185246'::timestamp, '*system*', NULL::timestamp, NULL, 0, 37, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W38', '2025-11-07 09:51:46.18525'::timestamp, '*system*', NULL::timestamp, NULL, 0, 38, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W39', '2025-11-07 09:51:46.185255'::timestamp, '*system*', NULL::timestamp, NULL, 0, 39, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W4', '2025-11-07 09:51:46.185088'::timestamp, '*system*', NULL::timestamp, NULL, 0, 4, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W40', '2025-11-07 09:51:46.18526'::timestamp, '*system*', NULL::timestamp, NULL, 0, 40, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W41', '2025-11-07 09:51:46.185264'::timestamp, '*system*', NULL::timestamp, NULL, 0, 41, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W42', '2025-11-07 09:51:46.185269'::timestamp, '*system*', NULL::timestamp, NULL, 0, 42, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W43', '2025-11-07 09:51:46.185274'::timestamp, '*system*', NULL::timestamp, NULL, 0, 43, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W44', '2025-11-07 09:51:46.185278'::timestamp, '*system*', NULL::timestamp, NULL, 0, 44, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W45', '2025-11-07 09:51:46.185283'::timestamp, '*system*', NULL::timestamp, NULL, 0, 45, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W46', '2025-11-07 09:51:46.185288'::timestamp, '*system*', NULL::timestamp, NULL, 0, 46, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W47', '2025-11-07 09:51:46.185292'::timestamp, '*system*', NULL::timestamp, NULL, 0, 47, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W48', '2025-11-07 09:51:46.185297'::timestamp, '*system*', NULL::timestamp, NULL, 0, 48, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W49', '2025-11-07 09:51:46.185302'::timestamp, '*system*', NULL::timestamp, NULL, 0, 49, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W5', '2025-11-07 09:51:46.185093'::timestamp, '*system*', NULL::timestamp, NULL, 0, 5, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W50', '2025-11-07 09:51:46.185306'::timestamp, '*system*', NULL::timestamp, NULL, 0, 50, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W51', '2025-11-07 09:51:46.185311'::timestamp, '*system*', NULL::timestamp, NULL, 0, 51, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W52', '2025-11-07 09:51:46.185316'::timestamp, '*system*', NULL::timestamp, NULL, 0, 52, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W53', '2025-11-07 09:51:46.18532'::timestamp, '*system*', NULL::timestamp, NULL, 0, 53, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W6', '2025-11-07 09:51:46.185098'::timestamp, '*system*', NULL::timestamp, NULL, 0, 6, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W7', '2025-11-07 09:51:46.185102'::timestamp, '*system*', NULL::timestamp, NULL, 0, 7, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W8', '2025-11-07 09:51:46.185107'::timestamp, '*system*', NULL::timestamp, NULL, 0, 8, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
MERGE INTO traffic_calendar_week 
USING ( 
    SELECT '2026W9', '2025-11-07 09:51:46.185112'::timestamp, '*system*', NULL::timestamp, NULL, 0, 9, '2026') 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
ON (tmp.x__id = traffic_calendar_week.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, week, traffic_calendar_year_id) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp.week, tmp.traffic_calendar_year_id);
