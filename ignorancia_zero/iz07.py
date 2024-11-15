#PEDINDO O VALOR
n1 = input('digite um número:')

#VERIFICANDO SE É NÚMERO
while n1.isnumeric() == False:
    if '.' in n1:
        if n1.islower() == False:
            if n1.isupper() == False:
                    break
            else:
                print('esse não é um valor válido, digite, novamente.')
                n1 = input('digite um número:')
        else:
            print('esse não é um valor válido, digite novamente.')
            n1 = input('digite um número:')
    else:
        print('esse não é um valor válido, digite novamente.')
        n1 = input('digite um número:')

#CONVERTENDO
if n1.isnumeric() == True:
    n1 = int(n1)
else:
    n1 = float(n1)

#CLASSIFICANDO
if n1 >= 0:
    print('{} é um número positivo.'.format(n1))
elif n1 < 0:
    print('{} é um número negativo.'.format(n1))
