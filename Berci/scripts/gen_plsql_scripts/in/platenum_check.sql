
--- core
-- core_analytic
select count(*) from plate_number_whitelist where plate_number != upper(plate_number);
-- core_ticket
select count(*) from pre_ticket where plate_number != upper(plate_number);
select count(*) from ticket where plate_number != upper(plate_number);
select count(*) from ticket_plan where plate_number != upper(plate_number);
-- core_vehicle
select count(*) from plate_number_change where plate_number != upper(plate_number);
select count(*) from vehicle where plate_number != upper(plate_number);

--- enforcement
-- enforcement_detection_alert
select count(*) from alert_check_data where plate_number != upper(plate_number);
-- enforcement_detection_observation
select count(*) from observation where plate_number != upper(plate_number);
-- enforcement_detection
select count(*) from detection_detail where front_plate_number != upper(front_plate_number);
select count(*) from detection_detail where rear_plate_number != upper(rear_plate_number);
-- enforcement_detection_transit_identifier
select count(*) from transit_identifier_event where plate_number != upper(plate_number);
-- enforcement_detection_transition
select count(*) from detection where plate_number != upper(plate_number);
select count(*) from lane_user where plate_number != upper(plate_number);
-- enforcement_eligibility
select count(*) from detection_data where front_plate_number != upper(front_plate_number);
select count(*) from detection_data where rear_plate_number != upper(rear_plate_number);
select count(*) from detection_data where search_plate_number != upper(search_plate_number);
select count(*) from onsite where front_plate_number != upper(front_plate_number);
select count(*) from presumption where front_plate_number != upper(front_plate_number);
select count(*) from presumption_in_progress where search_plate_number != upper(search_plate_number);
select count(*) from sick_detection_data where front_plate_number != upper(front_plate_number);
select count(*) from sick_detection_data where rear_plate_number != upper(rear_plate_number);
select count(*) from ticket_data where plate_number != upper(plate_number);
-- enforcement_exemption
select count(*) from exemption_vehicle where plate_number != upper(plate_number);
-- enforcement_onsite_alert
select count(*) from alert_data where front_plate_number != upper(front_plate_number);
-- enforcement_onsite_inspection
select count(*) from inspection_data where plate_number != upper(plate_number);
select count(*) from vhl_check where plate_number != upper(plate_number);
-- enforcement_sanctioning_presumption
select count(*) from presumption where plate_number != upper(plate_number);
select count(*) from presumption_declaration where front_plate_number != upper(front_plate_number);
select count(*) from presumption_detection where front_plate_number != upper(front_plate_number);
select count(*) from presumption_detection where rear_plate_number != upper(rear_plate_number);
-- enforcement_sanctioning_sanction
select count(*) from sanction where plate_number != upper(plate_number);
-- enforcement_visual_check
select count(*) from check_package where front_plate_number != upper(front_plate_number);
select count(*) from check_package where rear_plate_number != upper(rear_plate_number);
select count(*) from task where front_plate_number != upper(front_plate_number);
select count(*) from task where rear_plate_number != upper(rear_plate_number);

--- eobu
-- eobu_trip
select count(*) from trip where plate_number != upper(plate_number);

--- payment
-- payment_invoice
select count(*) from invoice where front_plate_number != upper(front_plate_number);
