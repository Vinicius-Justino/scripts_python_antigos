print('digite quantos números quiser.')
print('digite 0 para interromper a sequência.')
ant = 0
cont = 0
top = 0

while True:
    n = int(input('digite um número: '))

    if n == 0:
        break

    if n > ant:
        cont += 1
    elif n < ant:
        cont = 1

    if cont > top:
        top = cont

    ant = n

print('o maior segmento crescente foi', top)
