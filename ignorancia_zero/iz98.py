def isalpha(texto):
    e = False
    for car in texto:
        if (65 <= ord(car) <= 90) == False and (97 <= ord(car) <= 122) == False:
            print('False')
            e = True
            break

    if e == False:
        print('True')

isalpha('abc')
isalpha('ab,c')
print('')

def islower(texto):
    e = False
    for car in texto:
        if 65 <= ord(car) <= 90:
            print('False')
            e = True
            break

    if e == False:
        print('True')

islower('abc')
islower('ABC')
islower('ab,c')
islower('AB,C')
print('')

def isupper(texto):
    e = False
    for car in texto:
        if 97 <= ord(car) <= 122:
            print('False')
            e = True
            break

    if e == False:
        print('True')

isupper('abc')
isupper('ABC')
isupper('ab,c')
isupper('AB,C')

