# Készíts rekurzív megoldást! 
# Tilos "for" vagy "while" ciklus használata!

def c_vanParos(x):
    i = 0
    while i < len(x) and not(x[i] % 2 == 0):
        i += 1
    return i < len(x)

def r_vanParos(x):
    if len(x) == 1:
        return x[0]

    if x[0] % 2 == 0:
        x.pop(1)
        return r_vanParos(x)
    else:
        x.append(x.pop(0))
        return r_vanParos(x)

def main():
    x = [7, -1, 2, 3, 12, -4, 5, 10]
    print("Van-e páros:", r_vanParos(x))

main()