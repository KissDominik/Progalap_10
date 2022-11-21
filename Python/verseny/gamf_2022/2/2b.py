rendszam = []
be_ora = []
be_perc = []
ki_ora = []
ki_perc = []
ut = []
eredmény = 0

for i in range(300):
    a = input().split()
    rendszam.append(a[0])
    be_ora.append(int(a[1]))
    be_perc.append(int(a[2]))
    ki_ora.append(int(a[3]))
    ki_perc.append(int(a[4]))
    ut.append(int(a[5]))
print(rendszam)
print(be_ora)
print(be_perc)
print(ki_ora)
print(ki_perc)
print(ut)
print()

# v = s / t
g = 0
s = 10
for i in range(300):
    t = ki_perc[i] - be_perc[i]
    if t < 0:
        t += 60
    t /= 60
    v = s / t
    if v >= 100:
        print(rendszam[i]," ", v, sep="")
        g += 1
print(g)