def f(x):
    if x == 1:
        return 1
    else:
        return x * f(x-1)

print(f(4))

# a) 12
# b) 24
# c) 36
# d) 48
    
    
    
def f(x):
    if x == 1:
        return 1
    else:
        return x + f(x-1)
    
print(f(4))
                                                    
# a) 10 
# b) 24
# c) SyntaxError
# d) 16