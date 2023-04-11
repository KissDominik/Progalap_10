def f(x:list):
    lista = []
    for i in range(len(x-1)):
        if x[i] % 2 == 0:
            lista.append(lista[i])
    return lista.copy()
                                                
# a) Keresés tétel
# b) Szétválogatás tétel
# d) Error
# c) Kiválogatás tétel