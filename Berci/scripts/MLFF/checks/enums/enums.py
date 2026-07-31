from classes import Environment
from classes.Column import Column

env = 'cantas_test'
e = Environment.Env(env)
dblist = e.databases
f = open(f'constraints_{env}.out', 'w')
for db in dblist[0:]:
    for name, table in db.tables.items():
        c = table.check_constraints
        for i in c[0:]:
            col = Column(db, table.name, i.colname, conn=db.conn, schema=table.schema)
            nullable = col.nullable
            enums = i.enums_in_constraint
            if enums and db.name != 'Adventureworks':
                if nullable == 'YES':
                    enums.append('NULL')
                value_count = col.count_values
                f.write(f'{db.name} : {i} : {enums} : {value_count}\n')
f.close()