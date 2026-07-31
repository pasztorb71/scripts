--CANTAS_DEV, CANTAS_TEST, CANTAS_TRAIN környezeteken QA_WRITE user létrehozása

--- core
-- postgres
CREATE USER qa_write WITH PASSWORD 'f7U+)s2rwUX_';
GRANT analytic_full TO qa_write;
GRANT customer_full TO qa_write;
GRANT genos_full TO qa_write;
GRANT privateuser_full TO qa_write;
GRANT template_full TO qa_write;
GRANT ticket_full TO qa_write;
GRANT vehicle_full TO qa_write;

--- notification
-- postgres
CREATE USER qa_write WITH PASSWORD 'f7U+)s2rwUX_';
GRANT notification_dispatcher_full TO qa_write;
GRANT notification_email_full TO qa_write;
GRANT notification_wa_full TO qa_write;
GRANT notification_wa_full TO qa_write;
GRANT sms_full TO qa_write;

--- enforcement
-- postgres
CREATE USER qa_write WITH PASSWORD 'f7U+)s2rwUX_';
GRANT detection_full TO qa_write;
GRANT detection_alert_full TO qa_write;
GRANT detection_image_full TO qa_write;
GRANT detection_observation_full TO qa_write;
GRANT detection_transit_identifier_full TO qa_write;
GRANT detection_transition_full TO qa_write;
GRANT eligibility_full TO qa_write;
GRANT exemption_full TO qa_write;
GRANT onsite_alert_full TO qa_write;
GRANT onsite_alert_subscribe_full TO qa_write;
GRANT onsite_inspection_full TO qa_write;
GRANT sanctioning_presumption_full TO qa_write;
GRANT sanctioning_sanction_full TO qa_write;
GRANT visual_check_full TO qa_write;

--- eobu
-- postgres
CREATE USER qa_write WITH PASSWORD 'f7U+)s2rwUX_';
GRANT tariff_full TO qa_write;
GRANT trip_full TO qa_write;

--- obu
-- postgres
CREATE USER qa_write WITH PASSWORD 'f7U+)s2rwUX_';
GRANT obuprovider_full TO qa_write;

--- payment
-- postgres
CREATE USER qa_write WITH PASSWORD 'f7U+)s2rwUX_';
GRANT account_info_full TO qa_write;
GRANT invoice_full TO qa_write;
GRANT psp_proxy_full TO qa_write;
GRANT payment_transaction_full TO qa_write;

--- settlement
-- postgres
CREATE USER qa_write WITH PASSWORD 'f7U+)s2rwUX_';
GRANT psp_clearing_full TO qa_write;
GRANT tro_clearing_full TO qa_write;
