import re


def gen_enum(colname, values):
    valuelist = values.split(',')
    f1 = "CONSTRAINT ck_ CHECK (((" + colname + ")::text = ANY ((ARRAY["
    l = []
    for v in valuelist:
        l.append("'" + v + "'::character varying")
    f2 = ', '.join(l)
    f3 = '])::text[])))'
    return f1 + f2 + f3


def prep_enum(p):
    colname = re.match('CHECK\\((.*) IN ', p).group(1).lower()
    values = re.match('.* IN \\((.*)\\)\\)', p).group(1).replace("'",'').replace(' ','')
    return colname, values


if __name__ == '__main__':
    c, p = prep_enum("CHECK(channel IN ('WHATSAPP', 'PUSH_NOTIFICATION','EMAIL'))")
    print(gen_enum(c, p))