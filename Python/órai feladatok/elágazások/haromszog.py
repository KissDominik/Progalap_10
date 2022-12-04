a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a + b > c and b + c > a and a + c > b:
    print("háromszög")
else:
    print("nem háromszög")