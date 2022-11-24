sor = []

# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6


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

        # k = ["1", "2", "3", "4", "5", "6"]
        # ls1 = [l1[0], l2[0], l3[0], l4[0], l5[0], l6[0]]
        # ls2 = [l1[1], l2[1], l3[1], l4[1], l5[1], l6[1]]

        # print(ls1, ls2)

        if sor[i][j + 1] == l1 or sor[i][j + 1] == l2 or sor[i][j + 1] == l3 or sor[i][j + 1] == l4 or sor[i][j + 1] == l5 or sor[i][j + 1] == l6 or sor[i][j + 1] == l7 or sor[i][j + 1] == l8:
            jo = True
        else:
            jo = False
    if jo == True:
        print(1, end="")
    else:
        print(0, end="")
        

1001010111010111_0_1011101111101_0_111110111111111111111111111111111111111111111111111111111111111111111
1001010111010111_1_1011101111101_1_111110111111111111111111111111111111111111111111111111111111111111111