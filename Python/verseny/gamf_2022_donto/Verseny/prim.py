from math import *

def feltetel(x):
    szam = factorial(x-1)
    szam += 1
    szam /= x
    return szam.is_intiger()

def primek(eddig):
    db = 0
    for i in range(1, eddig):
        if feltetel(i):
            db += 1
    return db

def main():
    n = int(input("prímek n-ig:"))
    print(primek(n))
    
main()

# n = int(input("prímek n-ig:"))
# db = 0
# for j in range(2, n):
#     print(j, end=" ")
#     feltetel = ((factorial(j-1) + 1) / j).is_integer()
#     if feltetel:
#         db += 1
# print(db)