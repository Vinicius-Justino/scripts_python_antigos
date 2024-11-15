lado1 = int(input('digite um número: '))
lado2 = int(input('digite outro número: '))
lado3 = int(input('digite mais um número: '))

if lado1**2 + lado2**2 == lado3**2 or lado1**2 + lado3**2 == lado2**2 or lado2**2 + lado3**2 == lado1**2:
    print('{}, {} e {} são lados de um triângulo retângulo.'.format(lado1, lado2, lado3))

else:
    print('{}, {} e {} não são lados de um triângulo retângulo.'.format(lado1, lado2, lado3))
