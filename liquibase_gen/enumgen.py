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
    c, p = prep_enum("CHECK(ticket_payment_status IN ('PREPARED_FOR_PAYMENT,WAITING_FOR_PAYMENT,PAID,UNPAID,WAITING_FOR_CONFIRMATION,REFUNDED,CAPTURED'))")
    print(gen_enum(c, p))