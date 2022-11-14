from math import *

n = int(input())
adat = n

while adat > 0:
    k = int(sqrt(adat))
    print(k, end=" ")
    adat -= k*k