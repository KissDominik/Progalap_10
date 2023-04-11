lista = [["1", 6, 3], [2, 1, "0"], [-2, "-2", "-1"]]    

a = lista[lista[0][-1]-1][0]
b = lista[lista[a][lista[a][a]]][a]-1

print(lista[b][a])
                                                    
# a) 1
# b) 6
# c) "-1"
# d) "0"
# e) IndexError
# f) 3