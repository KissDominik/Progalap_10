#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6


sor = []
db = 0

for i in range(100):
    a = input().split()
    sor.append(a)


for i in range(len(sor)):
    
    y = int(sor[i][-1][0])
    x = int(sor[i][-1][1])

    l1 = str((y + 2)) + str((x - 1))
    l2 = str((y + 2)) + str((x + 1))
    l3 = str((y + 1)) + str((x - 2))
    l4 = str((y + 1)) + str((x + 2))
    l5 = str((y - 2)) + str((x - 1))
    l6 = str((y - 2)) + str((x + 1))
    l7 = str((y - 1)) + str((x - 2))
    l8 = str((y - 1)) + str((x + 2))

    if sor[i][0] == l1:
        db += 1
    if sor[i][0] == l2:
        db += 1
    if sor[i][0] == l3:
        db += 1
    if sor[i][0] == l4:
        db += 1
    if sor[i][0] == l5:
        db += 1
    if sor[i][0] == l6:
        db += 1
    if sor[i][0] == l7:
        db += 1
    if sor[i][0] == l8:
        db += 1
print(db)