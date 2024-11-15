from random import choice
from random import randint

#montando o jogo
aposta = []
for escolhendo in range(1, 7):
    while True:
        erro = False
    
        n = int(input('digite o {}º número do seu jogo: '.format(escolhendo)))

        for cheatproof in range(len(aposta)):
            if aposta[cheatproof] == n:
                erro = True
                break

        if erro == False and 0 < n <= 60:
            aposta += [n]
            break

        else:
            print('número inválido, digite novamente.')
            print('')

saldo = 100
for jogos in range(50063860):
    saldo -= 2.5

    quinas = 0
    quadras = 0
    
    #determinando o valor de cada prêmio
    premio = randint(15, 70)
    premio *= 100000

    aux_quina = randint(1, 4)
    aux_quadra = randint(3, 5)

    aux_quina /= 10
    aux_quadra *= 1000

    premio_quina = premio/100*aux_quina
    premio_quadra = premio*(1/aux_quadra)
    premio_vitoria = premio/100*94

    premio_quadra = int(premio_quadra)
    
    #sorteando
    possibilidades = list(range(1, 61))
    premiado = []

    for correto in range(6):
        certo = choice(possibilidades)
        premiado += [certo]
        possibilidades.remove(certo)

    aposta.sort()
    premiado.sort()

    for quina in range(6):
        if aposta[quina] == premiado[quina]:
            quinas += 1

    for quadra in range(6):
        if aposta[quadra] == premiado[quadra]:
            quadras += 1

    #premiando o usuário      
    if aposta == premiado:
        saldo += premio_vitoria

    elif quinas == 5:
        saldo += premio_quina

    elif quadras == 4:
        saldo += premio_quadra

print('')
print('você terminou as apostas com um saldo total de {} reais.'.format(saldo))
