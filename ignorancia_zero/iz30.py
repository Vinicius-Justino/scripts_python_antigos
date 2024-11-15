#DETERMINANDO OS VALORES
i = int(input('digite o primeiro número: '))
j = int(input('digite o segundo número: '))
n = int(input('digite o número de múltiplos: '))
cont = 0
mult = 0

while True:
    if cont == n:
        break
    
    if mult%i == 0 or mult%j == 0:
        print(mult)
        cont += 1

    mult += 1
