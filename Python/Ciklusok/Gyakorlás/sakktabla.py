n = int(input("n: "))

for i in range(n):
    if i % 2 == 0:
        for j in range(1, n+1):
            if j % 2 == 0:
                print("w", end=" ")
            else:
                print("b", end=" ")
    else:
        for j in range(1, n+1):
            if j % 2 != 0:
                print("w", end=" ")
            else:
                print("b", end=" ")
    print()

# for i in range(8):
#     if i % 2 == 0:
#         for j in range(4):
#             print("b", end=" ")
#             print("w", end=" ")
#         print()
#     else:
#         for j in range(4):
#             print("w", end=" ")
#             print("b", end=" ")
#         print()