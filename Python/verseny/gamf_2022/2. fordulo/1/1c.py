eredetiSzam = 10000 
db = 0

while eredetiSzam != 100000:
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

        print(f"{eredetiSzam}: ", end="")

        for szamjegy in szam:
            szam_lista.append(szamjegy)

        szam_lista = list(map(int, szam_lista))
        n = len(szam_lista)

        for j in range(n):
            prim = True
            prim_oszto = 2
            szamjegy = szam_lista[j]

            if szamjegy != 1:
                while prim_oszto<szamjegy and prim:
                    if szamjegy % prim_oszto == 0:
                        prim = False
                    prim_oszto += 1
            else:
                prim = False

            if prim:
                print(szamjegy, end="")
                db += 1

        print()
          

    eredetiSzam += 1

print(db)