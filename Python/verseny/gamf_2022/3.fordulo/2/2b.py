# 4 a 2 1 3 4 szoval 4+1 input van
# Hány olyan útvonal van a kocka élein megvalósíthatóak között, amelynek során a hangya a kocka
# minden csúcsán jár? 

lista = []
for i in range(100):
    w = input().split()
    lista.append(w)

helyes_db = 0

for i in range(100):

    lehetseges = True
    hely = lista[i][1]

    a = False
    b = False
    c = False
    d = False
    e = False
    f = False
    g = False
    h = False

    for j in range(2, int(lista[i][0]) + 2):

        # a lepesek 1 2 3
        if hely == "A":

            a = True

            if lista[i][j] == "1":
                hely = "B"
            elif lista[i][j] == "2":
                hely = "D"
            elif lista[i][j] == "3":
                hely = "E"
            else:
                lehetseges = False
                # print("a")

        # b lepesek 2 3 4
        elif hely == "B":

            b = True

            if lista[i][j] == "2":
                hely = "C"
            elif lista[i][j] == "3":
                hely = "F"
            elif lista[i][j] == "4":
                hely = "A"
            else:
                lehetseges = False
                # print("b")

        # c lepesek 3 4 5
        elif hely == "C":

            c = True

            if lista[i][j] == "3":
                hely = "G"
            elif lista[i][j] == "4":
                hely = "D"
            elif lista[i][j] == "5":
                hely = "B"
            else:
                lehetseges = False
                # print("c")

        # d lepesek 1 3 5
        elif hely == "D":

            d = True

            if lista[i][j] == "1":
                hely = "C"
            elif lista[i][j] == "3":
                hely = "H"
            elif lista[i][j] == "5":
                hely = "A"
            else:
                lehetseges = False
                # print("d")

        # e lepesek 1 2 6
        elif hely == "E":

            e = True

            if lista[i][j] == "1":
                hely = "F"
            elif lista[i][j] == "2":
                hely = "H"
            elif lista[i][j] == "6":
                hely = "A"
            else:
                lehetseges = False
                # print("e")

        # f lepesek 2 4 6
        elif hely == "F":

            f = True

            if lista[i][j] == "2":
                hely = "G"
            elif lista[i][j] == "4":
                hely = "E"
            elif lista[i][j] == "6":
                hely = "B"
            else:
                lehetseges = False
                # print("f")

        # g lepesek 4 5 6
        elif hely == "G":

            g = True

            if lista[i][j] == "4":
                hely = "H"
            elif lista[i][j] == "5":
                hely = "F"
            elif lista[i][j] == "6":
                hely = "C"
            else:
                lehetseges = False
                # print("g")

        # h lepesek 1 5 6
        elif hely == "H":

            h = True

            if lista[i][j] == "1":
                hely = "G"
            elif lista[i][j] == "5":
                hely = "E"
            elif lista[i][j] == "6":
                hely = "D"
            else:
                lehetseges = False
                # print("h")
        
        else:
            lehetseges == False
    
    if lehetseges == True and a == True and b == True and c == True and d == True and e == True and f == True and g == True and g == True and h == True:
        helyes_db += 1

print(helyes_db)