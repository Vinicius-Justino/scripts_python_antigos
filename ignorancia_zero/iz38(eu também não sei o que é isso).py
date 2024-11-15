x = float(input('digite um número real: '))
n = int(input('digite um número inteiro: '))

a = 1
b = 2

k = 2

cos_x = 1/1

cont = 0

while cont < n:
    #a
    aux_a = a*k
    aux_aux_a = aux_a
    fat1 = 0
    fat1 = aux_a*(aux_a-1)
    aux_a -= 1
    #b
    aux_b = b*k
    aux_aux_b = aux_b
    cont_b = 0
    fat2 = aux_b*(aux_b-1)
    aux_b -= 1
    #a
    while aux_a != 1:
        aux_fat = aux_a - 1
        fat1 = fat1*aux_fat
        aux_a -= 1
    #b
    while aux_b != 1:
        aux_fat = aux_b - 1
        fat2 = fat2*aux_fat
        aux_b -= 1

    print('{} - ({}**{})/{} + ({}**{})/{}'.format(cos_x, x, aux_aux_a, fat1, x, aux_aux_b, fat2))
    cos_x += -(x**aux_aux_a)/fat1 + (x**aux_aux_b)/fat2

    a += 2
    b += 2

    cont += 1
