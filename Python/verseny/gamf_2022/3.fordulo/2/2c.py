# 4 a 2 1 3 4 szoval 4+1 input van
# Hány olyan útvonal van a kocka élein megvalósíthatóak között, amelynek során a hangya a kocka
# minden élén jár?

lista = []
for i in range(100):
    w = input().split()
    lista.append(w)

helyes_db = 0

for i in range(100):

    lehetseges = True
    hely = lista[i][1]

    a_b = False
    a_d = False
    a_e = False
    e_f = False
    e_h = False
    f_b = False
    h_d = False
    g_h = False
    g_f = False
    g_c = False
    c_d = False
    c_b = False

    for j in range(2, int(lista[i][0]) + 2):

        # a lepesek 1 2 3
        if hely == "A":
            if lista[i][j] == "1":
                hely = "B"
                a_b = True
            elif lista[i][j] == "2":
                hely = "D"
                a_d = True
            elif lista[i][j] == "3":
                hely = "E"
                a_e = True
            else:
                lehetseges = False
                # print("a")

        # b lepesek 2 3 4
        elif hely == "B":
            if lista[i][j] == "2":
                hely = "C"
                c_b = True
            elif lista[i][j] == "3":
                hely = "F"
                f_b = True
            elif lista[i][j] == "4":
                hely = "A"
                a_b = True
            else:
                lehetseges = False
                # print("b")

        # c lepesek 3 4 5
        elif hely == "C":
            if lista[i][j] == "3":
                hely = "G"
                g_c = True
            elif lista[i][j] == "4":
                hely = "D"
                c_d = True
            elif lista[i][j] == "5":
                hely = "B"
                c_b = True
            else:
                lehetseges = False
                # print("c")

        # d lepesek 1 3 5
        elif hely == "D":
            if lista[i][j] == "1":
                hely = "C"
                c_d = True
            elif lista[i][j] == "3":
                hely = "H"
                h_d = True
            elif lista[i][j] == "5":
                hely = "A"
                a_d = True
            else:
                lehetseges = False
                # print("d")

        # e lepesek 1 2 6
        elif hely == "E":
            if lista[i][j] == "1":
                hely = "F"
                e_f = True
            elif lista[i][j] == "2":
                hely = "H"
                e_h = True
            elif lista[i][j] == "6":
                hely = "A"
                a_e = True
            else:
                lehetseges = False
                # print("e")

        # f lepesek 2 4 6
        elif hely == "F":
            if lista[i][j] == "2":
                hely = "G"
                g_f = True
            elif lista[i][j] == "4":
                hely = "E"
                e_f = True
            elif lista[i][j] == "6":
                hely = "B"
                f_b = True
            else:
                lehetseges = False
                # print("f")

        # g lepesek 4 5 6
        elif hely == "G":
            if lista[i][j] == "4":
                hely = "H"
                g_h = True
            elif lista[i][j] == "5":
                hely = "F"
                g_f = True
            elif lista[i][j] == "6":
                hely = "C"
                g_c = True
            else:
                lehetseges = False
                # print("g")

        # h lepesek 1 5 6
        elif hely == "H":
            if lista[i][j] == "1":
                hely = "G"
                g_h = True
            elif lista[i][j] == "5":
                hely = "E"
                e_h = True
            elif lista[i][j] == "6":
                hely = "D"
                h_d = True
            else:
                lehetseges = False
                # print("h")
        
        else:
            lehetseges == False
    
    if lehetseges == True and a_b == True and a_d == True and a_e == True and e_f == True and e_h == True and f_b == True and h_d == True and g_f == True and g_c == True and g_h == True and c_b == True and c_d == True:
        helyes_db += 1

print(helyes_db)