a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
e = 0

if a < b:
    for i in range(a, b+1):
        if i % c == 0:
            e = e + 1
else:
    for i in range(b, a+1):
        if i % c == 0:
            e = e + 1
print(e)