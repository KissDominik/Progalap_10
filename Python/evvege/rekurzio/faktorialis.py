def faktorialis(x):
    if x == 0:
        return 1
    else:
        return x * faktorialis(x-1)