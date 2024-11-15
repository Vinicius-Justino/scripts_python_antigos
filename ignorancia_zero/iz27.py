m = int(input('quer ver cubos até onde? R: '))
impar = 1
for cubos in range(1, m+1):
    cont = 0
    cubo = 0
    while cont < cubos:
        cubo += impar
        impar += 2
        cont += 1
    print('{}**3={}'.format(cubos, cubo))
