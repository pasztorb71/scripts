cmdlist = {
    'core_customer': [
        """INSERT INTO security_user
        (x__id, username, "password", active, x__insdate, x__insuser, x__moddate, x__moduser, x__version)
        VALUES('tesztid', 'test20220408153532',
        'D437BB85A2854392878C6A1686728F680AAD060073053EA8D21DFBE5F965158244D4727FCA811B7ADD99D4BA004D405958AF79151996016B8D1CC7BAE0CBEBD9', 
        true, '2022-04-08 15:35:33.481', '0', '2022-04-08 15:35:36.407', '0', 1)""",
        """INSERT INTO user_session
        (x__id, security_user_id, username, session_start, session_end, session_token, session_token_expiry, refresh_token, 
        refresh_token_expiry, device_id, device_token, device_token_expiry, x__insdate, x__insuser, x__moddate, x__moduser, 
        x__version)
        VALUES('tesztid', 'tesztid', 'Robot20220408120053', '2022-04-08 12:00:58.275', NULL, 
        'c8958589-d42a-4308-851d-56a1a08378b23QBZJIQR33OD', '2022-04-08 12:30:58.275', 
        'f6f6568a-501f-4bfd-9d9e-234a6d22dfb33QBZJIQRGDPL', '2022-04-08 21:00:58.275', '''apple''', 
        '11a8760f-1535-4470-bf85-1441ba4dfb663QBZJIQSQLJG', '2022-07-07 12:00:58.276', '2022-04-08 12:00:58.284', '0', NULL, 
        NULL, 0)""",
        "DELETE FROM user_session WHERE x__id = 'tesztid'",
        "DELETE FROM security_user WHERE x__id = 'tesztid'"
    ],
    'enforcement_visual_check':[
        """INSERT INTO check_package 
        (x__id, event_id, front_plate_number, rear_plate_number, category, front_plate_status, rear_plate_status, 
        category_status, resource_id, event_time, status, priority, origin, verified, x__insdate, x__insuser, 
        x__moddate, x__moduser, x__version, error_type) 
        VALUES('tesztid', '00e987ae-5033-4c8a-a08e-2b406c3a7a08'::uuid, 'MSS697', 'XZN475', 'GROUP_5', 'RECOGNIZED', 
        'RECOGNIZED', 'RECOGNIZED', '7510eb11-6a0e-4f0e-a471-20b3a5ef379d'::uuid, '2022-02-17 12:05:30.000', 
        'SELECTABLE', 2, 'SANCTIONING', false, '2022-05-15 12:01:04.017', 'init', '2022-05-15 12:01:04.017', 
        'init', 1, NULL)""",
        """INSERT INTO task 
        (x__id, check_package_id, user_id, front_plate_number, rear_plate_number, category, front_plate_status, 
        rear_plate_status, category_status, start_time, end_time, status, x__insdate, x__insuser, x__moddate, x__moduser, 
        x__version)
        VALUES('tesztid', 'tesztid', 'test_user3', 'MSS697', 'MSS697', 'GROUP_5', 'RECOGNIZED', 'RECOGNIZED', 
        'RECOGNIZED', '2022-02-18 08:05:30.000', '2022-02-18 10:08:30.000', 'FINISHED', '2022-02-18 09:05:30.000', 
        'init', '2022-02-18 09:05:30.000', 'init', 1)""",
        "DELETE FROM task WHERE x__id = 'tesztid'",
        "DELETE FROM check_package WHERE x__id = 'tesztid'",
        ],
    'core_template':[
        """INSERT INTO template
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, template_name, template_language, 
        template_channel, template_category, template_subject, body, example, default_parameters, template_version, 
        template_status, provider_template_id, valid_from, valid_until)
        VALUES('tesztid', '2022-04-21 17:23:58.580', 'test adat 9', '2022-04-21 17:23:58.604', 'test adat 9', 1, 
        'Test adat 02', 'hu', 'WHATSAPP', 'ACCOUNT_UPDATE', 'test', 'body', NULL, 'egyes,null', 1, 'CREATED', NULL, 
        '2022-02-11 12:50:00.708', '2022-02-11 12:50:00.708')""",
        "DELETE FROM template WHERE x__id = 'tesztid'",
    ],
    'core_vehicle': [
        """INSERT INTO toll_category
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, is_active, code, "name")
        VALUES('tesztid', '2022-04-11 17:21:44.576', 'system', '2022-04-11 17:21:44.576', 'system', 0, true, 22, 'Non-Truck')""",
        """INSERT INTO vehicle
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, owner_id, height, length, vehicle_make, 
        plate_number, vehicle_type, weight, width, toll_category_id)
        VALUES('tesztid', '2022-04-19 13:03:22.855', 'rewq', '2022-04-19 13:03:22.855', 'rewq', 0, 'tesztowner', NULL, NULL, 
        'toyota', '32423423', 'corolla', NULL, NULL, 'tesztid')""",
        "DELETE FROM vehicle WHERE x__id = 'tesztid'",
        "DELETE FROM toll_category WHERE x__id = 'tesztid'",
    ],
    'payment_account_info': [
        """INSERT INTO payment_method
        (x__id, psp_type, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "type")
        VALUES('tesztid', 'GOPAY', '2022-04-12 23:29:06.781', '3P6VP2T4S7K6D1TEST', NULL, NULL, 0, 'EWALLET')""",
        """INSERT INTO account_info
        (x__id, user_id, payment_method_token, status, x__insdate, x__insuser, x__moddate, x__moduser, x__version, 
        payment_method_id, binding_token)
        VALUES('tesztid', '3R1GRN63C0GTEST3', '1149b260-39d0-49c9-bdcf-d87d14d8aea1', 'ACTIVE', 
        '2022-05-10 14:26:20.177', 'dummy', '2022-05-10 14:26:56.377', 'dummy', 1, 'tesztid', NULL);""",
        "DELETE FROM account_info WHERE x__id = 'tesztid'",
        "DELETE FROM payment_method WHERE x__id = 'tesztid'",
    ],
    'document': [
        """INSERT INTO object_metadata
        (x__id, request_id, object_id, external_request_id, external_system_id, cluster_name, bucket_name, 
        document_issue_date, document_size, document_name, document_extension, ttl, ttl_cycle, ttl_value, archiving_hash, 
        archiving_timestamp, crc_result, authorization_data, additional_data, x__insdate, x__insuser, x__moddate, x__moduser, x__version)
        VALUES('tesztid', '3QHUOKF4GW363Y01', '3QHUOKF4GW363Y01', '3QHUOKF4GW363Y01', 'mlff', NULL, 
        'mlff-persistent', '2022-04-12', 16, 'test_txt_file', 'txt', NULL, 'PERSISTENT', 1, NULL, '2022-04-12 14:31:34.592', 
        '1361703869', NULL, NULL, '2022-04-12 14:31:34.650', '0', NULL, NULL, 0)""",
        "DELETE FROM object_metadata WHERE x__id = 'tesztid'",
    ],
    'payment_transaction': [
        """INSERT INTO payment_transaction
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, transaction_type, transaction_state, sent_at, 
        payer_id, amount, currency, reference_type, reference_id, reference_name, reference_description, psp_type, 
        payment_token, payment_method_type, payment_method_token, payment_url, capture_date, psp_processed_at, 
        psp_transaction_id, error_code, error_message, payment_mode)
        VALUES('tesztid', '2022-05-11 17:19:06.088', 'dummy', '2022-05-11 17:20:35.081', 'dummy', 6, 'AUTO', 
        'SUCCESS', '2022-05-11 17:20:34.010', '3R1GRN63DYT0QC0G', 100072, 'IDR', 'TRIP', 'TSId_TEST_3', 'RName_TEST_1', 
        'RDesc_TEST_1', 'GOPAY', '3RNGHMU2VC5D6307', 'EWALLET', 'f677add1-a435-406a-ba5b-7b3d61210bb0', NULL, NULL, 
        '2022-05-11 17:20:35.041', '8a8d9ee8-94ba-4d4c-bcbe-2493a558d10f', '0', NULL, NULL)""",
        """INSERT INTO retry_task
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, transaction_id, counter, next_retry_time)
        VALUES('tesztid', '2022-05-11 17:09:19.580', 'dummy', '2022-05-11 17:11:44.914', 'dummy', 1, 
        'tesztid', 2, NULL)""",
        "DELETE FROM retry_task WHERE x__id = 'tesztid'",
        "DELETE FROM payment_transaction WHERE x__id = 'tesztid'",
    ],
    'payment_psp_clearing': [
        """INSERT INTO psp_settlement_batch
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, state, psp_type, psp_settlement_type, 
        psp_settlement_package_id, period_start, period_end, amount, currency, generated_filename, generated_document_id)
        VALUES('tesztid', '2022-05-16 11:29:42.468', 'dummy', NULL, NULL, 0, 'WAITING_FOR_SETTLEMENT', 'GOPAY', 
        'TOLL', NULL, '2022-05-09 17:13:04.641', '2022-05-12 14:25:49.575', 501130, 'IDR', NULL, NULL)""",
        """INSERT INTO psp_clearing
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, psp_type, clearing_state, psp_processed_at, 
        psp_settlement_batch_id, psp_settlement_type, amount, currency, transaction_id, psp_transaction_id, payment_token, 
        reference_type, reference_id, reference_name, reference_description, correction, correction_info)
        VALUES('tesztid', '2022-05-10 09:36:50.870', 'dummy', '2022-05-16 11:29:42.481', 'dummy', 1, 'GOPAY', 
        'EXECUTED', '2022-05-10 09:36:50.568', 'tesztid', 'TOLL', 6000, 'IDR', '3RLKHEG8ATJITR02', 
        'a682a375-46e8-469e-a71c-189985b08a53', 'faab90e5-76d4-4ad2-b677-8bec59e9fe8a', 'TRIP', 'TRIP_Test_01', 
        'TRIP_Test_NAME_01', 'TRIP_Test_DESC_01', false, NULL)""",
        "DELETE FROM psp_clearing WHERE x__id = 'tesztid'",
        "DELETE FROM psp_settlement_batch WHERE x__id = 'tesztid'",
        """INSERT INTO psp_settlement_package
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, psp_type, amount, currency)
        VALUES('tesztid', '2022-05-24 07:59:17.291', 'dummy', NULL, NULL, 0, 'GOPAY', 2000, 'IDR')""",
        "DELETE FROM psp_settlement_package WHERE x__id = 'tesztid'",

    ],
    'enforcement_exemption': [
        """INSERT INTO exemption_vehicle
        (x__id, plate_number, x__insdate, x__insuser, x__moddate, x__moduser, x__version)
        VALUES('tesztid', 'tesztplate', '2022-04-08 09:08:48.419', 'teszt', NULL, NULL, 0)""",
        """INSERT INTO exemption_vehicle_segment
        (x__id, exemption_vehicle_id, country_wide, segment_id, valid_from, valid_to, status, x__insdate, x__insuser, 
        x__moddate, x__moduser, x__version, department, other_department, "source")
        VALUES('tesztid', 'tesztid', false, 'DEEAA6DD-5723-8dAa-fE4d-bA40B9de8D2e', '2022-05-13 13:18:14.182', 
        '2023-05-13 13:18:14.182', 'CREATED', '2022-05-13 14:44:38.525', '0', NULL, NULL, 0, 'FO', NULL, 'BACK_OFFICE')""",
        "DELETE FROM exemption_vehicle_segment WHERE x__id = 'tesztid'",
        "DELETE FROM exemption_vehicle WHERE x__id = 'tesztid'",

    ],
    'core_notification_common': [],
    'core_notification_pn': [],
    'core_notification_wa': [
        """INSERT INTO notification
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, recipient, channel, template_id, "language", 
        parameters, customer_id, source_service, object_type, object_id, response_status, response_id, attachments)
        VALUES('tesztid', CURRENT_TIMESTAMP, 'a', NULL, '', 0, 'a', 'WHATSAPP', 'a', 'a', '', 'a', 'a', 'a', 'a', 'READ', 'a', '')""",
        "DELETE FROM notification WHERE x__id = 'tesztid'"
    ],
    'core_notification_email': [],
    'payment_psp_proxy': [
        """INSERT INTO psp_data_assignment
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, psp_type, payment_token, psp_transaction_id)
        VALUES('tesztid', CURRENT_TIMESTAMP, 'a', NULL, '', 0, 'a', 'a', 'a')""",
        "DELETE FROM psp_data_assignment WHERE x__id = 'tesztid'"
    ],
    'eobu_tariff': [],
    'eobu_trip': [
        """INSERT INTO trip
        (x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, matching_session_id, customer_id, driver_id, 
        payer_id, vdu_id, plate_number, toll_category, status, start_time, end_time)
        VALUES('tesztid', '2022-05-13 12:50:06.925', '3QHR3Z608HM0K502', NULL, NULL, 0, 
        'tesztid', 'driverId', 'driverId', '3QHR3Z40FKB48A01', 'vduId', 'plateNumber', 1, 
        'MATCHED', '2022-05-13 11:50:06.811', NULL)""",
        "DELETE FROM trip WHERE x__id = 'tesztid'"
    ],
    'payment_retry': [
        """INSERT INTO task
        (x__id, item_type, item_id, counter, next_retry_time, x__insdate, x__insuser, x__moddate, x__moduser, x__version)
        VALUES('tesztid', 'auto_charge', 'transaction_id_01', 0, NULL, '2022-04-14 12:55:15.970', 'dummy', 
        '2022-04-14 12:59:09.449', 'dummy', 4)""",
        "DELETE FROM task WHERE x__id = 'tesztid'"
    ],
}