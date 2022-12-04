n = int(input("n: "))
a = 0
b = 0

for i in range(n+1):
    if i % 2 != 0:
        print(i * "a")
    else:
        print(i * "b")