#ESCOLHENDO O PRIMEIRO NÚMERO
n1 = input('digite o primeiro número: ')
while n1.isnumeric() == False:
    if '.' in n1:
        if n1.islower() == False:
            if n1.isupper() == False:
                break
            else:
                print('não é um valor válido digite novamente.')
                n1 = input('digite o primeiro número: ')
        else:
            print('não é um valor válido digite novamente.')
            n1 = input('digite o primeiro número: ')
    else:
        print('não é um valor válido digite novamente.')
        n1 = input('digite o primeiro número: ')

#ESCOLHENDO O SEGUNDO NÚMERO
n2 = input('digite o segundo número: ')
while n2.isnumeric() == False:
    if '.' in n2:
        if n2.islower() == False:
            if n2.isupper() == False:
                break
            else:
                print('não é um valor válido digite novamente.')
                n2 = input('digite o segundo número: ')
        else:
            print('não é um valor válido digite novamente.')
            n2 = input('digite o segundo número: ')
    else:
        print('não é um valor válido digite novamente.')
        n2 = input('digite o segundo número: ')

#ESCOLHENDO O TERCEIRO NÚMERO
n3 = input('digite o terceiro número: ')
while n3.isnumeric() == False:
    if '.' in n3:
        if n3.islower() == False:
            if n3.isupper() == False:
                break
            else:
                print('não é um valor válido digite novamente.')
                n3 = input('digite o terceiro número: ')
        else:
            print('não é um valor válido digite novamente.')
            n3 = input('digite o terceiro número: ')
    else:
        print('não é um valor válido digite novamente.')
        n3 = input('digite o terceiro número: ')

#CONVERTENDO
if n1.isnumeric() == True:
    n1 = int(n1)
elif '.' in n1:
    n1 = float(n1)

if n2.isnumeric() == True:
    n2 = int(n2)
elif '.' in n2:
    n2 = float(n2)

if n3.isnumeric() == True:
    n3 = int(n3)
elif '.' in n3:
    n3 = float(n3)

#COMPARANDO
if n1 > n2:
    if n2 > n3:
        print('esses números em ordem crescente são: {}, {} e {}.'.format(n3, n2, n1))
    elif n2 < n3:
        if n3 < n1:
            print('esses números em ordem crescente são: {}, {} e {}.'.format(n2, n3, n1))
        elif n3 > n1:
            print('esses números em ordem crescente são: {}, {} e {}.'.format(n2, n1, n3))

elif n2 > n1:
    if n1 > n3:
        print('esses números em ordem crescente são: {}, {} e {}.'.format(n3, n1, n2))
    elif n1 < n3:
        if n3 < n2:
            print('esses números em ordem crescente são: {}, {} e {}.'.format(n1, n3, n2))
        elif n3 > n2:
            print('esses números em ordem crescente são: {}, {} e {}.'.format(n1, n2, n3))

elif n3 > n2:
    if n2 > n1:
        print('esses números em ordem crescente são: {}, {} e {}.'.format(n1, n2, n3))
    elif n2 < n1:
        if n1 < n3:
            print('esses números em ordem crescente são: {}, {} e {}.'.format(n2, n1, n3))
        elif n1 > n3:
            print('esses números em ordem crescente são: {}, {} e {}.'.format(n2, n3, n1))
