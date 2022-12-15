n = int(input())
k = int(input())
nig = []

for i in range(n):
    er = int(input())
    if er < k:
        nig.append(er)

print(sum(nig))