n = int(input())
perc = []
mp = []
for i in range(n):
    be = [int(x) for x in input().split()]
    perc.append(be[1])
    mp.append(be[2])

ido = []
for i in range(n):
    ido.append(perc[i] * 60 + mp[i])
osszeg = 0
for i in range(1, n):
    if ido[i] < ido[i-1]:
        osszeg += 1
print(osszeg)