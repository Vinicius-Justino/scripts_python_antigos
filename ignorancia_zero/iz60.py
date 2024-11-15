#recebendo a lista
print('monte sua lista, digite 0 quando estiver pronta.')
print('')

lista = []
organizada = []

n = int(input('digite um número inteiro: '))

lista += [n]
organizada += [n]

while True:
    n = int(input('digite um número inteiro: '))

    if n != 0:
        lista += [n]

        maior = True

        for ordem in range(len(organizada)):
            if n <= organizada[ordem]:
                organizada.insert(ordem, n)
                maior = False
                break

        if maior:
            organizada += [n]
    else:
        break

print('')
print('lista antes:', lista)
print('lista depois:', organizada)
