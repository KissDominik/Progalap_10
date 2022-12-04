from random import *
lista = []

for i in range(10):
    lista.append(randint(0, 100))
print(lista)

# rendezd növekvő sorrendbe az [a] lista elemeit

i = 0

while i < len(lista) - 1:
    if lista[i] > lista[i + 1]:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
        i = 0
    else:
        i += 1

print(lista)
print(lista[0], "minimum")
print(lista[-1], "maximum")