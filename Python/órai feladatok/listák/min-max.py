from random import *

lista = []

for i in range(10):
    lista.append(randint(1, 100))
print(lista)

minimum = lista[0]
maximum = lista[0]
for i in range(len(lista)):
    if lista[i] < minimum:
        minimum = lista[i]
    if lista[i] > maximum:
        maximum = lista[i]
print(minimum, maximum)
        