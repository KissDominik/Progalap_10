n = int(input())
fok = []

for i in range(n):
    fok.append(int(input()))

fok2 = fok.copy()
fok2 = [x for x in set(fok2)]
if len(fok2) == 1:
    print("0")
    exit()

sus = []

for i in range(1, n-1):
    sus.append(abs(((fok[i-1] + fok[i+1]) / 2 ) - fok[i]))

sussy = max(sus)

if len(fok) >= 3:
    print(sus.index(sussy)+2)
else:
    print("1")