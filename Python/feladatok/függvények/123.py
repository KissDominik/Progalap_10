def f(x, y = 4, z = 6):
    print(x, y, z)
    
lista = [1, 2, 3]

f(2, lista[lista[0]])
                                                    
# a) 1 2 3
# b) 2 4 6
# c) Error
# d) 2 2 6
# e) 2 1 6