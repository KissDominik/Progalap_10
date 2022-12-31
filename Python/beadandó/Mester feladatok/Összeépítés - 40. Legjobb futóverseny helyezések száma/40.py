n = int(input())
miejsce = []
for i in range(n):
    Wejscie = [int(x) for x in input().split()]
    miejsce.append(Wejscie[0])
print(min(miejsce), miejsce.count(min(miejsce)))