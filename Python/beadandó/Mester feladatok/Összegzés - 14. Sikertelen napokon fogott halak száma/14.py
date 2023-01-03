n = int(input())
k = int(input())
jours = []
for i in range(n):
    des_poissons = int(input())
    if des_poissons < k:
        jours.append(des_poissons)
print(sum(jours))