while True:
    import random

    aceitavel = False
    palpite = 0000
    nums_palpite = []
    secretnum = 0000
    nums_secretnum = []

    def recebePalpite():
        global palpite, nums_palpite

        palpite = int(input('Digite o seu palpite: '))

        aux = palpite
        
        for gerandoLista in range(4):
            n = aux%10
            nums_palpite += [n]
            aux //= 10

        nums_palpite.reverse()
            
    def analisaPalpite():
        global aceitavel
        if len(nums_palpite) == 4:
            aceitavel = True

        else:
            aceitavel = False

        return aceitavel

    def geraSecretnum():
        global secretnum, nums_secretnum
        
        opçoes = list(range(10))

        for GerandoSecretNum in range(4):
            n = random.choice(opçoes)
            nums_secretnum += [n]
            opçoes.remove(n)

        a = str(nums_secretnum[0])
        b = str(nums_secretnum[1])
        c = str(nums_secretnum[2])
        d = str(nums_secretnum[3])

        secretnum = int(a + b + c + d)

        if nums_secretnum[0] == 0:
            geraSecretnum()

    def geraDicas():
        dicas = []

        for num1 in range(4):
            for num2 in range(4):
                if nums_palpite[num1] == nums_secretnum[num2]:
                    if num1 == num2:
                        dicas += ['Fermi']

                    else:
                        dicas += ['Pico']

        if dicas != []:
            for dica in dicas:
                print(dica, end=' ')

        else:
            print('Bagels')

    def main():
        global secretnum, aceitavel, nums_secretnum, nums_palpite
        print('                       ~ BAGELS ~                          ')
        print('                                                           ')
        print('--> O computador sorteará um número de 4 dígitos.          ')
        print('--> Todos os dígitos desse número serão diferentes.        ')
        print('--> Você tem 10 chances para adivinhar esse número.        ')
        print('                                                           ')
        print('                                                           ')
        print('                      MODO DE JOGAR:                       ')
        print('                                                           ')
        print('Digite um número de 4 dígitos e preste atenção nas dicas:  ')
        print('                                                           ')
        print('   Pico --> Um dos dígitos nesse número aparece no número  ')
        print('            sorteado, mas em outra posição.                ')
        print('                                                           ')
        print('  Fermi --> Um dos dígitos nesse número aparece no número  ')
        print('            sorteado, e na mesma posição.                  ')
        print('                                                           ')
        print(' Bagels --> Nenhum dos dígitos nesse número aparece no     ')
        print('            número sorteado.                               ')
        print('                                                           ')
        print('podem haver múltiplos dígitos corretos no mesmo número,    ')
        print('nesse caso, a quantidade de cada Pico e cada Fermi indica  ')
        print('quantos estão na posição correta e quantos estão na errada.')
        print('                                                           ', end='')
        geraSecretnum()

        cont = 0
        for tentativas in range(10):
            print('\nTentativas: {}'.format(10-tentativas))
            nums_palpite = []
            while True:
                recebePalpite()
                analisaPalpite()

                if aceitavel == True:
                    break

                else:
                    print('digite números de 4 dígitos.')
                    print('')
                    nums_palpite = []

            if palpite == secretnum:
                print('')
                break

            else:
                geraDicas()
                print('')

            cont += 1

        if cont < 10:
            print('parabéns, você ganhou ☺!, o número era {}.'.format(secretnum))
                
        else:
            print('infelizmente você perdeu, o número era {}.'.format(secretnum))

    main()
    print('')
    print('')
                        
