from db_name import DBName


class DBConf(DBName):
    dba_user_name = "postgres"
    schema_password = "mlffTitkosPassword123!"

    def __init__(self, db_name_obj, project="mlff", database_type="postgredb"):
        super().__init__(domain_name=db_name_obj.domain_name,
                         service_name=db_name_obj.service_name,
                         schema_name=db_name_obj.schema_name)
        self._replace_list_init()

        self._project = project
        self._database_type = database_type
        # self._repo_name = self._project + "-" + self._db_name.replace("_", "-") + "-" + self._database_type
        self._repo_name = "-".join([self._project, self._db_name.replace("_", "-"), self._database_type])

    # -- replace_list --
    @property
    def replace_list(self):
        return self._replace_list

    def _replace_list_init(self):
        self._replace_list = {"db_name": self.db_name.lower(),
                              "DB_NAME": self.db_name.upper(),
                              "schema_name": self.schema_name.lower(),
                              "SCHEMA_NAME": self.schema_name.upper(),
                              "service_name": self.service_name.lower(),
                              "SERVICE_NAME": self.service_name.upper(),
                              "dba_user_name": self.dba_user_name,
                              "schema_password": self.schema_password}

    @property
    def repo_name(self):
        return self._repo_name

    @property
    def project(self):
        return self._project

    @property
    def database_type(self):
        return self._database_type


# if __name__ == '__main__':
#     db_n = DBName(domain_name="core", service_name="customer", schema_name="customer")
#     print(db_n)
#
#     db_c = DBConf(db_name_obj=db_n)
#     print(db_c.replace_list)
#     print(db_c.db_name, db_c.repo_name)
