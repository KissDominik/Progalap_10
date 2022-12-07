n = int(input())
varos = []
erkezes = []
indulas = []

for i in range(n):
    be = input().split() 
    varos.append(be[0])
    erkezes.append(int(be[1]))
    indulas.append(int(be[2]))

i = 0
while i < n and not (varos[i] == "Szekesfehervar" and erkezes[i] == -1):
    i += 1
if i < n:
    print(i+1)
else:
    print("-1")