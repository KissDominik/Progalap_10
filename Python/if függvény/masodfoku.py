a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b ** 2 - 4 * a * c

if D < 0:
    print("nincs megoldás")
elif D == 0:
    print("egy megoldás")
else:
    print("kettő megoldás")