# Egy lépcsőnek "n" darab lépcsőfoka van.
# Kétféleképpen tudunk felfelé lépni: 1 vagy 2 lépcsőfokot haladunk egyszerre.
# Hányféleképpen juthatunk a lépcső tetejére?

# Példák:
# lepcso(1) == 1
# lepcso(2) == 2, mert 2 = 1+1
# lepcso(3) == 3, mert 2+1 = 1+2 = 1+1+1
# lepcso(4) == 5, mert 2+2 = 2+1+1 = 1+2+1 = 1+1+2 = 1+1+1+1
# ...
# lepcso(7) == 21
# lepcso(13) == 377
# lepcso(20) == 10946
# lepcso(30) == 1346269

# Készíts lepcso(n) néven függvényt, amely visszatérési értéke,
# hogy egy "n" magas lépcsőt hányféleképpen lehet megmászni.

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
 
def lepcso(x):
    return fib(x + 1)


def main():
    print(lepcso(7))

main()