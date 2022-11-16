a = [1.23, 3, 43, 3.4, 54, 7, 78.75]
for i in range(len(a)):
    if a[i] % 2 != 0:
        a[i] = int(a[i])
print(a)