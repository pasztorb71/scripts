import Database
import Environment

e = Environment.Env('local')
dblist = e.database_names
for db in dblist[0:]:
    db = Database.Database(db)
    for name, table in db.tables.items():
        c = table.check_constraints
        for i in c[0:]:
            enums = i.enums_in_constraint
            if enums:
                print(f'{db.name} : {i} : {i.enums_in_constraint}')
