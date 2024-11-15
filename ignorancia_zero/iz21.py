numero1 = int(input('Digite um número:'))
while numero1 <= 1:
    print('não é um número válido,digite valores acima de 1.')
    numero1 = int(input('digite um número:'))
    if numero1 >= 2:
        break
numero2 = numero1-1
amostra = numero1
print('{}*{}={}'.format(numero1, numero2, numero1*numero2))
resultado = numero1*numero2
numero2 = numero1-1
for fatorial in range(numero2+1):
    numero2 = numero2-1
    print('{}*{}={}'.format(resultado, numero2, resultado*numero2))
    resultado = resultado*numero2
    if numero2 == 1:
        break
print('{}! = {}.'.format(amostra, resultado))
