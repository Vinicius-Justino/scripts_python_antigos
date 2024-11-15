print('digite 0 para interromper a sequência.')
print('')

temperatura = float(input('digite a temperatura 1: '))
maior = temperatura
menor = temperatura

aux = temperatura
media = 1
cont = 1

amostra_maior = cont
amostra_menor = cont

while temperatura != 0:
    cont += 1
    
    temperatura = float(input('digite a temperatura {}: '.format(cont)))

    if temperatura == 0:
        break

    elif temperatura > maior:
        maior = temperatura
        amostra_maior = cont

    elif temperatura < menor:
        menor = temperatura
        amostra_menor = cont

    media += 1
    aux += temperatura
    
print('')
print('a maior temperatura foi a {} com {}º.'.format(amostra_maior, maior))
print('a menor temperatura foi a {} com {}º.'.format(amostra_menor, menor))
print('a média de temperatura foi {:.1f}º.'.format(aux/media))
