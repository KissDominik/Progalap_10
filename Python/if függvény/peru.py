jegy = int(input("jegy: "))
if jegy < 1 or jegy > 20:
    print("hibas!")
    exit()
else:
    if jegy <= 10:
        print("bukott")
    else:
        print("nembukott")
print("program vége")