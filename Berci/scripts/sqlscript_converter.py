import re


def write_head(outf, table='INIT'):
    outf.write(f"""--liquibase formatted sql

--===============================================================================================--
-- DML_tariff ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:{table}-DML_tariff runOnChange:true failOnError:true stripComments:true
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
    outfile = 'c:/GIT/MLFF/mlff-core-template-postgredb/liquibase/core_template/template/dmls/template-DML_tariff.sql'

    outf = open(outfile, 'w', encoding='utf8')
    write_head(outf, 'TEMPLATE')
    with open(path+file, 'r', encoding='utf8') as f:
        for line in f.readlines():
            if line.startswith("('change20221014',") or line.startswith("INSERT INTO tariff_change "):
                outf.write(line)
                continue
            if 'x__insdate,' in line:
                line = line.replace('x__insdate, ', '').replace('x__moddate, ','').replace('x__moduser, ','').replace('x__version, ','')
            else:
                if re.match('.*\(.*\).*', line) or re.match('.*VALUES\(.*', line):
                    arr = line.split(',')
                    del arr[1]
                    del arr[2:5]
                    line = ','.join(arr)
            if ';TRUNCATE TABLE' in line:
                line = line.replace(';TRUNCATE TABLE', ';/nTRUNCATE TABLE')
            outf.write(line)
    write_end(outf)
    outf.close()