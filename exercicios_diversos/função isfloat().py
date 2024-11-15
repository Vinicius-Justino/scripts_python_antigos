def isfloat(x):
    x = str(x)
    if '.' in x:
        if x.islower() == False:
            if x.isupper() == False:
                if x.istitle() == False:
                    r = True
                else:
                    r = False
            else:
                r = False
        else:
            r = False
    else:
        if x.isnumeric() == True:
            r = True

        else:
            r = False

    return r

print(isfloat(7.0))
print(isfloat(1))
print(isfloat('a'))
print(isfloat(6.5))
print(isfloat('Python'))
