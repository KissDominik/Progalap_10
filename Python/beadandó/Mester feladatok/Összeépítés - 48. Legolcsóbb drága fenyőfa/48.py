aporte = input().split()
n = int(aporte[0])
k = int(aporte[1])
todos_los_abroles = []
los_abroles = []
indice = []
for i in range(n):
    aporte_dos = int(input())
    todos_los_abroles.append(aporte_dos)
    if aporte_dos > k:
        los_abroles.append(aporte_dos)
        indice.append(i)
minimo = los_abroles[0]
for i in range(1, len(los_abroles)):
    if minimo > los_abroles[i]:
        minimo = los_abroles[i]
for i in range(len(todos_los_abroles)):
        if todos_los_abroles[i] == minimo:
            indice_de_minimos = i
print(indice_de_minimos + 1, minimo)