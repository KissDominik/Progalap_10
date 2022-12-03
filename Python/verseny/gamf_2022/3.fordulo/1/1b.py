szavak = []
vegzodes = ["VAL", "VEL"]

for i in range(1239):
    sor = input().split()
    for j in sor:
        if j[len(j)-3:] in vegzodes and len(j) > 3:
            szavak.append(j)

            
szavak = [x for x in set(szavak)]

print(szavak)
print(len(szavak))