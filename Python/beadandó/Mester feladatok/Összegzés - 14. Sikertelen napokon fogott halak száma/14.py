nig = []
e = int(input())
r = int(input())

for i in range(e):
    er = int(input())
    if er < r:
        nig.append(er)

print(sum(nig))