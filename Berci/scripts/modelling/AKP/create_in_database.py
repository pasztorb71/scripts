""" This script creates a PostgreSQL database and the necessary tables for the AKP authorization system. """
from sqlalchemy import create_engine, text
from akp_authorization import Base


def create_all_tables(l_database_name: str) -> None:
    """ Create all tables in the specified PostgreSQL database. """
    url = f"postgresql://postgres:postgres@localhost:5432/{l_database_name}"
    engine = create_engine(url)
    # create schema if not exists
    schema_name = Base.metadata.schema
    with engine.connect() as conn:
        conn.execute(
                text(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"')
        )
        conn.commit()
        print(f"Séma létrehozva: {schema_name}")
    Base.metadata.create_all(engine)
    print("All tables created successfully.")


def create_database(database_name: str) -> None:
    """ Create a PostgreSQL database if it does not exist. """
    url = f"postgresql://postgres:postgres@localhost:5432/{database_name}"
    default_url = url.replace(f"/{database_name}", "/postgres")
    engine = create_engine(default_url, isolation_level="AUTOCOMMIT")

    with engine.connect() as conn:
        # Ellenőrizzük, létezik-e az adatbázis
        result = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname=:dbname"),
            {"dbname": database_name}
        )
        if result.scalar():
            print(f"Adatbázis már létezik: {database_name}")
        else:
            # Létrehozás
            conn.execute(text(f'CREATE DATABASE "{database_name}"'))
            print(f"Adatbázis létrehozva: {database_name}")

if __name__ == "__main__":
    database_name = 'test'
    create_database(database_name)
    create_all_tables(database_name)
