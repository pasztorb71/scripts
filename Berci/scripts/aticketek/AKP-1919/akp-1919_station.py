import random
from datetime import datetime


def main():
    global path
    path = "C:\\GIT\\AKP\\data-backend-database-postgres-liquibase\\liquibase\\masterdata\\tables\\station\\"
    infile = path + "station másolata.csv"
    outfile = path + "station.csv"
    with open(infile, "r", encoding="utf-8") as in_file:
        out_file = open(outfile, "w", encoding="utf-8")
        s = 0
        for line in in_file:
            if s > 0:
                out_file.write(f'{str(s)},{line}')
            else:
                out_file.write(f'X__ID,{line}')
            s += 1

def rollback():
    global path
    path = "C:\\GIT\\AKP\\data-backend-database-postgres-liquibase\\liquibase\\masterdata\\tables\\station\\"
    infile = path + "station másolata.csv"
    outfile = path + "station.csv"
    with open(infile, "r", encoding="utf-8") as in_file:
        out_file = open(outfile, "w", encoding="utf-8")
        for line in in_file:
            l = line.split(',',1)[1]
            out_file.write(l)

def write_generated_id():
    global path
    path = "C:\\GIT\\AKP\\data-backend-database-postgres-liquibase\\liquibase\\masterdata\\tables\\station\\"
    infile = path + "station másolata.csv"
    outfile = path + "station.csv"
    with open(infile, "r", encoding="utf-8") as in_file:
        out_file = open(outfile, "w", encoding="utf-8")
        s = 0
        for line in in_file:
            l = line.split(',',1)[1]
            if s > 0:
                out_file.write(f'{generateid()},{l}')
            else:
                out_file.write(f'X__ID,{l}')
            s += 1


def generateid():
    # Generate a random 20-digit integer for more uniqueness
    rndint = random.randint(10**19, 10**20 - 1)
    szam = rndint
    szam_konv = ''
    while szam > 0:
        szamjegy = szam % 35
        if 0 <= szamjegy <= 9:
            szam_konv = chr(48 + szamjegy) + szam_konv
        elif 10 <= szamjegy <= 34:
            szam_konv = chr(65 + szamjegy - 10) + szam_konv
        szam = szam // 35
    return szam_konv


def teszt():
    import csv
    path = "C:\\GIT\\AKP\\data-backend-database-postgres-liquibase\\liquibase\\masterdata\\tables\\station\\"
    infile = path + "station.csv"
    with open(infile, mode='r', encoding='utf8') as file:
        csvFile = csv.reader(file)
        c = 1
        for l in csvFile:
            len1 = len(l)
            print(len1)
            #if len1 != 62:
            #    print(f'HIBA: {len1} - {l}')
            c += 1
            if c > 15:
                break


if __name__ == '__main__':
    #main()
    #rollback()
    write_generated_id()
    #teszt()