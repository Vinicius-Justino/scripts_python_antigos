empresas = int(input('digite o número de empresas: '))
meses = int(input('digite o número de meses: '))

#empresa
for custos in range(empresas):  #para cada empresa loop isso:
    balança = 0
    #mes
    for dados in range(0, meses): #para cada mês loop issso:
        lucro = int(input('quanto ganhou nesse mês: '))
        gasto = int(input('quanto gastou nesse mês: '))
        balança = balança + (lucro - gasto)   #balança recebe o valor dos meses
#empresa
    print('a empresa terminou com um saldo de {} reais.'.format(balança))
