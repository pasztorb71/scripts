# read inserts.txt
with open('inserts.sql', 'r', encoding='utf-8') as f:
	inserts = f.readlines()

out_inserts = []
for insert in inserts[0:]:
	command = insert.split(',')
	command[16] = 'current_timestamp'  # set md_load_date to current_timestamp
	new_insert = ','.join(command)
	out_inserts.append(new_insert)

with open('out_inserts.sql', 'w', encoding='utf-8') as f:
	for line in out_inserts:
		f.write(line)

