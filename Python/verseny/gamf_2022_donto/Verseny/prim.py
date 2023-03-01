from math import *

def T(x):
    szam = factorial(x-1)
    print(szam)
    szam += 1
    print(szam)
    szam /= x
    print(szam)
    szam *= pi
    print(szam)
    szam = cos(szam)
    print(szam)
    szam = szam**2
    print(szam)
    szam = floor(szam)
    print(szam)
    print()
    return szam

def primek(eddig):
    db = 0
    for i in range(1, eddig+1):
        print(i)
        if T(i) == 1:
            db += 1
    return db

def main():
    n = int(input("prímek n-ig:"))
    print(primek(n))
    
main()