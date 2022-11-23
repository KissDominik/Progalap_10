sor = []

for i in range(100):
    a = input().split()
    sor.append(a)

for i in range(len(sor)):
    jo = True
    for j in range(len(sor[i]) - 1):

        y = int(sor[i][j][0])
        x = int(sor[i][j][1])

        l1 = str((y + 2)) + str((x - 1))
        l2 = str((y + 2)) + str((x + 1))
        l3 = str((y + 1)) + str((x - 2))
        l4 = str((y + 1)) + str((x + 2))
        l5 = str((y - 2)) + str((x - 1))
        l6 = str((y - 2)) + str((x + 1))
        l7 = str((y - 1)) + str((x - 2))
        l8 = str((y - 1)) + str((x + 2))

        if sor[i][j + 1] == l1 or sor[i][j + 1] == l2 or sor[i][j + 1] == l3 or sor[i][j + 1] == l4 or sor[i][j + 1] == l5 or sor[i][j + 1] == l6 or sor[i][j + 1] == l7 or sor[i][j + 1] == l8:
            jo = True
        else:
            jo = False
    if jo == True:
        print(1, end="")
    else:
        print(0, end="")