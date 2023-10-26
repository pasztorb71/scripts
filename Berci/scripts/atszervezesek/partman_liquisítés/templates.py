template = """<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
  http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

  <changeSet id="partman-{name}" author="bertalan.pasztor" runOnChange="true" >
    <comment>partman/{name} install</comment>
    <sqlFile path="../{dir}/{name}" relativeToChangelogFile="true" splitStatements="false"/>
  </changeSet>

</databaseChangeLog>"""

incl_template = '    <include file="xmls/{name}.xml" relativeToChangelogFile="true"/>'

install_template = """<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

{incl_template}

</databaseChangeLog>"""
