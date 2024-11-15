tamanho = int(input('digite a quantidade de números na sequência: '))
print('')
lista = []

for lolp in range(1, tamanho+1):
    vetor = int(input('digite o {}º número: '.format(lolp)))

    for testes in range(len(lista)):
        if lista[testes] == vetor:
            lista.remove(vetor)

    lista += [vetor]

print('')
print(lista)
