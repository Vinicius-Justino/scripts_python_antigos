def notas():
    n = input('nota:')
    while n.isnumeric() == False:
        print('não é uma nota válida, digite novamente.')
        n = input('nota:')
        if n.isnumeric() == True:
            break
    n = float(n1)
    while n < 0:
        print('não é uma nota válida, digite novamente.')
        n = float(input('nota:'))
        if n >= 0:
            if n <= 10:
                break
            else:
                print('não é uma nota válida, digite novamente.')
                n = float(input('nota:'))
        else:
            print('não é uma nota válida, digite novamente.')
            n = float(input('nota:'))
    while n > 10:
        print('não é uma nota válida, digite novamente.')
        n = float(input('nota:'))
        if n <= 10:
            if n >= 0:
                break
            else:
                print('não é uma nota válida, digite novamente.')
                n = float(input('nota:'))
        else:
            print('não é uma nota válida, digite novamente.')
            n = float(input('nota:'))
#PRIMEIRA NOTA
n1 = notas()
#SEGUNDA NOTA
n2 = notas()
#TERCEIRA NOTA
n3 = notas()
#QUARTA NOTA
n4 = notas()
