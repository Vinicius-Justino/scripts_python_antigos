atleta = input('Atleta: ')
print('')

notas = []
maior = 0
menor = 10
media = 0
for apresentaçoes in range(1, 8):
    nota = float(input('{}ª nota: '.format(apresentaçoes)))

    notas += [nota]

    if nota > maior:
        maior = nota

    if nota < menor:
        menor = nota

notas.remove(maior)
notas.remove(menor)

for m in range(5):
    media += notas[m]

media /= 5

print('\nAtleta: {}\nMelhor nota: {}\nPior nota: {}\nMédia: {:.2f}\n\n'.format(atleta, maior, menor, media))
