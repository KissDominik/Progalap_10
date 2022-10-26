m = int(input("n: "))
j = 2

while j <= m:
    n = j
    i = 2
    prim = True

    while i < n and prim:
        if n % i == 0:
            prim = False
            print(i)
        i += 1

    if prim:
        print(j, end=" ")
    else:
        print(j, end=" ")

    i += 1