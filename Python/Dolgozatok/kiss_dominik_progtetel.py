n = int(input())
termekek = []
mennyisegek = []
ar = []



for i in range(n):
    bemenet = input().split()
    termekek.append(bemenet[0])
    mennyisegek.append(int(bemenet[1]))
    ar.append(int(bemenet[2]))



maximum = ar[0]
for i in range(1, n):
    if ar[i] > maximum:
        maximum = ar[i]
        index = i
print(termekek[index])



fizetendo_osszeg = 0
for i in range(n):
    fizetendo_osszeg += mennyisegek[i] * ar[i]
print(fizetendo_osszeg)



i = 0
while i < n and not (ar[i] > 400 and mennyisegek[i] > 5):
    i += 1
if i < n:
    print(termekek[i])
else:
    print("Nincs ilyen!")



elso_db = mennyisegek[0]
tobb = 0
for i in range(1, n):
    if mennyisegek[i] > elso_db:
        tobb += 1
print(tobb)