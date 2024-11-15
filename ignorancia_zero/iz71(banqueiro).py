banco = [[000000, 0]]
loop = True

while loop:
    print('                 BANCÁRIO')
    print('1 - depositar')
    print('2 - fechar')
    print('')
    while True:
        açao = input('digite o número da sua ação: ')
        print('')

        if açao == '1':
            registro = int(input('digite o número do seu registro: '))

            for testes in range(len(banco)):
                c = False
                if banco[testes][0] == registro:
                    deposito = float(input('digite o valor do depósito: '))
                    banco[testes][1] += deposito
                    c = True
                    break

                if c == False:
                    deposito = float(input('digite o valor do depósito: '))
                    banco += [[registro, deposito]]
                    break

            print('')

            r = input('deseja ver o seu saldo bancário? R: ')

            while True:
                if r == 'sim':
                    for saldo in range(len(banco)):
                        if banco[saldo][0] == registro:
                            print('seu saldo é de R${:.2f}.'.format(banco[saldo][1]))
                            print('')
                            break

                    break

                elif r == 'não':
                    print('')
                    break

                else:
                    print('não entendo como uma resposta, digite apenas "sim" ou "não".')
                    print('')

            break

        elif açao == '2':
            print('volte sempre.')
            loop = False
            break

        else:
            print('não entendo como uma ação, digite apenas "1" ou "2".')
            print('')
