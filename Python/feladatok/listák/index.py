lista = [1, 2, 3, 4, 5, 6]
for i in range(len(lista)):
    if lista[i] == 3:
        lista.pop(i)
print(lista)
                                                
# a) [1, 2, 4, 5]
# b) [1, 2, 4, 6]
# c) [1, 2]
# d) IndexError
# e) [3, 6]