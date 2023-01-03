n = int(input())
minut = []
secunde = []
for i in range(n):
    intrare = [int(x) for x in input().split()]
    minut.append(intrare[1])
    secunde.append(intrare[2])
timp = []
for i in range(n):
    timp.append(minut[i] * 60 + secunde[i])
Cantitate = 0
for i in range(1, n):
    if timp[i] < timp[i-1]:
        Cantitate += 1
print(Cantitate)