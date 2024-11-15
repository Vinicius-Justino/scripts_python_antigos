restos_faltando = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
restos = []
numeros = []
somas = []

n = 10

while restos_faltando != []:
    soma = int(str(n)[0]) + int(str(n)[1])
    resto = n%soma

    if resto == 11:
        print('Número:', n)
        print('Soma:', soma)
        print('Resto:', resto)

    if resto in restos_faltando:
        restos += [resto]
        numeros += [n]
        somas += [soma]

        restos_faltando.remove(resto)

    n += 1

for mostra in range(12):
    saida = str(numeros[mostra]) + ' % ' + ' '*(2-len(str(somas[mostra]))) + str(somas[mostra]) + ' = ' + ' '*(2-len(str(restos[mostra]))) + str(restos[mostra])
    print(saida)
