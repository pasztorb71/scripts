
--- core
-- core_analytic
select count(*) from analytic.plate_number_whitelist where plate_number != upper(plate_number);
-- core_ticket
select count(*) from ticket.pre_ticket where plate_number != upper(plate_number);
select count(*) from ticket.ticket where plate_number != upper(plate_number);
select count(*) from ticket.ticket_plan where plate_number != upper(plate_number);
-- core_vehicle
select count(*) from vehicle.plate_number_change where plate_number != upper(plate_number);
select count(*) from vehicle.vehicle where plate_number != upper(plate_number);

--- enforcement
-- enforcement_detection_alert
select count(*) from detection_alert.alert_check_data where plate_number != upper(plate_number);
-- enforcement_detection_observation
select count(*) from detection_observation.observation where plate_number != upper(plate_number);
-- enforcement_detection
select count(*) from detection.detection_detail where front_plate_number != upper(front_plate_number);
select count(*) from detection.detection_detail where rear_plate_number != upper(rear_plate_number);
-- enforcement_detection_transit_identifier
select count(*) from detection_transit_identifier.transit_identifier_event where plate_number != upper(plate_number);
-- enforcement_detection_transition
select count(*) from detection_transition.detection where plate_number != upper(plate_number);
select count(*) from detection_transition.lane_user where plate_number != upper(plate_number);
-- enforcement_eligibility
select count(*) from eligibility.detection_data where front_plate_number != upper(front_plate_number);
select count(*) from eligibility.detection_data where rear_plate_number != upper(rear_plate_number);
select count(*) from eligibility.detection_data where search_plate_number != upper(search_plate_number);
select count(*) from eligibility.onsite where front_plate_number != upper(front_plate_number);
select count(*) from eligibility.presumption where front_plate_number != upper(front_plate_number);
select count(*) from eligibility.presumption_in_progress where search_plate_number != upper(search_plate_number);
select count(*) from eligibility.sick_detection_data where front_plate_number != upper(front_plate_number);
select count(*) from eligibility.sick_detection_data where rear_plate_number != upper(rear_plate_number);
select count(*) from eligibility.ticket_data where plate_number != upper(plate_number);
-- enforcement_exemption
select count(*) from exemption.exemption_vehicle where plate_number != upper(plate_number);
-- enforcement_onsite_alert
select count(*) from onsite_alert.alert_data where front_plate_number != upper(front_plate_number);
-- enforcement_onsite_inspection
select count(*) from onsite_inspection.inspection_data where plate_number != upper(plate_number);
select count(*) from onsite_inspection.vhl_check where plate_number != upper(plate_number);
-- enforcement_sanctioning_presumption
select count(*) from sanctioning_presumption.presumption where plate_number != upper(plate_number);
select count(*) from sanctioning_presumption.presumption_declaration where front_plate_number != upper(front_plate_number);
select count(*) from sanctioning_presumption.presumption_detection where front_plate_number != upper(front_plate_number);
select count(*) from sanctioning_presumption.presumption_detection where rear_plate_number != upper(rear_plate_number);
-- enforcement_sanctioning_sanction
select count(*) from sanctioning_sanction.sanction where plate_number != upper(plate_number);
-- enforcement_visual_check
select count(*) from visual_check.check_package where front_plate_number != upper(front_plate_number);
select count(*) from visual_check.check_package where rear_plate_number != upper(rear_plate_number);
select count(*) from visual_check.task where front_plate_number != upper(front_plate_number);
select count(*) from visual_check.task where rear_plate_number != upper(rear_plate_number);

--- eobu
-- eobu_trip
select count(*) from trip.trip where plate_number != upper(plate_number);

--- payment
-- payment_invoice
select count(*) from invoice.invoice where front_plate_number != upper(front_plate_number);
