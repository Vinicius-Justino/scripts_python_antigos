altura = float(input('digite sua altura: '))
print('')
print('masculino/feminino')
print('')
sexo = input('digite seu sexo: ')
print('')
peso = float(input('digite seu peso: '))

if sexo == 'masculino':
    ideal = (72.7*altura) - 58

elif sexo == 'feminino':
    ideal = (62.1*altura) - 44.7

print('peso:', peso)
print('ideal: {:.1f}'.format(ideal))

if peso > ideal:
    print('você está acima do peso.')

elif peso == ideal:
    print('você está no peso ideal.')

else:
    print('você está abaixo do peso.')
