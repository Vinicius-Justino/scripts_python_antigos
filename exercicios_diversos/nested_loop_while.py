#determinando o número de empresas
empresas = int(input('digite o número de empresas: '))

#determinando o número de meses
meses = int(input('digite o número de meses: '))

#determinando os contadores
cont_empresas = 0

cont_meses = 0

#empresas
while cont_empresas <= empresas: #até 'contador' chegar em 'empresas' loop isso:
    cont_empresas += 1
    if cont_empresas > empresas:
        break
    balança = 0    #balança zera para cada nova empresa.
    cont_meses = 0  #contador zera para cada nova empresa.
    print('empresa {}:'.format(cont_empresas))
    print('')

    #meses
    while cont_meses <= meses:  #até 'contador' chegar em 'meses' loop isso:
        cont_meses += 1
        if cont_meses > meses:
            break
        print('mês {}:'.format(cont_meses))
        print('')
        #lucro
        lucro = int(input('quanto ganhou nesse mês: '))
        #gasto
        gasto = int(input('quanto gastou nesse mês: '))
        #total
        balança = balança + (lucro - gasto)  #balança recebe o valor total dos meses.
        print('')
#empresas
    if balança > 0:
        print('a empresa {} ficou com um lucro de {} reais.'.format(cont_empresas, balança))
        print('')
    elif balança == 0:
        print('a empresa {} ficou indiferente, com um saldo de 0 reais'.format(cont_empresas))
        print('')
    elif balança < 0:
        print('a empresa {} ficou com um prejuizo de {} reais.'.format(cont_empresas, balança))
        print('')
        
