#criando as listas
lista = []
menor_7 = []
maior_media = []
soma = 0

#recebendo os número
n = float(input('digite o 1º número: '))
if n != -1:
    lista += [n]

    if n < 7:
        menor_7 += [n]

    soma += n

while n != -1:
    n = float(input('digite o {}º número: '.format(len(lista)+1)))

    if n == -1:
        break

    lista += [n]

    if n < 7:
        menor_7 += [n]

    soma += n

for testes in lista:
    if testes > soma/len(lista):
        maior_media += [testes]

#separando
print('todos os valores:')
print(lista)
print('')
print('ao contrário:')
print(lista[::-1])
print('')
print('soma:')
print(soma)
print('média:')
print('{:.1f}'.format(soma/len(lista)))
print('')
print('maiores que a média:')
print(maior_media)
print('')
print('menores que 7:')
print(menor_7)
print('')
print('mensagem.')
