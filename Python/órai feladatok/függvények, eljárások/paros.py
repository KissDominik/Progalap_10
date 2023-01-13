from random import *

def paros(x):
    i = 0
    while i < len(x) and not (x[i] % 2 == 0):
        i += 1

    if i < len(x):
        return True
    else:
        return False

szamok = [1, 3, 5, 13]
# for i in range(4):
#     szamok.append(randrange(1, 100))
print(szamok)
print(paros(szamok))