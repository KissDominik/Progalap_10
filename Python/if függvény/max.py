from distutils import bcppcompiler
from re import X


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if b < a and c < a:
    print(a)
elif a < b and c < b:
    print(b)
elif a < c and b < c:
    print(c)
else:
    print("több megoldás van")