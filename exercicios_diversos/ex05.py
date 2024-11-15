try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    print('\n{}:{} = {}'.format(a, b, a/b))
except:
    print('\nNão possível efetuar uma divisão.')
