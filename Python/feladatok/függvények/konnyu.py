def f(x):
    x += 1
    return x

a = 0
b = f(a)
print(a, b)
                                                            
# a) 0 0
# b) 0 1
# c) 1 0
# d) 1 1
# e) SyntaxError