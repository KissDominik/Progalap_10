n = int(input())
varos = []
erkezesi_ido = []
indulasi_ido = []

for i in range(n):
    be = input().split()
    varos.append(be[0])
    erkezesi_ido.append(int(be[1]))
    indulasi_ido.append(int(be[2]))


i = 0
while i < n and not (varos[i] == "Pecs" and erkezesi_ido[i] != -1 and indulasi_ido[i] == 9999):
    i += 1

if i < n:
    print("IGEN")
else:
    print("NEM")