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
        i.append(sor)
        sor = fr.readline().strip()
        m.append(sor)
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
    for i in range((len(d))):
        if d[i] <= datum and m[i] == 0:
            print(e[i], "\t", c[i])

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
    # print(datum)
main()