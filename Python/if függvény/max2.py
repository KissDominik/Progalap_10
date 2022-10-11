a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

maximum = a
if b > maximum:
    maximum = b
elif c > maximum:
    maximum = c
else:
    print(maximum)