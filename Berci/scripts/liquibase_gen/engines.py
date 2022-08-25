from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.dialects.oracle import cx_oracle
from sqlalchemy.sql.ddl import CreateTable


def create_db_engine(db, user, password, local='y'):
    host = 'localhost:5434'
    if local == 'gcp':
        host = '34.79.34.14'
    engine = create_engine('postgresql+psycopg2://' + user + ':' + password + '@' + host + '/' + db)
    try:
        engine.connect()
    except:
        return None
    return engine

def create_oracle_engine(db, user, password, local='y'):
    host = 'localhost'
    if local == 'gcp':
        host = '34.79.34.14'
    print('oracle://' + user + ':' + password + '@' + host + ':1522/?service_name=' + db)
    engine = create_engine('oracle://' + user + ':' + password + '@' + host + ':1522/?service_name=' + db)
    try:
        engine.connect()
    except:
        return None
    return engine

if __name__ == '__main__':
    e = create_db_engine('core_customer', 'postgres', 'fLXyFS0RpmIX9uxGII4N')
    meta_data = MetaData(schema='customer', bind=e)
    MetaData.reflect(meta_data, bind=e)
    table1 = meta_data.tables['customer.customer'].create(bind=e)
    print(CreateTable(table1, bind=e))
    exit(0)
    #meta_data.create(table1)
    o = create_oracle_engine('SANDBOX2', 'mlff_dba', 'mlff_dba')
    exit(0)

    e = create_db_engine('postgres', 'postgres', 'mysecretpassword')
    print(CreateTable(table1, bind=e))
    exit(0)
    meta = MetaData()
    meta_data.reflect(bind=e)
    meta.create_all(e, tables=[table1])

    a=1
