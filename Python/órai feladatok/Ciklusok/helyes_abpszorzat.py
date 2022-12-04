a = int(input("a: "))
b = int(input("b: "))
p = 1

while a == b:
    print("a két szám nem lehet egyenlő")
    a = int(input("a: "))
    b = int(input("b: "))

if a < b:
    if a % 2 == 0:
        for i in range(a+1, b+1, 2):
            p = p * i
        print(p)
    else:
        for i in range(a, b+1, 2):
            p = p * i
        print(p)
else:
    c = a
    a = b
    b = c
    if a % 2 == 0:
        for i in range(a+1, b+1, 2):
            p = p * i
        print(p)
    else:
        for i in range(a, b+1, 2):
            p = p * i
        print(p)