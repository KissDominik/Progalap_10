n = 32
szin = []
szam = []
for i in range(n):
    be = input().split()
    szin.append(be[0])
    szam.append(be[1])
    
i = 0
while i < n-1 and not (szin[i] == szin[i+1]):
    i += 1
print(i+1)