n = int(input("n: "))
#523

while n % 10 != 3 and n % 10 != 6 and n % 10 != 9:
    print("nem oszthato harommal az utolso szam")
    n = int(input("n: "))
print("a megoldas helyes")