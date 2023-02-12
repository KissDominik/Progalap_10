# a = input("telefonszám: ")

# mobil = [39, 41, 71]

# if int(a[0]+a[1]) in mobil:
#     print("mobil")
# else:
#     print("vezetékes")


# b = [int(x) for x in input("hívás kezdete: ").split()]
# c = [int(x) for x in input("hívás vége: ").split()]
# számla1 = (c[0]*60*60 + c[1]*60 + c[2]) - (b[0]*60*60 + b[1]*60 + b[2])

# if számla1 % 60 != 0:
#     print(számla1//60+1)
# else:
#     print(számla1//60)

fr = open("HIVASOK.txt", "r")
sorok = fr.readlines()
fr.close()

idopontok = []
szam = []

i = 0
while i < len(sorok):
    idopontok.append([int(x) for x in sorok[i].split()])
    szam.append(int(sorok[i+1]))
    i += 2

percek = []
for i in range(len(idopontok)):
    számla2 = (idopontok[i][3]*60*60 + idopontok[i][4]*60 + idopontok[i][5]) - (idopontok[i][0]*60*60 + idopontok[i][1]*60 + idopontok[i][2])

    if számla2 % 60 != 0:
        percek.append(számla2//60+1)
    else:
        percek.append(számla2//60)

fw = open("percek.txt", "w+")
for i in range(len(szam)):
    fw.write(str(percek[i]) + "/n")
    fw.write(str(szam[i]) + "/n")
fw.close()