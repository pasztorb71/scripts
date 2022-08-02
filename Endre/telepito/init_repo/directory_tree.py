class DirectoryTree:

    def __init__(self, db_name_obj):
        self._db_name = db_name_obj.db_name
        self._service_name = db_name_obj.service_name
        self._schema_name = db_name_obj.schema_name
        self._structure_init()

    # -- structure --
    @property
    def structure(self):
        return self._structure

    def _structure_init(self):
        self._structure = [
            {"obj_id": 1, "parent_id": 0, "name": "liquibase", "type": "D"},
            # --  1: liquibase -- level1
            {"obj_id": 2, "parent_id": 1, "name": self._db_name, "type": "D"},
            # --  2: core_customer -- level2
            {"obj_id": 3, "parent_id": 2, "name": "_init_dbs", "type": "D"},
            {"obj_id": 4, "parent_id": 2, "name": "all-modules", "type": "D"},
            {"obj_id": 5, "parent_id": 2, "name": self._schema_name, "type": "D"},
            {"obj_id": 6, "parent_id": 2, "name": "install-parameters.xml", "type": "F",
             "template": "06_install-parameters.txt"},
            {"obj_id": 7, "parent_id": 2, "name": "liquibase-install-step-01.xml", "type": "F",
             "template": "07_liquibase-install-step-01.txt"},
            {"obj_id": 8, "parent_id": 2, "name": "liquibase-install-step-02.xml", "type": "F",
             "template": "08_liquibase-install-step-02.txt"},
            # --  3:_init_dbs -- level3
            {"obj_id": 9, "parent_id": 3, "name": self._db_name, "type": "D"},
            {"obj_id": 10, "parent_id": 3, "name": self._db_name + "-db-install.xml", "type": "F",
             "template": "10_xy-db-install.txt"},
            # --  9: core_customer -- level4
            {"obj_id": 11, "parent_id": 9, "name": self._service_name + "_service", "type": "D"},
            {"obj_id": 12, "parent_id": 9, "name": "create-database.sql", "type": "F",
             "template": "12_create-database.txt"},
            # -- 11: customer -- level5
            {"obj_id": 13, "parent_id": 11, "name": "dwh_read-user.sql", "type": "F",
             "template": "13_dwh_read-user.txt"},
            {"obj_id": 14, "parent_id": 11, "name": "read-user.sql", "type": "F", "template": "14_read-user.txt"},
            {"obj_id": 15, "parent_id": 11, "name": "service-user.sql", "type": "F", "template": "15_service-user.txt"},
            {"obj_id": 16, "parent_id": 11, "name": "stream-user.sql", "type": "F", "template": "16_stream-user.txt"},
            # --  4: all-modules -- level3
            {"obj_id": 17, "parent_id": 4, "name": "functions", "type": "D"},
            {"obj_id": 18, "parent_id": 4, "name": "procedures", "type": "D"},
            {"obj_id": 19, "parent_id": 4, "name": "tables", "type": "D"},
            # -- 17: functions -- level4
            {"obj_id": 20, "parent_id": 17, "name": "gen_create_table_statement.sql", "type": "F",
             "template": "20_gen_create_table_statement.txt"},
            {"obj_id": 21, "parent_id": 17, "name": "gen_hist_trigger_function.sql", "type": "F",
             "template": "21_gen_hist_trigger_function.txt"},
            # -- 18: procedures -- level4
            {"obj_id": 22, "parent_id": 18, "name": "hist_table_generator.sql", "type": "F",
             "template": "22_hist_table_generator.txt"},
            {"obj_id": 23, "parent_id": 18, "name": "hist_trigger_generator.sql", "type": "F",
             "template": "23_hist_trigger_generator.txt"},
            # -- 19: tables -- level4
            {"obj_id": 24, "parent_id": 19, "name": "databasechangelog", "type": "D"},
            # -- 24: databasechangelog --
            {"obj_id": 25, "parent_id": 24, "name": "databasechangelog-DDL-0.00.1.sql", "type": "F",
             "template": "25_databasechangelog-DDL-0.00.1.txt"},
            # --  5: customer -- level3
            {"obj_id": 45, "parent_id": 5, "name": "dmls", "type": "D"},
            {"obj_id": 26, "parent_id": 5, "name": "schema", "type": "D"},
            {"obj_id": 27, "parent_id": 5, "name": "tables", "type": "D"},
            {"obj_id": 28, "parent_id": 5, "name": "views", "type": "D"},
            {"obj_id": 29, "parent_id": 5, "name": "xml-version-tree", "type": "D"},
            {"obj_id": 30, "parent_id": 5, "name": "install-dmls.xml", "type": "F", "template": "30_install-dmls.txt"},
            {"obj_id": 31, "parent_id": 5, "name": "install-modules.xml", "type": "F",
             "template": "31_install-modules.txt"},
            {"obj_id": 32, "parent_id": 5, "name": "liquibase-install-schema.xml", "type": "F",
             "template": "32_liquibase-install-schema.txt"},
            {"obj_id": 33, "parent_id": 5, "name": "schema-versions.xml", "type": "F",
             "template": "33_schema-versions.txt"},
            # -- 26: schema -- level4
            {"obj_id": 34, "parent_id": 26, "name": "alter-dwh_read-user.sql", "type": "F",
             "template": "34_alter-dwh_read-user.txt"},
            {"obj_id": 35, "parent_id": 26, "name": "alter-read-user.sql", "type": "F",
             "template": "35_alter-read-user.txt"},
            {"obj_id": 36, "parent_id": 26, "name": "alter-service-user.sql", "type": "F",
             "template": "36_alter-service-user.txt"},
            {"obj_id": 37, "parent_id": 26, "name": "alter-stream-user.sql", "type": "F",
             "template": "37_alter-stream-user.txt"},
            {"obj_id": 38, "parent_id": 26, "name": "create-roles.sql", "type": "F", "template": "38_create-roles.txt"},
            {"obj_id": 39, "parent_id": 26, "name": "create-schema.sql", "type": "F",
             "template": "39_create-schema.txt"},
            {"obj_id": 40, "parent_id": 26, "name": "install-schema.xml", "type": "F",
             "template": "40_install-schema.txt"},
            # -- 27: tables --  level4 -- csak az indító xml kerül ide..
            {"obj_id": 41, "parent_id": 27, "name": "create-tables.xml", "type": "F",
             "template": "41_create-tables.txt"},
            # -- 28: views --  level4 -- csak az indító xml kerül ide..
            {"obj_id": 42, "parent_id": 28, "name": "create-views.xml", "type": "F", "template": "42_create-views.txt"},
            # -- 29: xml-version-tree --  level4
            {"obj_id": 43, "parent_id": 29, "name": "version-0", "type": "D"},
            {"obj_id": 44, "parent_id": 29, "name": "schema-version-0.xml", "type": "F",
             "template": "44_schema-version-0.txt"}
        ]
        # ** last obj_id: 45 **


# if __name__ == '__main__':
#     from db_name import DBName
#
#     db_n = DBName(domain_name="core", service_name="customer", schema_name="customer")
#     print(db_n)
#
#     db_tree = DirectoryTree(db_n)
#     print(db_tree.structure)
