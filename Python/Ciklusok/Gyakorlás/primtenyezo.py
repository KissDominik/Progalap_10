n = int(input("n: ")) #3360
p = int(input("p: ")) #2
h = 0

while n % p == 0:
    n = n // p
    h += 1
print(p, "^", h, " * ", n, sep="")