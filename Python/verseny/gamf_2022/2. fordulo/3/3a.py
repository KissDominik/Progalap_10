l = []

for i in range(10_000):
    a = int(input())
    if a % 317 == 0:
        l.append(a)

print(len(l))