n = int(input())

nev = []
magassag = []

for i in range(n):
    be = input().split()
    nev.append(be[0])
    magassag.append(int(be[1]))

i = 1
while i < n and not (magassag[i] < magassag[i-1] and nev[i][0] < nev[i][1]):
    i += 1

if i < n:
    print("NEM") 
else:
    print("IGEN") 