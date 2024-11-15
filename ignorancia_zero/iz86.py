#montado as fichas
while True:
    media = 0
    saltos = []
    atleta = input('Atleta: ')

    if atleta == '':
        break
    
    print('')

    #perguntando de um jeito chique ~UwU~
    for s in range(5):
        if s == 0:
            salto = input('Primeiro salto: ')

        elif s == 1:
            salto = input('Segundo salto: ')

        elif s == 2:
            salto = input('Terceiro salto: ')

        elif s == 3:
            salto = input('Quarto salto: ')

        elif s == 4:
            salto = input('Quinto salto: ')

        saltos += [salto]
        media += float(salto)

    #tratando a saída
    saida = 'Saltos: '
    for t in range(5):
        saida += saltos[t]
        if t != 4:
            saida += ' - '

    print('')
    print('Resultado final:')
    print('Atleta:', atleta)
    print(saida)
    print('Média dos saltos: {} m'.format(media/5))
    print('')
    print('')
    
    
