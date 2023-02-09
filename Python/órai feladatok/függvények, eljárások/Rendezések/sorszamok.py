from random import randint

def feltolt(n):
    x = []
    for i in range(n):
        r = randint(50, 100)
        x.append(r)
    return x

def bubi(x, szamok):
    for i in range(len(x)-1, 0, -1):
        for j in range(i):
            if x[j] < x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                szamok[j], szamok[j+1] = szamok[j+1], szamok[j]

def main():
    x = feltolt(20)
    sorsz = list(range(1, 21))
    
    print("Rendezes elott:")
    print(sorsz)
    print(x)
    
    # rendez(x, sorsz)
    print("Rendezes utan:")
    print(sorsz)
    print(x)
    bubi(x, sorsz)
    print(sorsz)
    print(x)

main()