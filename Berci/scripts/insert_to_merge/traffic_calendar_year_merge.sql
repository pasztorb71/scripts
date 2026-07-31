MERGE INTO traffic_calendar_year 
USING ( 
    SELECT '2026', '2025-05-21 15:51:16.8772'::timestamp, '0', '2025-11-07 09:51:46.117'::timestamp, '*system*', 23, 2026, false, false, true) 
    AS tmp (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "year", closed, approved, calendar_structure_complete) 
ON (tmp.x__id = traffic_calendar_year.x__id) 
WHEN NOT MATCHED THEN 
INSERT (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "year", closed, approved, calendar_structure_complete) 
VALUES (tmp.x__id, tmp.x__insdate, tmp.x__insuser, tmp.x__moddate, tmp.x__moduser, tmp.x__version, tmp."year", tmp.closed, tmp.approved, tmp.calendar_structure_complete);
