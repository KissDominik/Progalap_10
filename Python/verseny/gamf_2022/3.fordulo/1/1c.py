szavak = []

for i in range(1239):
    sor = input().split()
    for j in sor:
        szavak.append(j)


for i in range(len(szavak)):
        szavak[i] = len(szavak[i])
# print(szavak)


#szavak hossza és mennyisége
hosszak = [[x,szavak.count(x)] for x in set(szavak)]
print(hosszak)


#ellenőrzés
összeg = 0
for i in range(len(hosszak)):
        összeg += hosszak[i][1]
print(összeg)