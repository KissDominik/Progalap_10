def feladat1(d:list, c:list, e:list, i:list, m:list):
    fr = open("lista.txt", "r")
    sor = fr.readline().strip()
    while sor != "":
        d.append(sor)
        sor = fr.readline().strip()
        c.append(sor)
        sor = fr.readline().strip()
        e.append(sor)
        sor = fr.readline().strip()
        i.append(int(sor))
        sor = fr.readline().strip()
        m.append(int(sor))
        sor = fr.readline().strip()
    fr.close()



def feladat2(datum:list):
    print(len(datum))



def feladat3(m:list):
    print("A listában lévő epizódok ", round(m.count(1) / len(m) *100, 2), "%-át látta.", sep="")


def feladat4(i:list, m:list):
    ido = 0
    for j in range(len(i)):
        if m[j] == 1:
            ido += i[j]
    nap = ido // (60 * 24)
    ora = ido % (60 * 24) // 60
    perc = ido % (60 * 24) % 60
    print("Sorozatnézéssel ", nap, " napot ", ora, " órát és ", perc, " percet töltött", sep="")


def feladat5(d, e, c, m):
    datum = input("dátum (év.hónap.nap): ")
    for i in range(len(d)):
            if d[i] <= datum and m[i] == 0:
                print(e[i] + "\t" + c[i])


def feladat6(ev, ho, nap:int):
    napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]
    return hetnapja


def feladat7(nap:str, d:list, c:list):
    for i in range(len(d)):
        datum = d[i].split(".")
        nap2 = feladat6(int(datum[0]), int(datum[1]), int(datum[2]))
        if nap == nap2:
            print(c[i])


def main():
    datum = []
    cim = []
    evad_resz = []
    ido = []
    megnezte = []
    feladat1(datum, cim, evad_resz, ido, megnezte)
    feladat2(datum)
    feladat3(megnezte)
    feladat4(ido, megnezte)
    feladat5(datum, evad_resz, cim, megnezte)
    feladat7(input("Adja meg a hét egy napját!").strip(), datum, cim)
main()