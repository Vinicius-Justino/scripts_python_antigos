print('     CAIXA ELETRÔNICO')
print('saque mínimo: 10 reais.')
print('saque máximo: 600 reais.')

#ESCOLHENDO O VALOR A SER SACADO
valor = input('digite o valor a ser sacado: ')

while valor.isnumeric() == False:
    print('não é um valor válido, digite novamente.')
    valor = input('digite o valor a ser sacado: ')

valor = int(valor)

while valor < 10 or valor > 600:
    if valor > 600:
        print('esse valor é muito grande, digite novamente.')

    elif valor < 10:
        print('esse valor é muito pequeno, digite novamente.')

    valor = input('digite o valor a ser sacado: ')

    while valor.isnumeric() == False:
        print('não é um valor válido, digite novamente.')
        valor = input('digite o valor a ser sacado: ')

    valor = int(valor)

    if valor >= 10 and valor <= 600:
        break

#ESCOLHENDO AS NOTAS
nota100 = valor//100
resto100 = valor%100

nota50 = resto100//50
resto50 = resto100%50

nota10 = resto50//10
resto10 = resto50%10

nota5 = resto10//5

nota1 = resto10%5

#MOSTRANDO NA TELA
if nota100 != 0:
    if nota50 != 0:
        if nota10 != 0:
            if nota5 != 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 50 reais, {} notas de 10,\n {} notas de 5 e {} notas de 1 real.'.format(nota100, nota50, nota10, nota5, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 50 reais, {} notas de 10,\ne {} notas de 5.'.format(nota100, nota50, nota10, nota5))
            elif nota5 == 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 50 reais, {} notas de 10,\ne {} notas de 1 real.'.format(nota100, nota50, nota10, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 50 reais, e {} notas de 10.'.format(nota100, nota50, nota10))
        elif nota10 == 0:
            if nota5 != 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 50 reais, {} notas de 5,\ne {} notas de 1 real.'.format(nota100, nota50, nota5, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 50 reais e {} notas de 5.'.format(nota100, nota50, nota5))
            elif nota5 == 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 50 reais e {} notas de 1.'.format(nota100, nota50, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais e {} notas de 50 reais.'.format(nota100, nota50))
    elif nota50 == 0:
        if nota10 != 0:
            if nota5 != 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 10, {} notas de 5 \ne {} notas de 1 real.'.format(nota100, nota10, nota5, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 10, {} notas de 5.'.format(nota100, nota10, nota5))
            elif nota5 == 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 10, {} notas de 1 real.'.format(nota100, nota10, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais, e {} notas de 10.'.format(nota100, nota10))
        elif nota10 == 0:
            if nota5 != 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais, {} notas de 5, \ne {} notas de 1 real.'.format(nota100, nota5, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais, e {} notas de 5.'.format(nota100, nota5))
            elif nota5 == 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 100 reais e {} notas de 1.'.format(nota100, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 100 reais.'.format(nota100))
elif nota100 == 0:
    if nota50 != 0:
        if nota10 != 0:
            if nota5 != 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 50 reais, {} notas de 10, {} notas de 5\ne {} notas de 1 real.'.format(nota50, nota10, nota5, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 50 reais, {} notas de 10, e {} notas de 5.'.format(nota50, nota10, nota5))
            elif nota5 == 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 50 reais, {} notas de 10, e {} notas de 1 real.'.format(nota50, nota10, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 50 reais, e {} notas de 10.'.format( nota50, nota10))
        elif nota10 == 0:
            if nota5 != 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 50 reais, {} notas de 5, e {} notas de 1 real.'.format(nota50, nota5, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 50 reais, e {} notas de 5.'.format(nota50, nota5))
            elif nota5 == 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 50 reais e {} notas de 1.'.format(nota50, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 50 reais.'.format(nota50))
    elif nota50 == 0:
        if nota10 != 0:
            if nota5 != 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 10, {} notas de 5 e {} notas de 1 real.'.format(nota10, nota5, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 10 e {} notas de 5.'.format(nota10, nota5))
            elif nota5 == 0:
                if nota1 != 0:
                    print('você receberá: {} notas de 10 e {} notas de 1 real.'.format(nota10, nota1))
                elif nota1 == 0:
                    print('você receberá: {} notas de 10.'.format(nota100, nota10))       
