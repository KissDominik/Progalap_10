n = int(input("n: "))
s1 = 0
s2 = 1
print("1")
for i in range(n + 1):
    s = s1 + s2
    print(s)
    s1 = s2
    s2 = s