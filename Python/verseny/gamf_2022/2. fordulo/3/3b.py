lista = []

egesz = 0
vegtelen = 0
veges = 0

for i in range(10_000):
    lista.append(int(input()))
    
    if lista[i] % 612 == 0:
        egesz += 1

    else:
        if lista[i] % (9 * 17) == 0:
            veges += 1

        elif lista[i] % (9 * 17) != 0:
            vegtelen += 1

print(egesz, "egész")
print(vegtelen, "végtelen")
print(veges, "véges (megoldás)")