from math import *

oldal = 1
összeg = 0

for i in range(10):
    terület = oldal * oldal
    összeg += terület
    kotes = sqrt(((oldal/2) ** 2) * 2)
    oldal = kotes
print(összeg)