def minimum(x):
    if len(x) == 1:
        return x[0]

    if x[0] < x[1]:
        x.pop(1)
        return minimum(x)
    x.append(x.pop(0))
    return minimum(x)

def minimum(x):
    if len(x) == 1:
        return x[0]

    if x[1] < x[0]:
        x.pop(0)
        return minimum(x)
    x.append(x.pop(1))
    return minimum(x)