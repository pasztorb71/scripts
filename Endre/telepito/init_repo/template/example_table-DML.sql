--liquibase formatted sql

--===============================================================================================--
-- DML ==
---------------------------------------------------------------------------------------------------
--changeset endre.balazs:TOLL_CATEGORY-DML runOnChange:true failOnError:true stripComments:true
--comment A TOLL_CATEGORY tábla feltöltése, induló értékekkel.. 
---------------------------------------------------------------------------------------------------
/*
SET CONSTRAINTS ALL DEFERRED;

--DELETE FROM vehicle.toll_category WHERE x__id IN 
	('TLC001', 'TLC002', 'TLC003', 'TLC004', 'TLC005', 'TLC006');
  
INSERT INTO vehicle.toll_category (X__ID,X__VERSION,X__INSDATE,X__INSUSER,X__MODDATE,X__MODUSER,IS_ACTIVE,CODE,NAME)
	VALUES ('TLC001',0,CURRENT_TIMESTAMP,'system',CURRENT_TIMESTAMP,'system',true,1,'Non-Truck');
	
INSERT INTO vehicle.toll_category (X__ID,X__VERSION,X__INSDATE,X__INSUSER,X__MODDATE,X__MODUSER,IS_ACTIVE,CODE,NAME)
	VALUES ('TLC002',0,CURRENT_TIMESTAMP,'system',CURRENT_TIMESTAMP,'system',true,2,'2-Axle Truck');
	
INSERT INTO vehicle.toll_category (X__ID,X__VERSION,X__INSDATE,X__INSUSER,X__MODDATE,X__MODUSER,IS_ACTIVE,CODE,NAME)
	VALUES ('TLC003',0,CURRENT_TIMESTAMP,'system',CURRENT_TIMESTAMP,'system',true,3,'3-Axle Truck');
	
INSERT INTO vehicle.toll_category (X__ID,X__VERSION,X__INSDATE,X__INSUSER,X__MODDATE,X__MODUSER,IS_ACTIVE,CODE,NAME)
	VALUES ('TLC004',0,CURRENT_TIMESTAMP,'system',CURRENT_TIMESTAMP,'system',true,4,'4-Axle Truck');
	
INSERT INTO vehicle.toll_category (X__ID,X__VERSION,X__INSDATE,X__INSUSER,X__MODDATE,X__MODUSER,IS_ACTIVE,CODE,NAME)
	VALUES ('TLC005',0,CURRENT_TIMESTAMP,'system',CURRENT_TIMESTAMP,'system',true,5,'≥ 5-Axle Truck');
	
INSERT INTO vehicle.toll_category (X__ID,X__VERSION,X__INSDATE,X__INSUSER,X__MODDATE,X__MODUSER,IS_ACTIVE,CODE,NAME)
	VALUES ('TLC006',0,CURRENT_TIMESTAMP,'system',CURRENT_TIMESTAMP,'system',true,6,'motorcycle');
  
-- -- --
COMMIT;
-- -- --

SET CONSTRAINTS ALL IMMEDIATE;
*/