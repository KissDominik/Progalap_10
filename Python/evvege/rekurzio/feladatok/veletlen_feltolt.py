from random import randint

# A kapott "x" lista végéhez hozzáfűz "k" darab
# véletlen számot az [1, 30] intervallumból.
def c_feltolt(x, k):
    for i in range(k):
        x.append(randint(1, 30))

# Készíts rekurzív megoldást!
# Tilos "for" vagy "while" ciklus használata!
def r_feltolt(x, k):
    if k == 0:
        return 0
    x.append(randint(1, 30))
    return r_feltolt(x, k-1)

def main():
    x = [4, -3]
    r_feltolt(x, 7)
    print("A kapott lista:", x)

main()