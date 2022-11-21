from random import *
a = []

for i in range(10):
    a.append(randint(0, 100))
print(a)

i = 0

while i < len(a) - 1:
    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
        i = 0
    else:
        i += 1
print(a)