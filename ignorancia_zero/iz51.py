notas = []
for alunos in range(1, 11):
    media = 0
    print('')
    print('aluno {}:'.format(alunos))
    print('')
    for provas in range(1, 5):
        nota = float(input('digite a {}ª nota: '.format(provas)))
        media += nota
    media /= 4
    notas += [media]

print('')

cont = 0
for avaliaçao in notas:
    if avaliaçao >= 7:
        cont += 1

print(cont, 'alunos tiraram notas maiores ou iguais a 7.')
