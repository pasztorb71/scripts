from utils.generate_id import generateid

path = "C:\\GIT\\EMAP\\emap-org-liquibase\\liquibase\\emap_registry\\tables\\postal_code\\"

def postal_code():
    global path
    infile = path + "NYILVANTARTAS_TORZSADATOK_0903.xlsx - POSTAL_CODE.csv"
    outfile = path + "postal_code.csv"
    with open(infile, "r", encoding="utf-8") as in_file:
        out_file = open(outfile, "w", encoding="utf-8")
        s = 0
        out_file.write('INSERT INTO postal_code (X__ID, POSTAL_CODE, CITY, DISTRICT, VALIDITY_START,VALIDITY_END) VALUES\n')
        for line in in_file:
            if s > 0:
                line1 = line.replace('\n','')
                line2 = line1.split(',')
                line2[1] = f"'{line2[1]}'"
                line2[2] = line2[2] if line2[2] != '' else 'null'
                line = ','.join(line2)
                out_file.write(f"('{generateid()}',{line}CURRENT_DATE,'9999-12-31')," + '\n')
            s += 1

def public_place_category():
    global path
    infile = path + "NYILVANTARTAS_TORZSADATOK_0903.xlsx - PUBLIC_PLACE_CATEGORY.csv"
    outfile = path + "public_place_category.csv"
    with open(infile, "r", encoding="utf-8") as in_file:
        out_file = open(outfile, "w", encoding="utf-8")
        s = 0
        out_file.write('INSERT INTO public_place_category (X__ID, PUBLIC_PLACE_CATEGORY, VALIDITY_START,VALIDITY_END) VALUES\n')
        for line in in_file:
            if s > 0:
                line = line.replace('\n','')
                out_file.write(f"('{generateid()}','{line}',CURRENT_DATE,'9999-12-31')," + '\n')
            s += 1


if __name__ == '__main__':
    #postal_code()
    public_place_category()