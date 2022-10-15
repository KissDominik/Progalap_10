h = 8
m = 0

while h < 18:
    if m >= 6:
        m -= 6
        h += 1
    if h < 10:
        print("0", h, ":", m, "0", sep="")
    else:
        print(h, ":", m, "0", sep="")
    m += 5