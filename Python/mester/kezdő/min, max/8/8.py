n = int(input())
l = []
max = 0

for i in range(n):
    be = list(map(int, input().split()))
    l.append(be)
    if be[i] > max:
        index = i
print(l[index])