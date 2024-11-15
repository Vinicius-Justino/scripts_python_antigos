import random as r

#inimigos
inimigos = int(input('digite o número de inimigos: '))
exercito = []

for recrutamento in range(1, inimigos+1):
    exercito += [recrutamento]
    exercito[recrutamento-1] = 50

print('')

#player
vida = 500
sp = 100

#jogo
while vida > 0:
    #SEU TURNO
    print('Vida:', vida)
    print('SP:', sp)
    print('atacar(1)   curar(2)')

    açao = int(input('digite sua ação: '))

    #ataque
    if açao == 1:
        dano = r.randint(10, 15)

        alvo = r.randint(1, len(exercito))
        while exercito[alvo-1] <= 0:
            alvo = r.randint(1, len(exercito))

        exercito[alvo-1] -= dano
        print('causou {} dano ao inimigo {}!'.format(dano, alvo))
        if exercito[alvo-1] <= 0:
            print('inimigo {} morreu.'.format(alvo))
        print('')

    #cura
    if açao == 2:
        if sp >= 10:
            cura = r.randint(10, 15)

            if vida + cura > 500:
                sp -= 10
                print('curou {} de vida!'.format(cura))
                vida = 500
                print('')

            elif vida + cura <= 500:
                sp -= 10
                print('curou {} de vida'.format(cura))
                vida += cura
                print('')

        else:
            print('não pode se curar com menos de 10 SP.')
            print('')

    #TURNO DO INIMIGO
    for ataques in range(len(exercito)):
        if exercito[ataques] > 0:
            chance = r.randint(1, 4)
            if chance != 1:
                dano = r.randint(1, 3)
                print('inimigo {} deu {} de dano!'.format(ataques+1, dano))
                vida -= dano

            else:
                print('inimigo {} errou!'.format(ataques+1))

    print('')

    if sp + 3 <= 100:
        sp += 3
    else:
        sp = 100

    cont = 0
    for mortos in range(len(exercito)):
        if exercito[mortos] <= 0:
            cont += 1

    if cont == inimigos:
        break

if cont == inimigos:
    print('você ganhou!')

else:
    print('você perdeu.')
