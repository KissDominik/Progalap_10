a = int(input("a: "))
b = int(input("b: "))
p = 1

if a != b:
    if a < b and a % 2 != 0:
        for i in range(a, b+1, 2):
            p = p * i
        print(p)
    elif a < b and a % 2 == 0:
        for i in range(a+1, b+1, 2):
            p = p * i
        print(p)
    elif b < a and b % 2 != 0:
        for i in range(b, a+1, 2):
            p = p * i
        print(p)
    elif b < a and b % 2 == 0:
        for i in range(b+1, a+1, 2):
            p = p * i
        print(p)
    else:
        pass
else:
    while a == b:
        print("a két szám nem lehet egyenlő")
        a = int(input("a: "))
        b = int(input("b: "))