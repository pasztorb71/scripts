from utils.generate_id import generateid


def read_file(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		rows = []
		for item in f.readlines()[1:]:
			item = item.replace('\n', '')
			rows.append(item)
	return rows


def create_rows_csv(rows):
	# CREATE TABLE akp_masterdata.station_x_device_x_device_unit (
	# 	x__id varchar(30) NOT NULL, -- Elsődleges kulcs
	# 	x__insdate timestamp DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'UTC'::text) NOT NULL, -- A beszúrás időpontja
	# 	x__insuser varchar(30) NOT NULL, -- A beszúrást végző felhasználó neve
	# 	x__moddate timestamp NULL, -- Az utolsó módosítás időpontja
	# 	x__moduser varchar(30) NULL, -- A módosítást végző felhasználó neve
	# 	x__version int8 DEFAULT 0 NOT NULL, -- Az aktuális verziója a rekordnak
	# 	station_id varchar(30) NOT NULL, -- Állomás azonosítója FK (STATION.X__ID)
	# 	device_id varchar(30) NOT NULL, -- Mérőműszer azonosítója FK (DEVICE.X__ID)
	# 	device_unit_id varchar(30) NOT NULL, -- Mérőműszeregység azonosítója FK (DEVICE_UNIT.X__ID)
	# 	valid_from timestamp NOT NULL, -- Érvényesség kezdete
	# 	valid_to timestamp NOT NULL, -- Érvényesség vége
	for row in rows:
		x__id = generateid()
		x__insuser = '0'
		x__version = 0
		station_id = row.split(',')[0]
		device_id = row.split(',')[1]


if __name__ == '__main__':
	rows = read_file('C:/Users/bertalan.pasztor/Downloads/traffic_2025-10-20-08-32.xlsx - Sheet0.csv')
	csv = create_rows_csv(rows)