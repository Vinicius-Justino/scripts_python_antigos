#ESCOLHENDO O PRIMEIRO NÚMERO
n1 = input('digite o primeiro número: ')

#VERIFICANDO SE É NÚMERO
while n1.isnumeric() == False:
    if '.' in n1:
        if n1.islower() == False:
            if n1.isupper() == False:
                    break
            else:
                print('não é um valor válido, digite novamente.')
                n1 = input('digite o primeiro número: ')
        else:
            print('não é um valor válido, digite novamente.')
            n1 = input('digite o primeiro número: ')
    else:
        print('não é um valor válido, digite novamente.')
        n1 = input('digite o primeiro número: ')

#CONVERTENDO
if n1.isnumeric() == True:
    n1 = int(n1)
else:
    n1 = float(n1)

#ESCOLHENDO O SEGUNDO NÚMERO
n2 = input('digite o segundo número: ')

#VERIFICANDO SE É NÚMERO
while n2.isnumeric() == False:
    if '.' in n2:
        if n2.islower() == False:
            if n2.isupper() == False:
                    break
            else:
                print('não é um valor válido, digite novamente.')
                n2 = input('digite o segundo número: ')
        else:
            print('não é um valor válido, digite novamente.')
            n2 = input('digite o segundo número: ')
    else:
        print('não é um valor válido, digite novamente.')
        n2 = input('digite o segundo número: ')

#CONVERTENDO
if n2.isnumeric() == True:
    n2 = int(n2)
else:
    n2 = float(n2)

#COMPARANDO OS NÚMEROS
if n1 > n2:
    print('o maior valor entre {} e {} é {}.'.format(n1, n2, n1))
elif n1 < n2:
    print('o maior valor entre {} e {} é {}.'.format(n1, n2, n2))
elif n1 == n2:
    print('esse valores são iguais.')
