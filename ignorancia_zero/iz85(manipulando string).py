x = 1
while int(x) > 0:
    a = ''
    b = ''
    c = ''
    
    x = input('digite um número menor que 1000: ')
    if int(x) <= 0:
        break
    
    aux = list(x)

    #NÚMEROS COM 3 DÍGITOS
    if len(aux) == 3:
        for textos in range(len(aux)):
            #centenas
            if textos == 0:
                    if int(aux[textos]) > 1:
                        a = 'centenas'
                    elif int(aux[textos]) == 1:
                        a = 'centena'
            #dezenas
            elif textos == 1:
                    if int(aux[textos]) > 1:
                        b = 'dezenas'
                    elif int(aux[textos]) == 1:
                        b = 'dezena'
            #unidades
            elif textos == 2:
                if int(aux[textos]) > 1:
                    c = 'unidades'
                elif int(aux[textos]) == 1:
                    c = 'unidade'

        #TEXTO FORMATADO
        #dezenas, centenas e unidades
        if a != '' and b != '' and c != '':
            print('{} = {} {}, {} {} e {} {}'.format(x, aux[0], a, aux[1], b, aux[2], c))

        #centenas e unidades
        if a != '' and b == '' and c != '':
            print('{} = {} {} e {} {}'.format(x, aux[0], a, aux[2], c))

        #centenas e dezenas
        if a != '' and b != '' and c == '':
            print('{} = {} {} e {} {}'.format(x, aux[0], a, aux[1], b))

        #só centenas
        if a != '' and b == '' and c == '':
            print('{} = {} {}'.format(x, aux[0], a))

    #NÚMEROS COM 2 DÍGITOS
    if len(aux) == 2:
        for textos in range(len(aux)):
            #dezenas
            if textos == 0:
                    if int(aux[textos]) > 1:
                        a = 'dezenas'
                    elif int(aux[textos]) == 1:
                        a = 'dezena'
            #unidades
            elif textos == 1:
                if int(aux[textos]) > 1:
                    b = 'unidades'
                elif int(aux[textos]) == 1:
                    b = 'unidade'

        #TEXTO FORMATADO
        #dezenas e unidades
        if a != '' and b != '':
            print('{} = {} {} e {} {}'.format(x, aux[0], a, aux[1], b))

        #só unidades
        if a == '' and b != '':
            print('{} = {} {}'.format(x, aux[1], b))

        #só dezenas
        if a != '' and b == '':
            print('{} = {} {}'.format(x, aux[0], a))

    #NÚMEROS COM 1 DÍGITO
    if len(aux) == 1:
        if int(x) > 1:
            print('{} = {} unidades'.format(x, x))

        else:
            print('1 = 1 unidade')

    print('')
