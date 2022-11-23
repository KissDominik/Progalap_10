sor = []
c = []
b = 0

for i in range(100):
    a = input().split()
    sor.append(a)

for i in range(len(sor)):
    for j in range(len(sor[:10])):
        if sor[i][j] == "33" or sor[i][j] == "34" or sor[i][j] == "43" or sor[i][j] == "44":
            c.append(i+1)

d = [x for x in set(c)]
print(len(d))