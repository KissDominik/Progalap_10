from codecs import namereplace_errors


n = int(input("n: "))
i = 2
prim = True

while i < n and prim:
    if n % i == 0:
        prim = False
    i += 1

if prim:
    print("primszam")
else:
    print("nem prim")