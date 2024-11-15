while True:
    #ESCOLHENDO O NÚMERO
    numero = input('digite um número  menor que 1000: ')

    while numero.isnumeric() == False:
        print('esse não é um valor válido, digite novamente.')
        numero = input('digite um número menor que 1000: ')

    numero = int(numero)
    
    while numero >= 1000:
        print('esse não é um valor válido, digite novamente.')
        numero = input('digite um número menor 1000: ') 
        if numero.isnumeric() == True:
            numero = int(numero)
            if numero < 1000:
                break

    #SEPARANDO
    centenas = numero//100
    resto_centenas = numero%100

    dezenas = resto_centenas//10
    resto_dezenas = resto_centenas%10

    unidades = resto_dezenas//1

    #MOSTRANDO NA TELA
    if centenas >= 2:
        if dezenas >= 2:
            if unidades >= 2:
                print('{} tem: {} centenas, {} dezenas e {} unidades.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 1:
                print('{} tem: {} centenas, {} dezenas e {} unidade.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 0:
                print('{} tem: {} centenas e {} dezenas.'.format(numero, centenas, dezenas))
        elif dezenas == 1:
            if unidades >= 2:
                print('{} tem: {} centenas, {} dezena e {} unidades.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 1:
                print('{} tem: {} centenas, {} dezena e {} unidade.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 0:
                print('{} tem: {} centenas e {} dezena.'.format(numero, centenas, dezenas))
        elif dezenas == 0:
            if unidades >= 2:
                print('{} tem: {} centenas e {} unidades.'.format(numero, centenas, unidades))
            elif unidades == 1:
                print('{} tem: {} centenas e {} unidade.'.format(numero, centenas, unidades))
            elif unidades == 0:
                print('{} tem: {} centenas.'.format(numero, centenas))
    elif centenas == 1:
        if dezenas >= 2:
            if unidades >= 2:
                print('{} tem: {} centena, {} dezenas e {} unidades.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 1:
                print('{} tem: {} centena, {} dezenas e {} unidade.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 0:
                print('{} tem: {} centena e {} dezenas.'.format(numero, centenas, dezenas))
        elif dezenas == 1:
            if unidades >= 2:
                print('{} tem: {} centena, {} dezena e {} unidades.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 1:
                print('{} tem: {} centena, {} dezena e {} unidade.'.format(numero, centenas, dezenas, unidades))
            elif unidades == 0:
                print('{} tem: {} centena e {} dezena.'.format(numero, centenas, dezenas))
        elif dezenas == 0:
            if unidades >= 2:
                print('{} tem: {} centena e {} unidades.'.format(numero, centenas, unidades))
            elif unidades == 1:
                print('{} tem: {} centena e {} unidade.'.format(numero, centenas, unidades))
            elif unidades == 0:
                print('{} tem: {} centena.'.format(numero, centenas))
    elif centenas == 0:
        if dezenas >= 2:
            if unidades >= 2:
                print('{} tem: {} dezenas e {} unidades.'.format(numero, dezenas, unidades))
            elif unidades == 1:
                print('{} tem: {} dezenas e {} unidade.'.format(numero, dezenas, unidades))
            elif unidades == 0:
                print('{} tem: {} dezenas.'.format(numero, dezenas))
        elif dezenas == 1:
            if unidades >= 2:
                print('{} tem: {} dezena e {} unidades.'.format(numero, dezenas, unidades))
            elif unidades == 1:
                print('{} tem: {} dezena e {} unidade.'.format(numero, dezenas, unidades))
            elif unidades == 0:
                print('{} tem: {} dezena.'.format(numero, dezenas))
        elif dezenas == 0:
            if unidades >= 2:
                print('{} tem: {} unidades.'.format(numero, unidades))
            elif unidades == 1:
                print('{} tem: {} unidade.'.format(numero, unidades))
            elif unidades == 0:
                print('esse número é 0.')

