lista = []
matrix = []

for i in range(21):
    a = input()
    lista.append(a)

lista2 = []

for i in range(len(lista)-1):
    lista2.append(int(lista[i]) + int(lista[i+1]))
    
lista3 = []

for i in range(len(lista2)-1):
    lista3.append(int(lista2[i]) + int(lista2[i+1]))
    
lista4 = []

for i in range(len(lista3)-1):
    lista4.append(int(lista3[i]) + int(lista3[i+1]))

lista5 = []

for i in range(len(lista4)-1):
    lista5.append(int(lista4[i]) + int(lista4[i+1]))

lista6 = []

for i in range(len(lista5)-1):
    lista6.append(int(lista5[i]) + int(lista5[i+1]))

lista7 = []

for i in range(len(lista6)-1):
    lista7.append(int(lista6[i]) + int(lista6[i+1]))

lista8 = []

for i in range(len(lista7)-1):
    lista8.append(int(lista7[i]) + int(lista7[i+1]))

lista9 = []

for i in range(len(lista8)-1):
    lista9.append(int(lista8[i]) + int(lista8[i+1]))

lista10 = []

for i in range(len(lista9)-1):
    lista10.append(int(lista9[i]) + int(lista9[i+1]))

lista11 = []

for i in range(len(lista10)-1):
    lista11.append(int(lista10[i]) + int(lista10[i+1]))

lista12 = []

for i in range(len(lista11)-1):
    lista12.append(int(lista11[i]) + int(lista11[i+1]))

lista13 = []

for i in range(len(lista12)-1):
    lista13.append(int(lista12[i]) + int(lista12[i+1]))

lista14 = []

for i in range(len(lista13)-1):
    lista14.append(int(lista13[i]) + int(lista13[i+1]))

lista15 = []

for i in range(len(lista14)-1):
    lista15.append(int(lista14[i]) + int(lista14[i+1]))

lista16 = []

for i in range(len(lista15)-1):
    lista16.append(int(lista15[i]) + int(lista15[i+1]))

lista17 = []

for i in range(len(lista16)-1):
    lista17.append(int(lista16[i]) + int(lista16[i+1]))

lista18 = []

for i in range(len(lista17)-1):
    lista18.append(int(lista17[i]) + int(lista17[i+1]))

lista19 = []

for i in range(len(lista18)-1):
    lista19.append(int(lista18[i]) + int(lista18[i+1]))

lista20 = []

for i in range(len(lista19)-1):
    lista20.append(int(lista19[i]) + int(lista19[i+1]))

lista21 = []

for i in range(len(lista20)-1):
    lista21.append(int(lista20[i]) + int(lista20[i+1]))

print("1", lista)
print("2", lista2)
print("3", lista3)
print("4", lista4)
print("5", lista5)
print("6", lista6)
print("7", lista7)
print("8", lista8)
print("9", lista9)
print("10", lista10)
print("11", lista11)
print("12", lista12)
print("13", lista13)
print("14", lista14)
print("15", lista15)
print("16", lista16)
print("17", lista17)
print("18", lista18)
print("19", lista19)
print("20", lista20)
print("21", lista21)