n = input('digite um número: ')

if '.' in n:
    n = float(n)
    print(n, 'é real.')
    d = n - int(n)

    if d >= 0.5:
        n = int(n)
        n += 1
        print('arredondamento:', n)
    else:
        n = float(n)
        print('arredondamento:', int(n))

else:
    n = int(n)
    print(n, 'é inteiro')
