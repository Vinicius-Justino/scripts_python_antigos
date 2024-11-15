##============================= DECODIFICA BINÁRIO ===========================##
def DecodificaBinario(binario):
    '''
Converte um texto escito em binário com caracteres entre as posições 1 e 255
na tabela ASCII para um texto convencional.
    '''
    decodificada = ''

    for caracteres in binario:
        char = 0

        for decodifica in range(8, 0, -1):
            if caracteres[decodifica-1] == '1':
                char += 2**(8-decodifica)

        decodificada += chr(char)

    return decodificada

##=========================== CODIFICA PARA BINÁRIO ==========================##
def CodificaBinario(texto):
    '''
Converte um texto convencional com os caracteres entre as posições 1 e 255
na tabela ASCII para um texto escrito em binário.
    '''
    codificada = ''

    for caracteres in texto:
        num = ord(caracteres)
        binario = ''

        for codifica in range(8, 0, -1):
            if num - 2**(codifica-1) >= 0:
                num -= 2**(codifica-1)
                binario += '1'

            else:
                binario += '0'

        codificada += binario + ' '

    return codificada



if __name__ == '__main__':
    print(' '*30 + 'Conversor de binário' + ' '*30)
    while True:
        açao = input('\nDeseja codificar ou decodificar? \n').lower()

        if açao[0] == 'c':
            mensagem = input('\nDigite a mensagem que deseja codificar: ')
            print('\n{}'.format(CodificaBinario(mensagem)))
        elif açao[0] == 'd':
            mensagem = input('\nDigite a mensagem que deseja decodificar: ').split()
            print('\n{}'.format(DecodificaBinario(mensagem)))
