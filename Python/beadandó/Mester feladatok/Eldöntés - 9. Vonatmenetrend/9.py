n = int(input())
kaupunki = []
Lahtoaika = []
kaupunkiok = []
for i in range(n):
    syotto = input().split()
    kaupunki.append(syotto[0])
    Lahtoaika.append(int(syotto[2]))
    if Lahtoaika[i] == 9999:
        kaupunkiok.append(kaupunki[i])
kaupunkiok = [x for x in set(kaupunkiok)]
if len(kaupunkiok) == 1 and kaupunkiok[0] == "Pecs":
    print("IGEN")
else:
    print("NEM")