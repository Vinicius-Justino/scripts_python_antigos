#MATURIDADE HARDCORE
print('    ELEIÇÕES')
print('vote 11 para eleger o candidato Kemel P. Junior.')
print('vote 26 para eleger o candidato Melo R. de Barros. ')
print('vote 34 para eleger o candidato Jacinto L. A. Rêgo.')
print('')
candidato1 = 0
candidato2 = 0
candidato3 = 0

#ELEITORES
eleitores = int(input('quantas pessoas vão votar? R: '))

#ELEIÇÕES
for eleiçoes in range(eleitores):
    voto = int(input('digite o número do seu candidato: '))

    if voto == 11:
        candidato1 += 1

    elif voto == 26:
        candidato2 += 1

    elif voto == 34:
        candidato3 += 1

print('canditado1 =', candidato1)
print('candidato2 =', candidato2)
print('candidato3 =', candidato3)

#APURAÇÃO DOS VOTOS
if candidato1 > candidato2 and candidato1 > candidato3:
    print('candidato 1 ganhou.')

elif candidato2 > candidato1 and candidato2 > candidato3:
    print('candidato 2 ganhou.')

elif candidato3 > candidato2 and candidato3 > candidato1:
    print('candidato 3 ganhou.')

elif candidato1 < candidato2 or candidato1 < candidato3:
    if candidato1 > candidato2 and candidato1 < candidato3:
        print('candidato 3 ganhou.')

    elif candidato1 < candidato2 and candidato1 > candidato3:
        print('candidato 2 ganhou.')

    elif candidato1 < candidato2 and candidato1 < candidato3:
        if candidato2 > candidato3:
            print('candidato 2 ganhou.')

        elif candidato2 < candidato3:
            print('candidato 3 ganhou.')

        else:
            print('empate.')

    else:
        print('empate.')

else:
    print('empate.')


