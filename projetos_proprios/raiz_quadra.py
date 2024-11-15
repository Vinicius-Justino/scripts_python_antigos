#DETERMINA ATÉ QUE NÚMERO IMPRIMIMOS RAÍZES
s = int(input('quer ver raízes até qual número? R:'))
n = 0

#VERIFICAMOS SE O NÚMERO TEM CASAS DECIMAIS
while n <= s:
    r = n**(1/2)
    r = str(r)
    c = 0
    cont = 0
    if '.0' in r:

        #VERFICAMOS SE ESSAS CASAS SÃO TODAS 0
        while True:
            c = str(c)
            d = '.0' + c
            if d in r:
                break
            cont += 1
            c = int(c)
            c += 1
            if cont == 10:
                print(n, '-->', n**(1/2))
                break

    n += 1
