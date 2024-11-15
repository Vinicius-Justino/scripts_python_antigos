#determinando n
n = input('digite um número: ')

while n.isnumeric() == False:
    print('')
    print('não é um valor válido, digite novamente.')
    n = input('digite um número: ')

n = int(n)
print('')

#determinando os triângulos
t1 = 0
t2 = 1
t3 = 2
total = 0

while True:
    t1 += 1
    t2 += 1
    t3 += 1
    total = t1*t2*t3

    print('{}x{}x{}={}'.format(t1, t2, t3, total))

    if total == n:
        print('')
        print('{} é um número triângulo.'.format(n))
        break

    elif total > n:
        print('')
        print('{} não é um número triângulo.'.format(n))
        break
    
