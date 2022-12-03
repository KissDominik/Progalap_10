szavak = []
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(1239):
    sor = input().split()
    for j in range(len(sor)):
        for k in range(len(sor[j])):
            szo = True
            if sor[j][k] in abc:
                szo = False
        if szo:
            szavak.append(sor[j])

szavak = [x for x in set(szavak)]

hosszak = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
szavak2 = []

for i in range(len(szavak)):
    if len(szavak[i]) in hosszak:
        szavak2.append(szavak[i])

print(len(szavak))
print(len(szavak2))