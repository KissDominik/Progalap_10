orarend = [
    "magyar",
    "tori",
    "programozas",
    "webprog",
    "tesi",

    "matek",
    "angol",
    "programozas",
    "programozas", 
    "magyar", 

    "webprog", 
    "adatbazis", 
    "angol", 
    "matek",
    "angol",

    "adatbazis",
    "programozas",
    "matek",
    "angol",
]

def egyediek_megszamolasa():
    targyak = []
    oraszamok = []
    targyak = set(targyak)
    oraszamok = [oraszamok.count(x) for x in oraszamok]
    print(targyak)
    print(oraszamok)

    # Egyediek megszamolasa (kivalogatas + eldontes + megszamolas)
    
def main():
    # print("Tárgyak:", orarend)

    # Hány óra van hetente a tantárgyakból?

    # Példa:
    # magyar: 2
    # tori: 1
    # programozas: 4
    # webprog: 2
    # ...

    egyediek_megszamolasa()

main()