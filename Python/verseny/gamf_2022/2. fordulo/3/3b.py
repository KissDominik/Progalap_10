l = []
db = 0

for i in range(10_000):
    a = int(input())
    l.append(a)

for i in range(len(l)):
    s1 = l[i] / 612
    s2 = s1 * 612
    if l[i] == s2:
        db += 1
print(db)