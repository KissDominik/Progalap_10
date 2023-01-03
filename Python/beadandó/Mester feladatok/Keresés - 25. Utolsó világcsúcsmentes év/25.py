n = int(input())
jaar = []
hoogte = []
for i in range(n):
    invoer = [int(x) for x in input().split()]
    jaar.append(invoer[0])
    hoogte.append(invoer[1])
liedje = max(jaar)
while liedje in jaar:
    liedje -= 1
print(liedje)