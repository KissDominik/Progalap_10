def feladat1(d:list, c:list, e:list, i:list, m:list):
    fr = open("lista.txt", "r")
    sor = fr.readline().strip().split(".")
    while sor != [""]:
        d.append(sor)
        sor = fr.readline().strip()
        c.append(sor)
        sor = fr.readline().strip()
        e.append(sor)
        sor = fr.readline().strip()
        i.append(int(sor))
        sor = fr.readline().strip()
        m.append(int(sor))
        sor = fr.readline().strip().split(".")
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


# def feladat5(d, e, m):
    # datum = input("dátum (év, hónap, nap): ")



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
    # feladat5(datum, evad_resz, megnezte)
    print(datum)
main()