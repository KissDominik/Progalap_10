def f(a, b):
    return a * b

eredmeny = f(2, 3)

print(eredmeny)

# a) 6
# b) 120
# c) TypeError
# d) 20


def f(x, y ,z):
    print()

parameterek = [1, 2, 3]
                                        
eredmeny = f(*parameterek)
print(eredmeny)
                                                    
# a) 6
# b) 5
# c) [1, 2, 3]
# d) TypeError