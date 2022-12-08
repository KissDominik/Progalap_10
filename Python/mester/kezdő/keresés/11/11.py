n = int(input())
lista_min = []
lista_max = []

for i in range(n):
    be = list(map(int, input().split()))
    lista_min.append(be[0])
    lista_max.append(be[1])

i = 1
while i < n and not (lista_max[i] < lista_min[i-1]):
    i += 1

if i < n:
    print(i+1)
else:
    print("-1")