from random import randint

def feltolt(n):
    x = []
    for i in range(n):
        r = randint(150, 190)
        x.append(r)
    return x

def kiir(m, n):
    for i in range(len(m)):
        print(n[i], ": ", m[i], sep = "")

def rendez(lista1, lista2):
    for i in range(len(lista1)-1, 0, -1):
        for j in range(i):
            if lista1[j] < lista1[j+1]:
                lista1[j], lista1[j+1] = lista1[j+1], lista1[j]
                lista2[j], lista2[j+1] = lista2[j+1], lista2[j]

def main():
    nevek = ["Adam", "Bela", "Csaba", "Denes", "Erik", "Feri", "Gergo", "Hedvig", "Imre", "Jani", "Karoly"]
    magassagok = feltolt(11)

    print("Rendezes elott:")
    kiir(magassagok, nevek)

    rendez(magassagok, nevek)
    print("\nRendezes utan:")
    # rendez(magassagok, nevek)
    kiir(magassagok, nevek)

    print("\nKozepen:")
    if len(nevek) % 2 != 0:
        print(nevek[int(len(nevek)/2)])
    else:
        print(nevek[int(len(nevek)/2)], nevek[int(len(nevek)/2)]+1)

main()