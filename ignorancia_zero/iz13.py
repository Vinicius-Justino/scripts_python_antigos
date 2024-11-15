#ESCOLHNEDO A BASE 
base = input('digite o valor da base base: ')

while base.isnumeric() == False:
    print('não é um valor válido, digite novamente.')
    base = input('digite o valor da base: ')

base = int(base)

#ESCOLHENDO O EXPOENTE
expoente = input('digite o expoente: ')

while expoente.isnumeric() == False:
    if '-' in expoente:
        if expoente.islower() == False:
            if expoente.isupper() == False:
                break
            else:
                print('não é um valor válido, digite novamente.')
                expoente = input('digite o expoente: ')
        else:
            print('não é um valor válido, digite novamente.')
            expoente = input('digite o expoente: ')
    else:
        print('não é um valor válido, digite novamente.')
        expoente = input('digite o expoente: ')

expoente = int(expoente)
expoente2 = expoente

#BOOM! BUTTERFLY EFECT!
if expoente == 0:
    print('{} elevado a {} é 1.'.format(base, expoente2))

elif expoente < -1:
    potencia = base*base
    expoente = expoente + 1
    while expoente < -1:
        potencia = potencia*base
        expoente = expoente + 1
    print('{} elevado a {} é 1/{}.'.format(base, expoente2, potencia))

elif expoente == -1:
    print('{} elevado a {} é 1/{}.'.format(base, expoente2, base))

elif expoente == 1:
    print('{} elevado a {} é {}.'.format(base, expoente2, base))

elif expoente > 1:
    potencia = base*base
    expoente = expoente - 1
    while expoente > 1:
        potencia = potencia*base
        expoente = expoente - 1
    print('{} elevado a {} é {}.'.format(base, expoente2, potencia))
