1. sqlacodegen postgresql+psycopg2://postgres:postgres@localhost:5432/akp_be --schema akp_authorization --outfile akp_authorization.py

2. partíció osztályok törlése
3. séma kiemelése egy közös változóba
    # Define a common schema name
    COMMON_SCHEMA = "akp_authorization"

    # Use a single MetaData object with the common schema
    metadata = MetaData(schema=COMMON_SCHEMA)

    class Base(DeclarativeBase):
        metadata = metadata

