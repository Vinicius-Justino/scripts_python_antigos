n = int(input('digite um número para ver a sau tabuada: '))

print('\n------------')
for tabuada in range(1, 11):
    saida = str(n) + ' x ' + ' '*(2-len(str(tabuada))) + str(tabuada) + ' = ' + str(n*tabuada)
    print(saida)
print('-------------')    
    
