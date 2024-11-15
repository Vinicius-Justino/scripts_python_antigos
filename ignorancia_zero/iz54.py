idades = []
alturas = []

sedadi = []
sarutla = []

for dados in range(1, 6):
    idade = int(input('digite a idade da pessoa {}: '.format(dados)))
    altura = float(input('digite a altura da pessoa {}: '.format(dados)))
    print('')
    
    idades += [idade]
    alturas += [altura]

magica = len(idades) - 1

while magica != -1:
    sedadi += [idades[magica]]
    sarutla += [alturas[magica]]

    magica -= 1

print('idades:')
print(sedadi)
print('')
print('alturas:')
print(sarutla)
