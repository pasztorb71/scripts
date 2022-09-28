import re


def gen_enum(tabname, colname, values):
    valuelist = values.split(',')
    f1 = "ALTER TABLE " + tabname + " ADD " if tabname else ''
    f1 += f"CONSTRAINT ck_{tabname.split('.')[1]}_{colname} CHECK (((" + colname + ")::text = ANY ((ARRAY["
    l = []
    for v in valuelist:
        l.append("'" + v + "'::character varying")
    f2 = ', '.join(l)
    f3 = '])::text[]))),'
    del_command = 'DELETE FROM ' + tabname + ' WHERE ' + colname + " NOT IN('" + "', '".join(valuelist) + "');"
    return del_command+'\n' + f1 + f2 + f3


def prep_enum( p):
    colname = re.match('CHECK\\((.*) IN ', p).group(1).lower()
    values = re.match('.* IN \\((.*)\\)\\)', p).group(1).replace("'",'').replace(' ','')
    return colname, values


if __name__ == '__main__':
    table = 'invoice.invoice'
    c, p = prep_enum("CHECK(invoice_state IN ('EN,ID'))")
    print(gen_enum(table, c, p))
