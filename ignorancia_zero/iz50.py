contagem = 0
votos = []

while True:
    voto = int(input('digite o número da camisa do jogador: '))

    if voto == 0:
        break
    elif 1 <= voto <= 23:
        contagem += 1
        votos += [voto]

if contagem != 0:
    print('')
    print('total de votos:', contagem)
    print('')

    for jogadores in range(1, 24):
        cont = votos.count(jogadores)

        if cont != 0:
            print('o jogador {} recebeu {} votos.'.format(jogadores, cont))

    print('')

    for percentuais in range(1, 24):
        if votos.count(percentuais) != 0:
            porcentagem = 100*votos.count(percentuais)/contagem
            print('o jogador {} recebeu {:.1f}% dos votos.'.format(percentuais, porcentagem))

    print('')

    melhor = 0
    mcont = 0

    for melhores in range(1, 24):
        cont = votos.count(melhores)
        if cont > mcont:
            melhor = melhores
            mcont = cont

    print('o jogador {} venceu com {} votos ou {:.1f}%!'.format(melhor, votos.count(melhor), 100*votos.count(melhor)/contagem))
