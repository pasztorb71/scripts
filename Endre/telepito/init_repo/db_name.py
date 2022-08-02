class DBName:

    def __init__(self, domain_name, service_name, schema_name):
        self._domain_name = domain_name
        self._service_name = service_name
        self._schema_name = schema_name
        self._db_name = "_".join([self._domain_name, self._service_name]).lower()

    def __str__(self):
        return f"DB_Name:{self._db_name} Schema_Name:{self._schema_name}"

    @property
    def domain_name(self):
        return self._domain_name

    @property
    def service_name(self):
        return self._service_name

    @property
    def schema_name(self):
        return self._schema_name

    @property
    def db_name(self):
        return self._db_name
