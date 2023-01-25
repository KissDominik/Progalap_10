from random import *

def kiválogatás(l:list, k:int):
    lista = []
    for i in range(len(l)):
        if T(l[i]):
            lista.append(i+1)
     return lista

def T(a):
    return a > k

szamok = []
for i in range(12):
    szamok.append(randrange(30))
print(szamok)

k = int(input("k: "))

print(kiválogatás(szamok, k))