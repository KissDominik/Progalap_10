a = input()
while not 0 < len(a) < 255:
    print()
    print("0-255 betű")
    print()
    a = input()

ekezet = ["á", "é", "í", "ö", "ü", "ó", "ő", "ú", "ű"]
ekezetlen = ["a", "e", "i", "o", "u", "o", "o", "u", "u"]
szo = []
for i in range(len(a)):
    szo.append(a[i])

for i in range(len(szo)):
    for j in range(len(ekezet)):
        if szo[i] == ekezet[j]:
            szo[i] = ekezetlen[j]

b = str()
for i in szo:
    b += i.upper()
print(b)

kulcsszo = input()