from random import randint

numero = randint(1, 100)
chutes = 0

while True:
    chute = int(input('digite um número: '))
    chutes += 1

    if chute == numero:
        print('você acertou, o número era {}.'.format(numero))
        print('você chutou {} vezes.'.format(chutes))
        break

    else:
        if chute < numero:
            print('chute mais alto.')

        elif chute > numero:
            print('chute mais baixo.')
        
