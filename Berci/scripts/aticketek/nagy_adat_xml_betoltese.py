def main(path, table):
    infile = path + f"{table} másolata.csv"
    outfile = path + f"{table}.csv"
    with open(infile, "r", encoding="utf-8") as in_file:
        out_file = open(outfile, "w", encoding="utf-8")
        s = 0
        for line in in_file:
            if s > 0:
                out_file.write(f'{str(s)},{line}')
            else:
                out_file.write(f'X__ID,{line}')
            s += 1


if __name__ == '__main__':
    path = "c:/GIT/AKP/data-backend-database-postgres-liquibase/liquibase/masterdata/tables/periodicity_factor_veh_grp_x_traf_time_prof_map/"
    main(path, 'periodicity_factor_veh_grp_x_traf_time_prof_map')
    #teszt()