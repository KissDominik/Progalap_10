# beolvasas
bemenet1 = "403292963733218921303328606261120475832956098470061489222021941160891584704399888549234627049830837928369818247008386334945660063804769026872676317213"
bemenet2 = "961646638602950029510034410209339645064157605742674247689838912413030584711676963415048434908804062786232792850219375660393320882593952053160336200718"

osszes_szam1 = []
osszes_szam2 = []

# osszes letrehozhato szam 2 listaban eltarolva
for i in range(150):
    for j in range(i, 150):
        osszes_szam1.append(bemenet1[i:j+1])
        osszes_szam2.append(bemenet2[i:j+1])


# minden elem szamma alakitasa
osszes_szam1 = [int(x) for x in osszes_szam1]
osszes_szam2 = [int(x) for x in osszes_szam2]


# 10 es 19 kozti szamok kivalasztasa
halmaz1 = []
for i in osszes_szam1:
    if 10 <= i <= 19:
        halmaz1.append(i)
print(halmaz1)

halmaz2 = []
for i in osszes_szam2:
    if 10 <= i <= 19:
        halmaz2.append(i)
print(halmaz2)
print()


# duplikaciok eltuntetese
halmaz1 = set(halmaz1)
halmaz2 = set(halmaz2)
print(halmaz1)
print(halmaz2)
print()

metszet_komplementer = list(halmaz1 ^ halmaz2)
print(metszet_komplementer)
print()

szorzat = 1
for i in metszet_komplementer:
    szorzat *= i
print(szorzat)