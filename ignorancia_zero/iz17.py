#determinando o numero de pessoas
pessoas = input('digite o número de pessoas: ')

while pessoas.isnumeric() == False:
    if '-' in pessoas:
        print('')
        print('mínimo 1 pessoa.')
        pessoas = input('digite o número de pessoas: ')
            
    else:
        print('')
        print('não é um valor válido, digite novamente.')
        pessoas = input('digite o número de pessoas: ')
    
pessoas = int(pessoas)

while pessoas <= 0:
    print('')
    print('mínimo 1 pessoa.')
    pessoas = input('digite o número de pessoas: ')
    while pessoas.isnumeric() == False:
        if '-' in pessoas:
            print('')
            print('mínimo 1 pessoa.')
            pessoas = input('digite o número de pessoas: ')
            
        else:
            print('')
            print('não é um valor válido, digite novamente.')
            pessoas = input('digite o número de pessoas: ')
    if pessoas > 0:
        break

cont_pessoas = 0

#loop isso, loop isso, loop isso, loop isso, loop isso, loop isso, loop isso, loop isso, loop isso, loop isso, loop isso...
#pessoas
while cont_pessoas < pessoas:   #para cada pessoa loop isso:
    cont_pessoas += 1
    if cont_pessoas > pessoas:
        break
    print('')
    print('pessoa {}:'.format(cont_pessoas))
    print('')

    #mês
    mes = input('digite o mês em que você nasceu: ')

    while mes.isnumeric() == False:
        if '-' in mes:
            print('')
            print('não é um valor válido, digite um número entre 1 e 12.')
            mes = input('digite o mês que você nasceu: ')

        else:
            print('')
            print('não é um valor válido, digite o número correspondente ao mês.')
            mes = input('digite o mês em que você nasceu: ')

    mes = int(mes)

    while mes < 1:
        print('')
        print('não é um valor válido, digite um número entre 1 e 12.')
        mes = input('digite o mês que você nasceu: ')

        while mes.isnumeric() == False:
            if '-' in mes:
                print('')
                print('não é um valor válido, digite um número entre 1 e 12.')
                mes = input('digite o mês que você nasceu: ')

            else:
                print('')
                print('não é um valor válido, digite o número correspondente ao mês.')
                mes = input('digite o mês que você nasceu: ')

        mes = int(mes)

    while mes > 12:
        print('')
        print('não é um valor válido, digite um número entre 1 e 12.')
        mes = input('digite o mês que você nasceu: ')

        while mes.isnumeric() == False:
            if '-' in mes:
                print('')
                print('não é um valor válido, digite um número entre 1 e 12.')
                mes = input('digite o mês que você nasceu: ')

            else:               
                print('')
                print('não é um valor válido, digite o número correspondente ao mês.')
                mes = input('digite o mês que você nasceu: ')

        mes = int(mes)
##############################################################################################################################
    #dia
    dia = input('digite o dia do seu nascimento: ')

    while dia.isnumeric() == False:
        if mes == 1:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 31.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 2:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 29.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 3:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 31.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 4:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 30.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 5:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 30.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 6:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 30.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 7:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 31.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 8:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 31.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 9:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 30.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 10:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 31.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 11:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 30.')
                dia = input('digite o dia que você nasceu: ')

        if mes == 12:
            if '-' in dia:
                print('')
                print('não é um valor válido, digite um número entre 1 e 31.')
                dia = input('digite o dia que você nasceu: ')
                
            else:               
                print('')
                print('não é um valor válido, digite o número correspondente ao mês.')
                mes = input('digite o mês que você nasceu: ')

    dia = int(dia)

    

    dia = int(dia)

    while dia < 1:
        if dia.isnumeric() == False:
            if mes == 1:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 31.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 2:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 29.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 3:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 31.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 4:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 30.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 5:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 30.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 6:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 30.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 7:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 31.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 8:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 31.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 9:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 30.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 10:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 31.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 11:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 30.')
                    dia = input('digite o dia que você nasceu: ')

            if mes == 12:
                if '-' in dia:
                    print('')
                    print('não é um valor válido, digite um número entre 1 e 31.')
                    dia = input('digite o dia que você nasceu: ')

            else:
                print('')
                print('')
####################################################################################################################
    #ano
    ano = input('digite o ano em que você nasceu: ')

    while ano.isnumeric() == False:
        print('')
        print('não é um valor válido, digite novamente.')
        ano = input('digite o ano em que você nasceu: ')

    ano = int(ano)

    #idade desejada
    idade = input('digite a idade desejada: ')

    while idade.isnumeric() == False:
        print('')
        print('não é um valor válido, digite novamente.')
        idade = input('digite a idade desejada: ')

    idade = int(idade)

    #blá, blá, blá, todo o resto
    ano += idade

    print('pessoa {} teria {} anos no dia {}/{}/{}.'.format(cont_pessoas, idade, dia, mes, ano))
