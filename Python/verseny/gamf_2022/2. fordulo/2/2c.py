# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6

sor = []

for i in range(100):
    a = input().split()
    sor.append(a)

for i in range(len(sor)):

    jo = True

    sor[i] = [int(k) for k in sor[i]]
    d = [x for x in set(sor[i])]
    if len(d) < 36:
        jo = False

    for j in range(len(sor[i]) - 1):

        sor[i] = [str(k) for k in sor[i]]

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

        if sor[i][j + 1] != l1 and sor[i][j + 1] != l2 and sor[i][j + 1] != l3 and sor[i][j + 1] != l4 and sor[i][j + 1] != l5 and sor[i][j + 1] != l6 and sor[i][j + 1] != l7 and sor[i][j + 1] != l8:
            jo = False


    if jo == True:
        print(1, end="")
    else:
        print(0, end="")
        
# jó
1001010111010111010111011111010111110111111111111111111111111111111111111111111111111111111111111111
1001010111010111010111011111010111110111111111111111111111111111111111111111111111111111111111111111
