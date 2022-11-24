sor = "63 51 32 11 23 44 25 46 65 53 61 42 21 13 34 15 36 55 43 24 16 35 56 64 52 31 12 33 14 26 45 66 54 62 41 22"

sor = sor.split()

for i in range(len(sor) - 1):
    y = int(sor[i][0])
    x = int(sor[i][1])

    l1 = str((y + 2)) + str((x - 1))
    l2 = str((y + 2)) + str((x + 1))
    l3 = str((y + 1)) + str((x - 2))
    l4 = str((y + 1)) + str((x + 2))
    l5 = str((y - 2)) + str((x - 1))
    l6 = str((y - 2)) + str((x + 1))
    l7 = str((y - 1)) + str((x - 2))
    l8 = str((y - 1)) + str((x + 2))

    if sor[i + 1] == l1 or sor[i + 1] == l2 or sor[i + 1] == l3 or sor[i + 1] == l4 or sor[i + 1] == l5 or sor[i + 1] == l6 or sor[i + 1] == l7 or sor[i + 1] == l8:
        print("jó")
    else:
        print("rossz")