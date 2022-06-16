precondition_column = "expectedResult:1 SELECT count(*) FROM information_schema.columns WHERE table_schema = '###schema###' AND table_name = '###table###' AND column_name = '###column###'"
column_template = '''---------------------------------------------------------------------------------------------------
--changeset ###author###:###table###-DDL-###version###-###jira###-###changesetid### runOnChange:true
--comment ###comment###
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check ###precondition###
---------------------------------------------------------------------------------------------------
'''

precondition_constraint = "expectedResult:1 SELECT count(*) FROM information_schema.columns WHERE table_schema = '###schema###' AND table_name = '###table###' AND column_name = '###column###'"
constraint_template = '''---------------------------------------------------------------------------------------------------
--changeset ###author###:###table###-DDL-###version###-###jira###-###changesetid### runOnChange:true
--comment ###comment###
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check ###precondition###
---------------------------------------------------------------------------------------------------
'''
