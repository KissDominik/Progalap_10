het52 = input("52.hét számai: ").split()
het52 = list(map(int, het52))

i = 0

while i < len(het52) - 1:
    if het52[i] > het52[i + 1]:
        het52[i], het52[i + 1] = het52[i + 1], het52[i]
        i = 0
    else:
        i += 1

#het52 = sorted([int(x) for x in input("52. hét számai: ").split()]) # 89 24 34 11 64

print(het52)
print()

f = open("lottosz.txt", "r")
lotto = []
for i in range(51):
    lotto.append([int(x) for x in f.readline().split()])

szam = int(input("szám 1-51 között: "))
print(lotto[szam-1])
print()

van = []
for i in range(len(lotto)):
    for j in range(len(lotto[i])):
        van.append(lotto[i][j])

if len(set(van)) == 90:
    print("Nincs")
else:
    print("Van")
print()

# paratlanok = [x for x in van if x % 2 != 0]
# print(paratlanok == paratlanok_2)

paratlanok_2 = []
for i in van:
    if i % 2 != 0:
        paratlanok_2.append(i)
print(len(paratlanok_2))