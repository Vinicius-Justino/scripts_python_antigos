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

#recebendo o número
print('')
print(lista)
print('')

est = int(input('digite o número que deseja acrescentar a essa lista: '))
p = int(input('digite a posição desejada: '))
cont = 0

#inserindo o número na lista
if p < len(lista):
    sub1 = lista[p]
    sub2 = sub1

    lista[p] = est

    cont += 1

    #arrumando a lista
    while p + cont < len(lista):
        sub1 = sub2                #número que vai ser substituido
        sub2 = lista[p + cont]    #número que vai substituir

        lista[p + cont] = sub1         #substituição

        cont += 1

    lista += [sub2]

else:
    lista += [est]

print(lista)
