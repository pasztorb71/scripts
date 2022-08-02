from modul.changeset import ChangeSet
import modul.db_conn as db_conn
from modul.directory import Dir


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Melyik release Tag-et telepítjük?

# Melyik környezetre akarunk telepíteni?

# 1db DB, vagy az összes telepítése?

# Service-k felsorolása, 1. az adatbázis környezet telepítése, utána a service-k


def telepito():
    chset = ChangeSet()

    chset.header.author = "endre.balazs"
    chset.header.changeset_id = "CUSTOMER_ROLES"
    chset.header.run_on_change = True

    chset.comment.text = "A customer Schema Role-ok létrehozása.."
    chset.precondition.on_fail = "MARK_RAN"
    chset.precondition.on_error = "HALT"
    chset.precondition.sql_check.expected_result_num = 1
    chset.precondition.sql_check.text = "SELECT count(*) FROM pg_catalog.pg_database WHERE datname = 'core_customer' and not exists (SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = 'customer_full')"

    print(chset)

    conn = db_conn.sqlite_connection(r"C:\sqlite\db\pythonsqlite.db")
    c = conn.cursor()


def directory():
    liquibase_dir = Dir(name="liquibase", parent_id=0)

    main_dir = liquibase_dir
    print(main_dir, main_dir.parent_id, main_dir.obj_id)

    sub_dir = Dir(name="core_customer")
    main_dir.add_dir(sub_dir)
    # sub_dir = dir.dirs[-1]
    print(sub_dir, sub_dir.parent_id, sub_dir.obj_id)

    sub_dir.add_dir("_init_dbs")
    sub_dir = sub_dir.dirs[-1]
    print(sub_dir, sub_dir.parent_id, sub_dir.obj_id)

    # dir.add_file("dwh_read-user.sql")
    # dir.add_file("read-user.sql")
    # dir.add_file("service-user.sql")
    # dir.add_file("stream-user.sql")

    return liquibase_dir


if __name__ == '__main__':
    # telepito()
    dir = directory()

    print("")
    print("Parent:", dir.parent_id, " Obj:", dir.obj_id, "\n")

    print("All obj:", dir.all_obj)
    print("List:", [x.obj_id for x in dir.files])
    print([(x.obj_id, x.parent_id) for x in dir.files])
