lista = []
for notas in range (1, 5):
    nota = float(input('digite a {}ª nota: '.format(notas)))
    lista += [nota]

n1 = lista[0]
n2 = lista[1]
n3 = lista[2]
n4 = lista[3]

print('')
print('nota do primeiro bimestre: {}'.format(n1))
print('nota do segundo bimestre: {}'.format(n2))
print('nota do terceiro bimestre: {}'.format(n3))
print('nota do quarto bimestre: {}'.format(n4))
print('média do aluno: {:.1f}'.format((n1 + n2 + n3 + n4)/4))
