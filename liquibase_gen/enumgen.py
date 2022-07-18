import re


def gen_enum(colname, values):
    valuelist = values.split(',')
    f1 = "CONSTRAINT ck_ CHECK (((" + colname + ")::text = ANY ((ARRAY["
    l = []
    for v in valuelist:
        l.append("'" + v + "'::character varying")
    f2 = ', '.join(l)
    f3 = '])::text[])))'
    del_command = 'DELETE FROM _ WHERE ' + colname + " NOT IN('" + "', '".join(valuelist) + "');"
    return del_command+'\n' + f1 + f2 + f3


def prep_enum(p):
    colname = re.match('CHECK\\((.*) IN ', p).group(1).lower()
    values = re.match('.* IN \\((.*)\\)\\)', p).group(1).replace("'",'').replace(' ','')
    return colname, values


if __name__ == '__main__':
    c, p = prep_enum("CHECK(event_name IN ('REGISTRATION','PHONE_NUMBER_MODIFICATION','AD_HOC_TICKET_PAYMENT_SUCCESS','AD_HOC_TICKET_PAYMENT_FAILED','TICKET_PAYMENT_SUCCES','TICKET_PAYMENT_FAILED','TRIP_PAYMENT_FAILED','TRIP_PAYMENT_SUCCESS','APPROACH_TOLL_ROAD_SEG','ENTER_CLOSED_SEG','EXIT_CLOSED_SEG','EXIT_OPEN_SEG))")
    print(gen_enum(c, p))