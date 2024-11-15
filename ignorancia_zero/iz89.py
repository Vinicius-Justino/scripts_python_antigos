n = int(input('Fatorial de: '))

resultado = 1
numeros = []
for fatorial in range(1, n+1):
    resultado *= fatorial
    numeros += [fatorial]

numeros.reverse()

saida = ''
for formataçao in numeros:
    saida += str(formataçao)
    if formataçao != 1:
        saida += ' x '

print('{}! = {} = {}'.format(n, saida, resultado))
