n = int(input("n: "))
e = 0

for i in range(1000):
    if i % n == 0:
        print("osztható szám:", i, "n-edik szorzat:", i // n)