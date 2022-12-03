lista = []
for i in range(100):
    lista.append(input().split())

helyes_db = 0

for i in range(100):

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
                hely = False


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
                hely = False


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
                hely = False


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
                hely = False


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
                hely = False


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
                hely = False


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
                hely = False


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
                hely = False

        
        else:
            hely == False
    
    if hely != False and a_b and a_d and a_e and e_f and e_h and f_b and h_d and g_f and g_c and g_h and c_b and c_d:
        helyes_db += 1
        print(i + 1, end=" ")

print()
print(helyes_db)