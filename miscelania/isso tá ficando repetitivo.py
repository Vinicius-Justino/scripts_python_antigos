n = 1
irredutiveis = 0

while n <= 50:
    numerador = 5*n+6
    denominador = 6*n+5

    irredutivel = True
    maior = max(numerador, denominador)
    simplificador = 2
    complemento = 'É irredutível'

    while simplificador <= maior:
        if numerador%simplificador == 0 and denominador%simplificador == 0:
            irredutivel = False
            complemento = 'Não é irredutível'
            break

        simplificador += 1

    print('       {}'.format(numerador))
    print('{} = -------  {}'.format(n, complemento))
    print('       {}'.format(denominador))
    print('')
    print('')

    if irredutivel:
        irredutiveis += 1

    n += 1

print('\n{} números entre 1 e 50 tem a fração irredutível quando 5n+6/6n+5.'.format(irredutiveis))

