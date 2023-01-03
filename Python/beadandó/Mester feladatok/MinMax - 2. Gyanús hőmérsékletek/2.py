n = int(input())
grader = []
for i in range(n):
    grader.append(int(input()))
grader2 = grader.copy()
grader2 = [x for x in set(grader2)]
if len(grader2) == 1:
    print("0")
    exit()
mistenkelig = []
for i in range(1, n-1):
    mistenkelig.append(abs(((grader[i-1] + grader[i+1]) / 2 ) - grader[i]))
if len(grader) >= 3:
    print(mistenkelig.index(max(mistenkelig))+2)
else:
    print("1")