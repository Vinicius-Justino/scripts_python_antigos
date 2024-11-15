n = 1
lista = []

while n != 0:
    n = int(input('isso vai demorar: '))
    lista += [n]

impar = []    
for impares in lista:
    if impares%2 == 0:
        continue

    impar += [impares]

print('')
print(impar)
