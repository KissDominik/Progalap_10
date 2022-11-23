szamok = input()
db = 0
hasznalt = []

for i in range(len(szamok)-3):
    szam = int(szamok[i:i+4])
    if szam >= 1000:
        if not szam in hasznalt:
            db += 1
            hasznalt.append(szam)

print(db)