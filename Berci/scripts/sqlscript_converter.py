import re


def write_head(outf, table='INIT'):
    outf.write(f"""--liquibase formatted sql

--===============================================================================================--
-- DML ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:{table}-DML runOnChange:true failOnError:true stripComments:true
--comment A táblák feltöltése induló értékekkel.. 
---------------------------------------------------------------------------------------------------
SET search_path = ${{schema_name}};

SET CONSTRAINTS ALL DEFERRED;

""")


def write_end(outf):
    outf.write("""  
    
-- -- --
COMMIT;
-- -- --

SET CONSTRAINTS ALL IMMEDIATE;
""")


if __name__ == '__main__':
    path = 'c:/Users/bertalan.pasztor/Downloads/'
    file = 'fill_tables.sql'
    outfile = 'c:/GIT/MLFF/mlff-core-template-postgredb/liquibase/core_template/template/dmls/template-DML.sql'

    outf = open(outfile, 'w', encoding='utf8')
    write_head(outf, 'TEMPLATE')
    with open(path+file, 'r', encoding='utf8') as f:
        for line in f.readlines():
            if line.startswith("('change20221014',") or line.startswith("INSERT INTO tariff_change "):
                outf.write(line)
                continue
            if 'x__insdate,' in line:
                line = line.replace('x__insdate,', '')
            else:
                if re.match('.*\(.*\).*', line):
                    arr = line.split(',')
                    del arr[1]
                    arr[3] = arr[4] = 'null'
                    line = ','.join(arr)
            if ';TRUNCATE TABLE' in line:
                line = line.replace(';TRUNCATE TABLE', ';/nTRUNCATE TABLE')
            outf.write(line)
    write_end(outf)
    outf.close()