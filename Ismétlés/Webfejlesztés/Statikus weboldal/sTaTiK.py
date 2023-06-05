from random import *

def be(t, z, db):
    with open("tartalom.txt", "r") as fr:
        sor = fr.readline().strip().split(";")
        while sor != [""]:
            t.append(sor[0])
            z.append(int(sor[1]))
            db.append(sor[2])
            sor = fr.readline().strip().split(";")

def szelesseg() -> int:
    return randrange(50, 71, 2)

def szinek_generalasa() -> list:
    lista = []
    lista.append(randint(0, 255))
    lista.append(randint(0, 255))
    lista.append(randint(0, 255))
    lista.append(randint(0, 255))
    lista.append(randint(0, 255))
    return lista

def a(t, z):
    print(f"a) Tag-ek nevei:")
    for i in range(len(t)):
        if z[i] == 0:
            print(f"<{t[i]}>")
        else:
            print(f"<{t[i]}></{t[i]}>")

def b(t, db):
    for i in range(len(t)):
        if t[i] == "img":
            break
        
    print(f"b) KéPEk sZÁmA:{db[i]}")

def c(z):
    print(f"c) {z.count(0)} olYaN tAg vaN, aMinEK nINcS zÁRó tAg-Je")
    
def d(t):
    th = [len(x) for x in t]
    print(f"c) A lEgHosSzABb nEvŰ tAg: {t[th.index(max(th))]}")

def e(t):
    db = 0
    for i in range(len(t)):
        if "a" in t[i]:
            db += 1
            
    print(f'e) {db} fajta különböző tag nevében van "a" betű!')

def main():
    t = []
    z = []
    db = []
    be(t, z, db)
    
    w = szelesseg()
    print("1. fElaDaT:")
    print(f"wIdTh: {w}%\n")
    
    print("2. fElaDaT:")
    bg = szinek_generalasa()
    print(f"A vÁlaSzToTt kÉk sZíN: rgb(0, 0, {min(bg)})\n")
    
    print("3. fElaDaT:")
    a(t, z)
    b(t, db)
    c(z)
    d(t)
    e(t)
main()