lista = []
for i in range(100):
    lista.append(input().split())

betuk = ["A", "B", "C", "D", "E", "F", "G", "H"]
helyes_db = 0

for i in range(100):

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
                hely = False

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
                hely = False

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
                hely = False

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
                hely = False

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
                hely = False

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
                hely = False

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
                hely = False

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
                hely = False
        
        else:
            hely == False
    
    if hely in betuk and a and b and c and d and e and f and g and h:
        helyes_db += 1
        print(i + 1, end=" ")

print()
print(helyes_db)