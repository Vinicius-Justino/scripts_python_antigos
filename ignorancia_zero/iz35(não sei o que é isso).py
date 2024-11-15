a = float(input('digite o valor de A: '))

if a > 0:
    b = float(input('digite o valor de B: '))
    c = float(input('digite o valor de C: '))

    delta = b**2

    if delta >= 0:
        if delta == 0:
            print('essa equação possui a raiz real:')
            raiz = (-b + (delta**(1/2)))/(2*a)
            print(raiz)

        elif delta > 0:
            print('essa equação possui duas raizes reais:')
            raiz1 = (-b + (delta**(1/2)))/(2*a)
            raiz2 = (-b - (delta**(1/2)))/(2*a)
            print(raiz1)
            print(raiz2)

    else:
        print('essa equação não possui raiz real.')

else:
    print('essa equação não é de segundo grau.')
