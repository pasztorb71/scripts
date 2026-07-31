--1.2 deploy előtt

--- core
-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:e79acbfd3b59b97a2919e965c5f8712b'
WHERE filename = 'core_analytic/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:2ec52e675794b17a0f91711ca1daa698'
WHERE filename = 'core_customer/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:e2c47e310220d8181ac225974c80e778'
WHERE filename = 'core_genos/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:1561e99e39553d1619e4443351f7cb37'
WHERE filename = 'core_privateuser/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:d0ad6f2675f915857edd3f624858859a'
WHERE filename = 'core_ticket/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:e5945159071a3f894443f1e55cfc8761'
WHERE filename = 'core_vehicle/_create_dbs/create-database-db1.sql'
;

--- enforcement
-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:dd8f30934ad8e2fb6fc646bfb0d5158c'
WHERE filename = 'enforcement_detection_alert/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:a7620ac298c0da52e3b56dc06db0706d'
WHERE filename = 'enforcement_detection_image/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:24b3dd97ea10d6abfb0360302138524b'
WHERE filename = 'enforcement_detection_observation/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:613788a6e53e98af3df7c36765795d82'
WHERE filename = 'enforcement_detection/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:d34c6878f5480f7eb0b17d25e7816e56'
WHERE filename = 'enforcement_detection_transit_identifier/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:0867d1353b43649342d4c686b5b1557f'
WHERE filename = 'enforcement_detection_transition/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:c5c71004c08dbb676092c221c3977eff'
WHERE filename = 'enforcement_eligibility/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:a859dd7e8b3465474853c02376d52700'
WHERE filename = 'enforcement_exemption/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:5cf9d63f192ec90185b3e997df7b6070'
WHERE filename = 'enforcement_onsite_alert/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:a584f1584ba43a97d63af110d42a3d09'
WHERE filename = 'enforcement_onsite_alert_subscribe/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:023a490b76455220d4ba2ad0fae80430'
WHERE filename = 'enforcement_sanctioning_presumption/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:f6a1107559da711bb4034211dd94521e'
WHERE filename = 'enforcement_sanctioning_sanction/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:8b88153b4ccf12f69123c94e92861a61'
WHERE filename = 'enforcement_visual_check/_create_dbs/create-database-db1.sql'
;

--- eobu
-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:a2cf15871d69be22c22e494694dbf235'
WHERE filename = 'eobu_tariff/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:573a812c7370f68555ebd1cbe1e80858'
WHERE filename = 'eobu_trip/_create_dbs/create-database-db1.sql'
;

--- obu
-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:e2c81be0775bb829f512e236b07d4859'
WHERE filename = 'obu_obuprovider/_create_dbs/create-database-db1.sql'
;

--- payment
-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:cbf4122c787c1a8c3de005ac06d70274'
WHERE filename = 'payment_account_info/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:836562870259b76c870cf46c0c556500'
WHERE filename = 'payment_invoice/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:94add219b7af0750fdbbf2dd160a9f97'
WHERE filename = 'payment_psp_proxy/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:64b9f9a1fb6122a940806d0db6df7ae5'
WHERE filename = 'payment_transaction/_create_dbs/create-database-db1.sql'
;

--- settlement
-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:c7d907476d2eeba00c707bd7673ba54e'
WHERE filename = 'settlement_psp_clearing/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE  
public.databasechangelog d SET md5sum = '8:0ea52fd23b8edc473a37b3bd545e361f'
WHERE filename = 'settlement_tro_clearing/_create_dbs/create-database-db1.sql'
;

--- notification
-- postgres
UPDATE
public.databasechangelog d SET md5sum = '8:54eced86ae3cdb7970b267a0f5b5ebc6'
WHERE filename = 'core_notification_dispatcher/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE
public.databasechangelog d SET md5sum = '8:66ee1e202a574f80797a7ab4396db90f'
WHERE filename = 'core_notification_email/_create_dbs/create-database-db1.sql'
;

-- postgres
UPDATE
public.databasechangelog d SET md5sum = '8:00a15b23de4e6f7880ee67a7f3db4031'
WHERE filename = 'core_notification_wa/_create_dbs/create-database-db1.sql'
;


