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

for i in range(300):
    if be_ora[i] == 12 or ki_ora[i] == 12:
        print(rendszam[i], " ", be_ora[i], ":", be_perc[i], " ", ki_ora[i], ":", ki_perc[i], sep="")
# a megoldás 2