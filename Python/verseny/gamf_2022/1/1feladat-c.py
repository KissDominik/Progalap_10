szamok = input()
db = 0
hasznalt = []

for i in range(len(szamok)-3):
    szam = int(szamok[i:i+4])
    j = 2
    prim = True
    if not szam in hasznalt:
        while j < szam and prim:
            if szam % j == 0:
                prim = False
            j += 1

        if prim:
            db += 1
            hasznalt.append(szam)

print(db)


