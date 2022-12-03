bemenet = "403292963733218921303328606261120475832956098470061489222021941160891584704399888549234627049830837928369818247008386334945660063804769026872676317213961646638602950029510034410209339645064157605742674247689838912413030584711676963415048434908804062786232792850219375660393320882593952053160336200718"

szorzat = []

i = 0
for i in range(i, len(bemenet) - 10):
        szorzat.append(bemenet[i:i+10])


szamok = []

for i in range(len(szorzat)):
    szorzo = 1
    for j in range(len(szorzat[i])):
        szorzando = int(szorzat[i][j])
        szorzo *= szorzando 
    szamok.append(szorzo)


szamok = list(set(szamok))
print(szamok)

max = 0
for i in szamok:
    if i > max:
        max = i
print(max)