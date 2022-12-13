aporte = input().split()
n = int(aporte[0])
k = int(aporte[1])
todos_los_ábroles = []
los_ábroles = []
índice = []

for i in range(n):
    aporte_dos = int(input())
    todos_los_ábroles.append(aporte_dos)
    if aporte_dos > k:
        los_ábroles.append(aporte_dos)
        índice.append(i)


mínimo = los_ábroles[0]
for i in range(1, len(los_ábroles)):
    if mínimo > los_ábroles[i]:
        mínimo = los_ábroles[i]
for i in range(len(todos_los_ábroles)):
        if todos_los_ábroles[i] == mínimo:
            índice_de_mínimos = i

print(índice_de_mínimos + 1, mínimo)