def beolvas(a, n, i, e, k):
    fr = open("fuvar.txt", "r")
    sor = fr.readline().split()
    while sor != []:
        a.append(sor[0])
        n.append(sor[1])
        i.append(sor[2]*60 + sor[3])
        e.append(sor[4]*60 + sor[5])
        k.append(sor[6])
        sor = fr.readline().split()
    fr.close()
    
def main():
    auto = []
    nap = []
    indulas = []
    erkezes = []
    km = []
    beolvas(auto, nap, indulas, erkezes, km)
    print(auto)
    print(nap)
    print(indulas)
    print(erkezes)
    print(km)
main()