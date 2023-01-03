n = 32
Farg = []
lat = []
for i in range(n):
    inmatning = input().split()
    Farg.append(inmatning[0])
    lat.append(inmatning[1])
i = 0
while i < n-1 and not (Farg[i] == Farg[i+1]):
    i += 1
print(i+1)