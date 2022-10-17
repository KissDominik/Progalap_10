kk = int(input("kutya kora:"))
k2 = 0

for i in range(kk - 1):
    if i <= 1:
        k1 = i * 10.5
    elif i >= 2:
        k2 = i * 4
    print(k1 + k2, i)