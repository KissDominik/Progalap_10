be = input().split()
n = int(be[0])
nev = be[1]
nevek = []
szamok = 0
index = []

for i in range(n):
    a = input()
    nevek.append(a)
    if nev == nevek[i]:
        szamok += 1
        index.append(i)


print(szamok, end = " ")
for i in range(len(index)):
    print(index[i], end = " ")