lista1 = [1, 2, 3]
lista2 = lista1
lista3 = lista1.copy()

lista1[0] = 0
print(lista1, lista2, lista3)
                                                    
# a) [0, 2, 3], [0, 2, 3], [0, 2, 3]
# b) [0, 2, 3], [0, 2, 3], [1, 2, 3]
# c) [0, 2, 3], [0, 2, 3], [1, 2, 3, 0]
# d) [0, 2, 3], [0, 2, 3], [0, 2, 3]
# e) [1, 2, 3], [1, 2, 3], [0, 2, 3]