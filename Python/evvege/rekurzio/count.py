def megszamolas(x):
    if len(x) != 0:
        if x.pop() == 5:
            return 1 + megszamolas(x)
        else:
            return megszamolas(x)
    return 0