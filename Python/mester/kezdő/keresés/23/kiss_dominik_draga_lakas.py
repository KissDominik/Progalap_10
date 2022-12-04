be = list(map(int, input().split()))
megoldasok = []
for i in range(be[0]):
    be2 = list(map(int, input().split()))
    if be2[0] >= be[2] and be2[1] >= be[1]:
        megoldasok.append(i+1)
print(megoldasok[0])