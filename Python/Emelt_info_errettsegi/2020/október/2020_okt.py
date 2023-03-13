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


def feladat4(i:list):
    print(i)
    ido = sum(i)
    perc = ido % 60
    ora = ido // 60
    nap =  // 
    print("Sorozatnézéssel ", nap, " napot ", ora, " órát és ", perc, " percet töltött", sep="")


def main():
    datum = []
    cim = []
    evad_resz = []
    ido = []
    megnezte = []
    feladat1(datum, cim, evad_resz, ido, megnezte)
    feladat2(datum)
    feladat3(megnezte)
    feladat4(ido)
main()