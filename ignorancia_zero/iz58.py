#recebendo a lista
print('monte sua lista, digite 0 quando estiver pronta.')
print('')

lista = []

while True:
    n = int(input('digite um número inteiro: '))

    if n != 0:
        lista += [n]
    else:
        break

#buscando o número
print('')
busca = int(input('digite o número que quer procurar: '))
print('')
print(lista)

erro = True

for buscas in range(len(lista)):
    if lista[buscas] == busca:
        print('o primeiro número {} está na posição {} dessa lista.'.format(busca, buscas+1))
        erro = False
        break

if erro == True:
    print('não tem nenhum número {} nessa lista.'.format(busca))
