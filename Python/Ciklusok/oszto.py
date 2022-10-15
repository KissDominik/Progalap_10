n = int(input("szám: "))
o = 1

for i in range(1, n+1):
    s = n / i
    if s % 1 == 0:
        print(s)