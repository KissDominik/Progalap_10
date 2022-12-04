n = int(input("n: "))

for s in range(1, n+1):
    for i in range(1, n+1):
        print(i * s, end=" ")
    print()