salario = float(input('digite o valor do seu salário: '))

if salario > 1500:
    print('salário antigo: {:.2f}'.format(salario))
    print('reajuste: 5%')
    print('reajuste em dinheiro: {:.2f}'.format(salario/100*5))
    print('novo salário: {:.2f}'.format(salario+(salario/100*5)))

elif 700 < salario <= 1500:
    print('salário antigo: {:.2f}'.format(salario))
    print('reajuste: 10%')
    print('reajuste em dinheiro: {:.2f}'.format(salario/100*10))
    print('novo salário: {:.2f}'.format(salario+(salario/100*10)))

elif 280 < salario <= 700:
    print('salário antigo: {:.2f}'.format(salario))
    print('reajuste: 15%')
    print('reajuste em dinheiro: {:.2f}'.format(salario/100*15))
    print('novo salário: {:.2f}'.format(salario+(salario/100*15)))

elif 0 < salario <= 280:
    print('salário antigo: {:.2f}'.format(salario))
    print('reajuste: 20%')
    print('reajuste em dinheiro: {:.2f}'.format(salario/100*20))
    print('novo salário: {:.2f}'.format(salario+(salario/100*20)))

else:
    print('')
    print('                              quebrou o programa')
    print('')
    print('ocorreu um erro, brinque com o cachorro enquanto resolvemos o problema:')
    print('')
    print('')
    print('')
    print('                                  cachorro')
    print('')
    print('')
    print('')
    while True:
        print('sim/não')
        brincar = input('quer bricar com o cachorro? R: ')

        if brincar == 'sim':
            print('o cachorro está feliz.')
            print('')
        
        elif brincar == 'não':
            print('você é chato')
            print('')
            
        else:
            print('você nunca vai escapar do cachorro.')
            print('')
