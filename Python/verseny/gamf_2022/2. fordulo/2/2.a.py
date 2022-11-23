sor = []
b = 0

for i in range(100):
    a = input().split()
    sor.append(a)

for i in range(len(sor)):
    for j in range(len(sor[i])):
        b += 1
        if sor[i][j] == 33 or sor[i][j] == 34 or sor[i][j] == 43 or sor[i][j] == 44: # valószínűleg ez a probléma
            print(sor[i])
print(b) # (b) darab elemen megy végig