def leiaInt():
    try:
        entrada = input('Digite um número inteiro: ')
        while True:
            erro = False
            
            for char in entrada:
                if not '0' <= char <= '9' and not char == '-':
                    print('Digite apenas números inteiros.')
                    erro = True
                    break
                
            if not erro:
                return int(entrada)

            entrada = input('\nDigite um número: ')
    except ValueError:
        return 'não foi informado'

def leiaFloat():
    try:
        entrada = input('Digite um número real: ')
        while True:
            erro = False
            
            for char in entrada:
                if not '0' <= char <= '9' and not char == '-' and not char == '.':
                    print('Digite apenas número reais.')
                    erro = True
                    break
                
            if not erro:
                return float(entrada)

            entrada = input('\nDigite um número: ')
    except ValueError:
        return 'não foi informado'
numero1 = leiaInt()
numero2 = leiaFloat()

print('\nNúmero inteiro: {}.'.format(numero1))
print('Número real: {}.'.format(numero2))
