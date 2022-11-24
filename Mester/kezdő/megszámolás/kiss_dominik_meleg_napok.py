a = input().split()
a = list(map(int, a))
db = 0

for i in range(a[0]):
    n = int(input())
    if n > a[1]:
        db += 1
print(db)

# egyszer bekérsz egy inputot amit space-el elválasztva adnak meg (pl: 3 40 vagy 45 6)
# tegyük fel az előbbi input '9 27'
# akkor kell bekérned 9 számot (input ciklusban), ami a hőmérsékletet jelzi
# ha a megadott szám nagyobb mint 27, akkor lesz a végeredményed eggyel nagyobb
# ha 9-ből 6 szám nagyobb mint 27, akkor 6 az eredmény