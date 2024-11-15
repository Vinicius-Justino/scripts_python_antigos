while True:
#IMPORTAÇÃO
    from random import randint

#USUÁRIO
    nome = input('escolha seu nome: ')

#OPERAÇÃO
    print('')
    print('--OPERAÇÕES--')
    print('')
    print('+ = adição')
    print('- = subtração')
    print('* = multiplicação')

    print('')
    operaçao = input('escolha sua operação: ')

    while operaçao != '+':
        if operaçao == '+':
            print('adição')
            break
        elif operaçao == '-':
            print('subtração')
            break
        elif operaçao == '*':
            print('multiplicação')
            break
        else:
            print('')
            print('não entendo como uma operação, digite apenas sinais que estão na lista.')
            operaçao = input('escolha sua operação: ')

#PARTIDAS
    print('')
    rodadas = int(input('escolha quantas contas vai fazer: '))

    while rodadas < 2:
        print('')
        print('mínimo 2 rodadas')
        rodadas = int(input('escolhas quantas contas vai fazer: '))

#FUNÇÃO PARA CONTAS
    def conta():
        global pontos
        if operaçao == '+':
            resposta = int(input('{}+{}= '.format(n1, n2)))
            print('{}+{}={}'.format(n1, n2, n1+n2))
            if resposta == n1+n2:
                print('você acertou')
                print('')
                pontos += 1
            else:
                print('você errou.')
                print('')

        elif operaçao == '-':
            resposta = int(input('{}-{}= '.format(n1, n2)))
            print('{}-{}={}'.format(n1, n2, n1-n2))
            if resposta == n1-n2:
                print('você acertou!')
                print('')
                pontos += 1
            else:
                print('você errou.')

        elif operaçao == '*':
            resposta = int(input('{}x{}= '.format(n1, n2)))
            print('{}x{}={}'.format(n1, n2, n1*n2))
            if resposta == n1*n2:
                print('você acertou')
                print('')
                pontos += 1
            else:
                print('você errou')

#JOGO
    erros = 3
    fases = 0
    print('----START!---')

#FASE 1
    while True:
        print('')
        print('FASE 1')
        print('')

        pontos = 0

        for fase1 in range(rodadas):
            n1 = randint(1, 10)
            n2 = randint(1, 10)

            conta()

        if rodadas%2 != 0:
            if pontos > (rodadas//2+1):
                print('parabéns {}! Você concluiu a fase 1 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1           
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))

        elif rodadas%2 == 0:
            if pontos > rodadas//2:
                print('parabéns {}! Você concluiu a fase 1 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1 
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))
            
#FASE 2
    while True:
        if erros == 0:
            break
        
        print('')
        print('FASE 2')
        print('')

        pontos = 0

        for fase2 in range(rodadas):
            n1 = randint(10, 30)
            n2 = randint(10, 30)

            conta()

        if rodadas%2 != 0:
            if pontos > (rodadas//2+1):
                print('parabéns {}! Você concluiu a fase 2 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1           
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))

        elif rodadas%2 == 0:
            if pontos > rodadas//2:
                print('parabéns {}! Você concluiu a fase 2 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1 
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))

#FASE 3
    while True:
        if erros == 0:
            break
        
        print('')
        print('FASE 3')
        print('')

        pontos = 0

        for fase3 in range(rodadas):
            n1 = randint(30, 50)
            n2 = randint(30, 50)

            conta()

        if rodadas%2 != 0:
            if pontos > (rodadas//2+1):
                print('parabéns {}! Você concluiu a fase 3 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1           
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))

        elif rodadas%2 == 0:
            if pontos > rodadas//2:
                print('parabéns {}! Você concluiu a fase 3 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1 
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))
            
#FASE 4
    while True:
        if erros == 0:
            break
        
        print('')
        print('FASE 4')
        print('')

        pontos = 0

        for fase4 in range(rodadas):
            n1 = randint(60, 100)
            n2 = randint(60, 100)

            conta()

        if rodadas%2 != 0:
            if pontos > (rodadas//2+1):
                print('parabéns {}! Você concluiu a fase 4 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1           
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))

        elif rodadas%2 == 0:
            if pontos > rodadas//2:
                print('parabéns {}! Você concluiu a fase 4 com uma pontuação de {}/{}.'.format(nome, pontos, rodadas))
                fases += 1
                break
            else:
                print('infelizmente você não atingiu a meta de acertos, tente novamente. {}/{}.'.format(pontos, rodadas))
                erros -= 1 
                if erros == 0:
                    break
                elif erros == 1:
                    print('você pode falhar mais 1 vez.')
                else:
                    print('você pode falhar mais {} vezes.'.format(erros))

    if erros == 3 and fases == 4:
        print('')
        print(' _________   ________   _________   ________   ________        __      ___        _     ___      _  ')
        print('|  _____  | |  ____  | |  _____  | |  ____  | |  ____  \      /_/     |   \      | |   / _ \    | | ') 
        print('| |     | | | |    | | | |     | | | |    | | | |    \  |  _________  | |\ \     | |  / / \ \   | | ')
        print('| |     | | | |    | | | |     | | | |    | | | |____/  | |  _______| | | \ \    | |  \ \ |_|   | | ')
        print('| |_____| | | |    | | | |_____| | | |    | | |  ____  /  | |______   | |  \ \   | |   \ \      | | ')
        print('|  _______| | |____| | |  __  ___| | |____| | | |    \ \  |  ______|  | |   \ \  | |  _ \ \     | | ')
        print('| |         |  ____  | | |  \ \    |  ____  | | |     | | | |         | |    \ \ | | | | \ \    |_| ')
        print('| |         | |    | | | |   \ \   | |    | | | |____/  | | |_______  | |     \ \| | \ \_/ /     _  ')
        print('|_|         |_|    |_| |_|    \_\  |_|    |_| |________/  |_________| |_|      \___|  \___/     |_| ')
        print('')
        print('parabéns {}! Você completou todos os desafios sem falhar nenhuma vez!'.format(nome))

    elif erros == 0:
        print('você não conseguiu cumprir os desafios. Tente novamente.')

    else:
        print('')
        print('parabés {}! Você completou {} desafios.'.format(nome, fases))
        
    print('')
    print('quer jogar de novo? (sim/não)')
    loop = input('R: ')

    while loop != 'sim' and loop != 'não':
        print('')
        print('não entendo como uma resposta, digite as palavras exatamente como estão abaixo:')
        print('sim/não')
        loop = input('quer jogar de novo? R: ')
        
    if loop == 'sim':
        print('')
        print('============================================================================================================================')
        print('')

    elif loop == 'não':
        break
