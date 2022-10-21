n = int(input("n: "))
sor = 1

for i in range(1, n+1):
    for j in range(sor, i):
        sor += 1
        print(i, end=" ")
    print()