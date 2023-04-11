def T() -> bool:
    return True

def f(x):
    r = 0
    for i in range(len(x)-1):
        if T():
            r += r
    return r
                                                            
# a) megszamolas tetel
# b) kereses tetel
# c) osszegzes tetel
# d) kivalasztas tetel