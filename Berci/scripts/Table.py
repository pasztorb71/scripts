from dataclasses import dataclass

import psycopg2

from Column import Column
from models import ForeignKey

@dataclass()
class ForeignKey:
    name: str = None
    fk_column: str = None
    ref_table: str = None
    deferrable: bool = False
    update: str = None
    delete: str = None

class Table:
    def __init__(self, table, connection=None):
        self.conn = connection
        self.schema, self.name = table.split('.')
        self.foreign_keys: dict[str, ForeignKey] = None

    def __str__(self):
        return f'{self.schema}.{self.name}'

    def setconn(self, connection: psycopg2.extensions.connection):
        self.conn = connection

    def is_check_constraint_on_column(self, column):
        stmt = f"SELECT count(*) " \
               f"FROM pg_constraint c " \
               f"JOIN pg_attribute  a ON a.attrelid = c.conrelid " \
               f"AND a.attnum = ANY(c.conkey) " \
               f"WHERE c.conrelid = '{self.schema}.{self.name}'::regclass " \
               f"AND c.contype = 'c' " \
               f"AND a.attname = '{column}' "
        cur = self.conn.cursor()
        cur.execute(stmt)
        res = cur.fetchone()
        return res[0] == 1

    def gen_drop_constraint_stmt(self, column):
        consname = Column(self.conn, f"{self.schema}.{self.name}", column).get_constraint_name()
        return f'ALTER TABLE {self.name} DROP CONSTRAINT {consname};'

    def fill_foreign_keys(self):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("""
                    select kcu.constraint_name, kcu.column_name, reft.relname
                          ,cons.condeferrable, cons.confupdtype, cons.confdeltype
                    from pg_catalog.pg_constraint cons
                    join pg_catalog.pg_class cls
                      on cls.oid = cons.conrelid
                    join pg_catalog.pg_namespace nsp
                      on nsp.oid = cons.connamespace
                    join pg_catalog.pg_class reft
                      on reft.oid = cons.confrelid
                    join information_schema.key_column_usage kcu
                      on kcu.constraint_name = cons.conname
                    where nsp.nspname = %s
                      and cls.relname = %s
                      and contype = 'f'""", (self.schema, self.name))
                res = cur.fetchall()
                self.foreign_keys = dict([_[0], ForeignKey(_[0], _[1], _[2], _[3], _[4], _[5])] for _ in res)

    def foreign_key_write(self, filepath: str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            for fk in self.foreign_keys.values():
                file.write(f"- fk_column: {fk.fk_column}\n")
                file.write(f"  name: {fk.name}\n")
                file.write(f"  ref_table: {fk.ref_table}\n")
                file.write(f"  deferrable: {fk.deferrable}\n")
                file.write(f"  update: {fk.update}\n")
                file.write(f"  delete: {fk.delete}\n")

    def foreign_key_read_from_file(self, filepath: str):
        try:
            with open(filepath, "r") as file:
                res = yaml.safe_load(file)
                self.foreign_keys = dict()
                if res:
                    self.foreign_keys = dict([fk['name'], ForeignKey(fk['name'], fk['fk_column'], fk['ref_table']
                                                 , fk['deferrable'], fk['update'], fk['delete'])] for fk in res)
        except FileNotFoundError:
            Logger.logger.warning(f"A megadott file: {filepath} nem létezik.")

    def _get_foreign_key_by_name(self, fk_name: str) -> ForeignKey:
        return self.foreign_keys[fk_name]

    def foreign_key_remove(self, fk_name: str):
        self.foreign_keys.pop(fk_name)

    def add_foreign_key(self, fk: ForeignKey):
        self.foreign_keys[fk.name] = fk

    def fk_disable_all(self):
        self._exit_if_noconn()
        fk_file = f'foreign_keys/{self.schema}-{self.name}.yml'
        if os.path.isfile(fk_file):
            raise FileExistsError(f"{fk_file} már létezik!")
        self.foreign_key_write(f'foreign_keys/{self.schema}-{self.name}.yml')
        cur = self.conn.cursor()
        for fk in self.foreign_keys.values():
            cur.execute(f"ALTER TABLE {self.schema}.{self.name} DROP CONSTRAINT {fk.name}")
            Logger.logger.info(f'A {self.schema}.{self.name} táblán a {fk.name} eldobva.')
        self.conn.commit()
        self.foreign_keys.clear()

    def fk_enable_all(self):
        self._exit_if_noconn()
        try:
            self.foreign_key_read_from_file(f'foreign_keys/{self.schema}-{self.name}.yml')
            if not self.foreign_keys:
                Logger.logger.warning(f'A {self.schema}.{self.name} tábla nem tartalmaz FK-t.')
                return
            cur = self.conn.cursor()
            for fk in self.foreign_keys.values():
                try:
                    cur.execute(f"""ALTER TABLE {self.schema}.{self.name} ADD CONSTRAINT {fk.name} 
                                FOREIGN KEY ({fk.fk_column}) REFERENCES {self.schema}.{fk.ref_table}(x__id) 
                                {' ON UPDATE RESTRICT' if fk.update == 'r' else ''}
                                {' ON DELETE CASCADE' if fk.delete == 'c' else ''}
                                {' DEFERRABLE' if fk.deferrable else ''}""")
                    Logger.logger.info(f'A {self.schema}-{self.name} táblán a(z) {fk.name} foreign key létrehozva.')
                except psycopg2.errors.DuplicateObject:
                    Logger.logger.warning(f'A {self.schema}-{self.name} táblán már rajta van a(z) {fk.name} foreign key.')
            self.conn.commit()
            os.remove(f'foreign_keys/{self.schema}-{self.name}.yml')
            Logger.logger.info(f'A foreign_keys/{self.schema}-{self.name}.yml file törölve.')
        except FileNotFoundError:
            Logger.logger.warning(f'A foreign_keys/{self.schema}-{self.name}.yml nem létezik.')

    def _exit_if_noconn(self):
        if not self.conn:
            Logger.logger.error(f"A {self.name} táblán a connection nincs beállítva!")
            raise Exception("A tábla connection nincs beállítva!")

    def dump_data(self, dbname: str):
        self._exit_if_noconn()
        filepath = f'dumps/{dbname}-{self.schema}-{self.name}.csv'
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with self.conn:
            with self.conn.cursor() as cur:
                with open(filepath, 'w', newline='', encoding="utf-8") as fp:
                    a = csv.writer(fp, delimiter=';')
                    cur.execute(f'select * from {self.schema}.{self.name}')
                    for row in cur.fetchall():
                        a.writerow(row)
        Logger.logger.info(f'A {self.schema}.{self.name} tábla tartalma a dumps/{dbname}-{self.schema}-{self.name}.csv file-be letöltve.')

    def load_data(self, dbname: str):
        self._exit_if_noconn()
        filepath = f'dumps/{dbname}-{self.schema}-{self.name}.csv'
        cur = self.conn.cursor()
        if not self.is_empty():
            Logger.logger.error(f'A {self.schema}.{self.name} tábla nem üres, csak üres táblába lehet betölteni!')
            raise Exception(f"A {self.schema}.{self.name} tábla nem üres!")
        with open(filepath, 'r', newline='', encoding="utf-8") as fp:
            for line in csv.reader(fp, delimiter=';'):
                cur.execute(self.csvrow_to_insert(line))
            self.conn.commit()

    def csvrow_to_insert(self, line: object) -> str:
        sql = f"INSERT INTO {self.schema}.{self.name} VALUES ("
        for value in line:
            if len(value) == 0:
                sql = sql + "NULL, "
            else:
                value = value.replace("'", "''''")
                sql = sql + f"'{value}', "
        sql = sql[:-2]
        sql = sql + ")"
        return sql

    def is_empty(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT count(1) FROM {self.schema}.{self.name}")
        self.conn.commit()
        row = cur.fetchone()
        return row[0] == 0


    def has_history(self):
        cur = self.conn.cursor()
        cur.execute(f"select count(*) from pg_tables where schemaname = '{self.schema}' and tablename = '{self.name}$hist'")
        res = cur.fetchone()[0]
        return res == 1

    def has_partitions(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT count(*) FROM pg_catalog.pg_inherits WHERE inhparent = '{self.schema}.{self.name}'::regclass")
        res = cur.fetchone()[0]
        return res > 0
