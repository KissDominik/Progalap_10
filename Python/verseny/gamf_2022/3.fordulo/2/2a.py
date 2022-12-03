lista = []
for i in range(100):
    lista.append(input().split())

helyes_db = 0

for i in range(100):

    lehetseges = True
    hely = lista[i][1]

    for j in range(2, int(lista[i][0]) + 2):

        # a lepesek 1 2 3
        if hely == "A":
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
    
    if lehetseges == True:
        helyes_db += 1

print(helyes_db)