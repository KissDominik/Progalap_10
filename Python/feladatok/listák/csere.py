lista = [1, 2, 3, 4, 5]
for i in range(5):
    lista.append(lista.pop())
    
print(lista)

# a) [1, 2, 3, 4, 5]
# c) Error
# b) [5, 4, 3, 2, 1]
# d) IndexError
# d) []