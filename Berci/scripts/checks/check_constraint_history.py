import collections
import os
import re
from dataclasses import dataclass

from tabulate import tabulate


def get_con_data(l):
    pass


def is_check_constraint(l):
    return re.match('.*ADD CONSTRAINT (.*) CHECK (.*)', l) is not None


def get_cons_from_filecontent(lines):
    l_cons = []
    l_except = []
    for l in lines:
        if is_check_constraint(l):
            if is_enum(l):
                l_cons.append(get_cons_data(l))
    return l_cons


def get_cons_data(l):
    enums = ()
    m = re.match('.*ADD CONSTRAINT (.*) CHECK (.*)', l)
    enums = re.findall("'(\w+)'", l)
    return [m.group(1), m.group(2), '', enums]


def is_enum(l):
    if 'ck_template_category' in l:
        return True
    return False
    if any([x in l for x in ['ck_customer_nik_number','ck_customer_phone_number']]):
        return False
    return True


@dataclass
class Constraint:
    name: str
    file: str
    enums: list[str]


def get_version(fname):
    m = re.match('.*-[0-9].([0-9]{2}).[0-9].*', fname)
    if m:
        return m.group(1)
    return ''

#TODO megcsinálni
if __name__ == '__main__':
    d_constraints = {}
    l_constraints = []
    l_consclass = []

    base = 'c:\\tmp\\check_constraints'
    files = os.listdir(base)
    for file in files[0:]:
        with open(f"{base}/{file}", 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
            l_consclass.append(Constraint)
            res = get_cons_from_filecontent(lines)
            l_constraints += [[get_version(file), file, x[0], x[3], x[1]] for x in res]
            #l_constraints += l_cons
            #d_constraints[file] = l_cons
    #a = [item for item, count in collections.Counter(l_constraints).items() if count > 1]
    #a.sort()
    l1 = sorted(l_constraints, key=lambda x: (int(x[0]), x[2]))
    print(tabulate(l1))
    print(len(l_constraints))
    #print(d_constraints)