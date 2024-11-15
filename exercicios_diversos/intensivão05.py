p = input('digite um número: ')
q = input('digite um número maior ou igual ao anterior: ')

if p in q:
    print('{} é subnúmero de {}.'.format(p, q))
else:
    print('{} não é subnúmero de {}.'.format(p, q))
