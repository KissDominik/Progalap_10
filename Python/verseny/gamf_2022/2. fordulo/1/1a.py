eredetiSzam = 10 
db = 0

while eredetiSzam != 101:
    prim = True
    prim_oszto = 2

    while prim_oszto<eredetiSzam and prim:
        if eredetiSzam % prim_oszto == 0:
            prim = False
        prim_oszto += 1

    if prim:
        szam = eredetiSzam
        szam = str(szam)
        szam_lista = []

        for szamjegy in szam:
            szam_lista.append(szamjegy)

        szam_lista = list(map(int, szam_lista))
        n = len(szam_lista)

        for j in range(n-1):
            if prim:
                szam_lista.pop(0)
                index = 0
                csonk_szam = 0

                for k in range(len(szam_lista), 0, -1):
                    csonk_szam += szam_lista[index] ** k 

                prim_oszto = 2

                while prim_oszto < csonk_szam and prim:
                    if csonk_szam % prim_oszto == 0:
                        prim = False
                    prim_oszto += 1

        if prim:
            db += 1

    eredetiSzam += 1

print(db)
