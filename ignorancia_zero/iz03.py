#PRIMEIRA NOTA
n1 = input('nota do primeiro bimestre:')
while n1.isnumeric() == False:
    if n1.isnumeric() == False:
        if '.' in n1:
            if n1.islower() == False:
                if n1.isupper() == False:
                    if n1.istitle() == False:
                        break
    else:
        print('não é uma nota válida, digite novamente.')
        n1 = input('nota do primeiro bimestre:')
n1 = float(n1)
while n1 < 0:
    print('não é uma nota válida, digite novamente.')
    n1 = float(input('nota do primeiro bimestre:'))
    if n1 >= 0:
        if n1 <= 10:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n1 = float(input('nota do primeiro bimestre:'))
    else:
        print('não é uma nota válida, digite novamente.')
        n1 = float(input('nota do primeiro bimestre:'))
while n1 > 10:
    print('não é uma nota válida, digite novamente.')
    n1 = float(input('nota do primeiro bimestre:'))
    if n1 <= 10:
        if n1 >= 0:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n1 = float(input('nota do primeiro bimestre'))
    else:
        print('não é uma nota válida, digite novamente.')
        n1 = float(input('nota do primeiro bimestre'))
#SEGUNDA NOTA
n2 = input('nota do segundo bimestre:')
while n2.isnumeric() == False:
    if n2.isnumeric() == False:
        if '.' in n2:
            if n2.islower() == False:
                if n2.isupper() == False:
                    if n2.istitle() == False:
                        break
    else:
        print('não é uma nota válida, digite novamente.')
        n2 = input('nota do segundo bimestre:')
n2 = float(n2)
while n2 < 0:
    print('não é uma nota válida, digite novamente.')
    n2 = float(input('nota do segundo bimestre:'))
    if n2 >= 0:
        if n2 <= 10:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n2 = float(input('nota do segundo bimestre:'))
    else:
        print('não é uma nota válida, digite novamente.')
        n2 = float(input('nota do segundo bimestre:'))
while n2 > 10:
    print('não é uma nota válida, digite novamente.')
    n2 = float(input('nota do segundo bimestre:'))
    if n2 <= 10:
        if n2 >= 0:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n2 = float(input('nota do segundo bimestre'))
    else:
        print('não é uma nota válida, digite novamente.')
        n2 = float(input('nota do segundo bimestre'))
#TERCEIRA NOTA
n3 = input('nota do terceiro bimestre:')
while n3.isnumeric() == False:
    if n3.isnumeric() == False:
        if '.' in n3:
            if n3.islower() == False:
                if n3.isupper() == False:
                    if n3.istitle() == False:
                        break
    else:
        print('não é uma nota válida, digite novamente.')
        n3 = input('nota do terceiro bimestre:')
n3 = float(n3)
while n3 < 0:
    print('não é uma nota válida, digite novamente.')
    n3 = float(input('nota do terceiro bimestre:'))
    if n3 >= 0:
        if n3 <= 10:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n3 = float(input('nota do terceiro bimestre:'))
    else:
        print('não é uma nota válida, digite novamente.')
        n3 = float(input('nota do terceiro bimestre:'))
while n3 > 10:
    print('não é uma nota válida, digite novamente.')
    n3 = float(input('nota do terceiro bimestre:'))
    if n3 <= 10:
        if n3 >= 0:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n3 = float(input('nota do terceiro bimestre'))
    else:
        print('não é uma nota válida, digite novamente.')
        n3 = float(input('nota do terceiro bimestre'))
#QUARTA NOTA
n4 = input('nota do quarto bimestre:')
while n4.isnumeric() == False:
    if n4.isnumeric() == False:
        if '.' in n4:
            if n4.islower() == False:
                if n4.isupper() == False:
                    if n4.istitle() == False:
                        break
    else:
        print('não é uma nota válida, digite novamente.')
        n4 = input('nota do quarto bimestre:')
n4 = float(n4)
while n4 < 0:
    print('não é uma nota válida, digite novamente.')
    n4 = float(input('nota do quarto bimestre:'))
    if n4 >= 0:
        if n4 <= 10:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n4 = float(input('nota do quarto bimestre:'))
    else:
        print('não é uma nota válida, digite novamente.')
        n4 = float(input('nota do quarto bimestre:'))
while n4 > 10:
    print('não é uma nota válida, digite novamente.')
    n4 = float(input('nota do quarto bimestre:'))
    if n4 <= 10:
        if n4 >= 0:
            break
        else:
            print('não é uma nota válida, digite novamente.')
            n4 = float(input('nota do quarto bimestre'))
    else:
        print('não é uma nota válida, digite novamente.')
        n4 = float(input('nota do quarto bimestre'))
print('a média entre {}, {}, {} e {} é {}'.format(n1, n2, n3, n4, (n1+n2+n3+n4)/4))
