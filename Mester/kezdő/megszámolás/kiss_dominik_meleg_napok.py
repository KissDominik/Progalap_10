a = list(map(int, input().split()))
db = 0

for i in range(a[0]):
    n = int(input())
    if n > a[1]:
        db += 1
print(db)