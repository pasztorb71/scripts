import psycopg2

import utils_sec
from utils import get_port

if __name__ == '__main__':
    port = get_port('dev')
    database = 'eobu_tariff'
    conn1 = psycopg2.connect(f"host=localhost port={port} dbname={database} "
                             f"user=postgres password={utils_sec.password_from_file('postgres', 'localhost', port)}")
    cur1 = conn1.cursor()

    port = get_port('new_test')
    database = 'eobu_tariff'
    conn2 = psycopg2.connect(f"host=localhost port={port} dbname={database} "
                             f"user=postgres password={utils_sec.password_from_file('postgres', 'localhost', port)}")
    cur2 = conn1.cursor()

    #Query the table structure from both databases
    cur1.execute("SELECT table_name, column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_schema = 'public'")
    tables1 = cur1.fetchall()
    cur2.execute("SELECT table_name, column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_schema = 'public'")
    tables2 = cur2.fetchall()

    #Compare the table structure between the two databases
    if len(tables1) != len(tables2):
    print("Number of tables does not match between the two databases")
    else:
    for i in range(len(tables1)):
    if tables1[i] != tables2[i]:
    print("Table structure does not match for table {}".format(tables1[i][0]))

    #Query the function structure from both databases
    cur1.execute("SELECT routine_name, parameter_name, data_type, character_maximum_length FROM information_schema.parameters WHERE specific_schema = 'public' AND routine_type = 'FUNCTION'")
    functions1 = cur1.fetchall()
    cur2.execute("SELECT routine_name, parameter_name, data_type, character_maximum_length FROM information_schema.parameters WHERE specific_schema = 'public' AND routine_type = 'FUNCTION'")
    functions2 = cur2.fetchall()

    #Compare the function structure between the two databases
    if len(functions1) != len(functions2):
    print("Number of functions does not match between the two databases")
    else:
    for i in range(len(functions1)):
    if functions1[i] != functions2[i]:
    print("Function structure does not match for function {}".format(functions1[i][0]))

    #Close the cursors and connections
    cur1.close()
    cur2.close()
    conn1.close()
    conn2.close()