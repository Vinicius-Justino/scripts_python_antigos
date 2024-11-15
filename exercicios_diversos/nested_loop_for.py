#determinando o número de empresas
empresas = int(input('digite o número de empresas: '))

#determinando o número de meses
meses = int(input('digite o número de meses: '))

#empresa
for custos in range(empresas):  #para cada empresa loop isso:
    balança = 0  #balança zera a cada nova empresa
    print('empresa {}:'.format(custos + 1))
    print('')
    #mês
    for dados in range(0, meses): #para cada mês loop isso:
        print('mês {}:'.format(dados + 1))
        print('')
        #lucro
        lucro = int(input('quanto ganhou nesse mês: '))
        #gasto
        gasto = int(input('quanto gastou nesse mês: '))
        balança = balança + (lucro - gasto)   #balança recebe o valor dos meses
        print('')        
#empresa
    print('a empresa terminou com um saldo de {} reais.'.format(balança))
    print('')
