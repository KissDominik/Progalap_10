from math import *

def n_alatt_k(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

n = int(input("n: "))
k = int(input("k: "))
print(n_alatt_k(n, k))