n = int(input())
varos = []
erkezesi_ido = [] # 24*60 = 1440 a maximum - -1 ha nem ertelmezheto
indulasi_ido = [] # rendezve van indulasi ido szerint - 9999 ha nem ertelmezheto

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