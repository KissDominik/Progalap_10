def osszegzes(x):
    if len(x) == 0:
        return 0
    else:
        return x.pop(0) + osszegzes(x)



def megszamolas(x):
    if x[0] != 5:
        return megszamolas(x.pop(0))
    else:
        return megszamolas(x.append(x.pop(0)))


        