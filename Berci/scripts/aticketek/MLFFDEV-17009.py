userlist = """I MADE KESUMA JAYA
I Nengah Suteja
I Ketut Sukerana
elyakim lie
SUARTHA GEDE
welly Tan
tri fendi rahayudi
M Rizki Ardiansyah 
agus handoko
matheus nurak
Ihsaan Nur Akbarudin Salaam
BEBUN
Bambang heriyanto
Priya Ardi Wibowo 
bayu dwi purnomo aji
Muhammad Khamim lutfy 
ariyanto
Herawati
babun samsul hadi
I Putu Gede Nesa Astawa
Ridhomuhammad
Tumpal Marojahan Siadari 
aan yosvanes sitompul 
andi setiawan
I Wayan Wirawan Jaya
abdul rohim andriawan
imade darsana
Soleman Ratu Emu
i putu muliana
Tengku Nazril 
Damianus lotu kopa
gede budiasa
Gasper Talan
i dewa gede Anom Arnata 
Robias Maitia
Dominukus Dara Dangga
Boyat
I GUSTI NGURAH AGUNG SIDIKARYA
Mario Fernando kotta 
Muhammad Akhbar 
Imam sodikin
Andri Wioko
I Ketut Sudiwiyasa
Anthoni haru nindir 
bahrul saifudin
Wy. M. Taufiq Akbar
mayumarisandi
I Wayan sandi wardana 
Antal Csaba
yohanan
Ody Anindyo 
Hutomo Rahadiant"""


def generate_select():
    users = [f"'{user}'" for user in userlist.split('/n')]
    print(f"select su.* from customer c /n"
          f"join customer_sec_user_relation cs /n"
          f"  on c.x__id = cs.customer_id/n"
          f"join security_user su/n"
          f"  on su.x__id = cs.security_user_id/n"
          f"where customer_name in /n"
          f"({','.join(users)});")


def generate_update(outfile):
    update = ''
    with open("C:/Users/bertalan.pasztor/Documents/MLFF/Tickets/MLFFDEV-17009/x__id_list_with_passwordhash.txt") as f:
        for row in f.read().split('\n'):
            if not row: continue
            arr = row.split(';')
            update += f"UPDATE security_user SET password = '{arr[1]}' WHERE x__id = '{arr[0]}';\n"
    with open(f"{outfile}", "w") as f:
        f.write(update)


if __name__ == '__main__':
    #generate_select()
    generate_update("C:/Users/bertalan.pasztor/Documents/MLFF/Tickets/MLFFDEV-17009/new_passwords_update.sql")
