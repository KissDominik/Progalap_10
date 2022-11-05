from math import *

n = int(input("n: "))
eredmény = 0

for i in range(1, n+1):
    összeg = 1 / (sqrt(i) + sqrt((i - 1)))
    eredmény += összeg
    print(eredmény)
    # Négyzetszámoknál mindig egész az eredmény