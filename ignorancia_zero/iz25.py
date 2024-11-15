s = int(input('digite o número de sequências: '))

for sequencia in range(s):   #para cada sequência loop isso:
    print('')
    print('sequência {}:'.format(sequencia+1))
    print('')
    soma = 0   #soma zera a cada sequência
    while True:   #para cada número da sequência loop isso:
        n = int(input('digite o número {}: '.format(numeros+1)))

        if n == 0:
            break

        if n%2 == 0:
            soma += n

    print('a soma dos pares dessa sequência é', soma)
