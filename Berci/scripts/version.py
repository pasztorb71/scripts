import os.path

from utils_file import append_to_file_after_line_last_occurence

version_file_tmpl = """<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

    <!-- ============================================================================== -->
    <!-- Adott alverzióhoz tartozó, sql tábla változáskat gyűjtő xml leíró file..       -->
    <!-- ============================================================================== -->


    <!-- ============================================================================== -->

</databaseChangeLog>
"""

table_ddl_tmpl = """--liquibase formatted sql

--===============================================================================================--
-- TABLE ==
"""

def check_schema_version_file(version, repo):
    version_arr = version.split('.')
    main_ver = version_arr[0]
    patch_ver = version_arr[1]
    fix_ver = version_arr[2]
    version_dir = repo.get_schema_version_dir()
    schema_version_file = '/'.join([version_dir, 'schema-version-'+main_ver+'.xml'])
    with open(schema_version_file, 'r', encoding='utf-8') as f:
        content = f.read()
    version_line = f'<include file="version-0/{version}.xml" relativeToChangelogFile="true" labels="{main_ver}.{patch_ver}"/>'
    if version_line not in content:
        print(f"Schema version file: {schema_version_file}")
        message = 'Not patch version row in schema version file!'
        print(message)
        if input("Create version row? [y/n]") == "y":
            append_to_file_after_line_last_occurence(schema_version_file, '<include file="version-0', '    ' + version_line)
        else:
            return
    version_file_path = '/'.join([version_dir, 'version-' + main_ver, version + '.xml'])
    if not os.path.isfile(version_file_path):
        message = 'Version file does not exists!'
        print(message)
        if input("Create version file? [y/n]") == "y":
            with open(version_file_path, 'w', encoding='utf-8') as f:
                f.write(version_file_tmpl)
        else:
            return message
    return 'ok'


def check_table_version_file(version, repo, tablename):
    if '$hist' in tablename:
        return
    table_dir = '/'.join([repo.get_tables_dir(), tablename])
    ddlfile_path = '/'.join([table_dir, tablename+'-DDL-'+version+'.sql'])
    version_dir = repo.get_table_version_dir()
    table_version_file = '/'.join([version_dir, version + '.xml'])
    with open(table_version_file, 'r', encoding='utf-8') as f:
        content = f.read()
    table_ddl_line = f'<include file="../../{tablename}/{tablename}-DDL-{version}.sql" relativeToChangelogFile="true"/>'
    if table_ddl_line not in content:
        print(f"Table version file: {table_version_file}")
        message = f'No table DDL file version row in table version file! ({tablename})'
        print(message)
        if input("Create table row? [y/n]") == "y":
            append_to_file_after_line_last_occurence(table_version_file, '<include file="../../', '    ' + table_ddl_line)
        else:
            return

    if not os.path.isfile(ddlfile_path):
        print(f"Missing DDL file: {ddlfile_path}")
        if input("Create DDL file? [y/n]") == "y":
            if not os.path.isdir(ddlfile_path):
                os.mkdir(ddlfile_path.rsplit('/')[0]) if not os.path.isdir(ddlfile_path.rsplit('/')[0]) else ''
            with open(ddlfile_path, 'w', encoding='utf-8') as f:
                f.write(table_ddl_tmpl)
        else:
            print('DDL file not created!')
    return None

def check_schema_version_file(version, repo, tablename):
    if '$hist' in tablename:
        return
    table_dir = '/'.join([repo.get_tables_dir(), tablename])
    ddlfile_path = '/'.join([table_dir, tablename+'-DDL-'+version+'.sql'])
    version_dir = repo.get_table_version_dir()
    table_version_file = '/'.join([version_dir, version + '.xml'])
    with open(table_version_file, 'r', encoding='utf-8') as f:
        content = f.read()
    table_ddl_line = f'<include file="../../{tablename}/{tablename}-DDL-{version}.sql" relativeToChangelogFile="true"/>'
    if table_ddl_line not in content:
        print(f"Table version file: {table_version_file}")
        message = f'No table DDL file version row in table version file! ({tablename})'
        print(message)
        if input("Create table row? [y/n]") == "y":
            append_to_file_after_line_last_occurence(table_version_file, '<include file="../../', '    ' + table_ddl_line)
        else:
            return

    if not os.path.isfile(ddlfile_path):
        print(f"Missing DDL file: {ddlfile_path}")
        if input("Create DDL file? [y/n]") == "y":
            if not os.path.isdir(ddlfile_path):
                os.mkdir(ddlfile_path.rsplit('/')[0]) if not os.path.isdir(ddlfile_path.rsplit('/')[0]) else ''
            with open(ddlfile_path, 'w', encoding='utf-8') as f:
                f.write(table_ddl_tmpl)
        else:
            print('DDL file not created!')
    return None