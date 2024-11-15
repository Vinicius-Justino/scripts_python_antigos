def totalmenteUmRange(x, y):
    if x == y:
        print(y)
        return y
    print(x)
    return totalmenteUmRange(x+1, y)

totalmenteUmRange(1, 100)
