def fatorial(numero1):
    while numero1 <= 1:
        print('não é um número válido,digite valores acima de 1.')
        numero1 = int(input('digite um número:'))

        if numero1 >= 2:
            break

    numero2 = numero1-1
    amostra = numero1

    print('{}*{}={}'.format(numero1, numero2, numero1*numero2))

    resultado = numero1*numero2

    while numero2 != 1:
        numero2 = numero2-1
        print('{}*{}={}'.format(resultado, numero2, resultado*numero2))
        resultado = resultado*numero2
        if numero2 == 1:
            break
    print('{}! = {}.'.format(amostra, resultado))

fatorial(5)
print('')
fatorial(10)
print('')
fatorial(4)
