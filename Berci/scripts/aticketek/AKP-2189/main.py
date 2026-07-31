from classes.Trino import Trino_class


def filter_tables(tablenames: list, filter: str):
	out = []
	for tablename in tablenames:
		table_info = {}
		ddl = trino.get_ddl(tablename)
		if filter in ddl:
			table_info['name'] = tablename
			table_info['partitioning'] = ddl.split('partitioning =', 1)[1].split(',', 1)[0]
			table_info['sorted_by'] = ddl.split('sorted_by =', 1)[1].split('\n', 1)[0].replace('md_process_id','md_load_id')
			out.append(table_info)

	# write to json file
	with open('filtered_tables.json', 'w', encoding='utf-8') as f:
		import json
		json.dump(out, f, indent=4, ensure_ascii=False)
	return out

# Load from json file
def load_from_file(param):
	with open(param, 'r', encoding='utf-8') as f:
		import json
		data = json.load(f)
	return data


def gen_create_new_tables(tables_data, postfix):
	out = []
	for tabledata in tables_data:
		out.append(f"""CREATE TABLE lakehouse.consolidated.{tabledata['name']}{postfix}
WITH (
    partitioning = {tabledata['partitioning']},
    sorted_by = {tabledata['sorted_by']}
)
AS
SELECT * FROM lakehouse.consolidated.{tabledata['name']};
""")
	return out


def write_to_file(filename, data):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in data:
			f.write(line)
			f.write('\n')


if __name__ == '__main__':
	#trino = Trino_class('akp-dev-dl-trino.gcp.icellmobilsoft.hu', 443, 'admin', 'lakehouse', 'consolidated')
	#table_names = [x[0] for x in trino.query("SELECT table_name FROM lakehouse.information_schema.tables WHERE table_schema = 'consolidated' and table_type = 'BASE TABLE'")]
	#table_names_filtered = filter_tables(table_names, "ARRAY['md_process_id")
	table_data = load_from_file('filtered_tables.json')
	create_new_tables = gen_create_new_tables(table_data, '_new')
	#drop_commands = [f"DROP TABLE lakehouse.consolidated.{x['name']}_new;" for x in table_data]
	#write_to_file('drop_new_tables.sql', drop_commands)
	write_to_file('01_create_new_tables.sql', create_new_tables)
	rename_commands_to_old = [f"ALTER TABLE lakehouse.consolidated.{x['name']} RENAME TO {x['name']}_old;" for x in table_data]
	rename_commands_from_new = [f"ALTER TABLE lakehouse.consolidated.{x['name']}_new RENAME TO {x['name']};" for x in table_data]
	write_to_file('02_rename_to_old.sql', rename_commands_to_old)
	write_to_file('03_rename_from_new.sql', rename_commands_from_new)
	drop_old_tables = [f"DROP TABLE lakehouse.consolidated.{x['name']}_old;" for x in table_data]
	write_to_file('04_drop_old_tables.sql', drop_old_tables)