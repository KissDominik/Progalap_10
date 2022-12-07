k = int(input())
összeg = 0
szel = []
hossz = []

for i in range(k):
    be = list(map(int, input().split()))
    szel.append(be[0])
    hossz.append(be[1])
    összeg += szel[i] * hossz[i]
print(összeg)