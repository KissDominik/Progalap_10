jegyek = [int(input("1: ")), int(input("2: ")), int(input("3: ")), int(input("4: ")), int(input("5: "))]
átlag = jegyek[0] * 1 + jegyek[1] * 2 + jegyek[2] * 3 + jegyek[3] * 4 + jegyek[4] * 5
oszt = jegyek[0] + jegyek[1] + jegyek[2] + jegyek[3] + jegyek[4]

print("Éves átlag:", átlag/oszt)
print()

tantargyi = []
for i in range(10):
    tantargyi.append(float(input("jegy kerekítve: ")))
t_atlag = sum(tantargyi) / 10

print("tantárgyi átlag:", t_atlag)
