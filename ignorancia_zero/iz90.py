print('Projeção de Gastos com Abono')
print('============================')
print('')

sal = []

while True:
    salario = float(input('Salário: '))

    if salario != 0:
        sal += [salario]

    else:
        break

maior = 0
mini = 0
total = 0
abonos = []

for correçao in sal:
    abono = correçao/100*20

    if abono < 100:
        abono = 100

    if abono > maior:
        maior = abono

    if abono == 100:
        mini += 1
        
    total += abono
    abonos += [abono]

def formata(saida, grana, espaço):
    if len(str(grana)) < espaço:
        formatado = (espaço-len('{:.2f}'.format(grana)))*' ' + '{:.2f}'.format(grana)
    return formatado

print('')

print('Salário    - Abono')
for saidas in range(len(sal)):
    saida = ''
    saida += 'R$' + formata(saida, sal[saidas], 8)
    saida += ' - '
    saida += 'R$' + formata(saida, abonos[saidas], 8)
    print(saida)

print('')

print('Foram processados {} colaboradores.'.format(len(sal)))
print('Total gasto com abonos: R$ {:.2f}.'.format(total))
print('Valor mínimo pago a {} colaboradores.'.format(mini))
print('maior valor de abono pago: R$ {:.2f}.'.format(maior))
    
