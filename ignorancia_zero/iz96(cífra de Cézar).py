modo = ''
chave = 0

def recebeModo():
    global modo
    while True:
        print('Quer criptografar ou decriptografar?')
        modo = input('')

        if modo == 'criptografar' or modo == 'c':
            print('')
            break

        elif modo == 'decriptografar' or modo == 'd':
            print('')
            break

        else:
            print('Não é uma entrada válida, digite apenas opções mostradas na tela.')
            print('')

def recebeChave():
    global chave
    while True:
        print('Digite o valor da chave (1 - 26)')
        chave = int(input(''))

        if 1 <= chave <= 26:
            print('')
            break

        else:
            print('Não é uma entrada válida, digite apenas valores de 1 a 26')

def traduz(modo, mensagem, chave):
    if modo == 'criptografar' or modo == 'c':
        cripto = ''
        for muda in mensagem:
            if 97 <= ord(muda) <= 122:
                if ord(muda) + chave > 122:
                    letra = chr((97 + ((ord(muda) + chave) - 122)) - 1)

                elif ord(muda) + chave <= 122:
                    letra = chr(ord(muda) + chave)

            elif 65 <= ord(muda) <= 90:
                if ord(muda) + chave > 90:
                    letra = chr((65 + ((ord(muda) + chave) - 90)) - 1)

                elif ord(muda) + chave <= 90:
                    letra = chr(ord(muda) + chave)

            else:
                letra = muda

            cripto += letra

        print(cripto)

    elif modo == 'decriptografar' or 'd':
        decripto = ''
        for muda in mensagem:
            if 97 <= ord(muda) <= 122:
                if ord(muda) - chave < 97:
                    letra = chr((122 - (97 - (ord(muda) - chave)) + 1))

                elif ord(muda) - chave >= 97:
                    letra = chr(ord(muda) - chave)

            elif 65 <= ord(muda) <= 90:
                if ord(muda) - chave < 65:
                    letra = chr((90 - (65 - (ord(muda) - chave)) + 1))

                elif ord(muda) - chave >= 65:
                    letra = chr(ord(muda) - chave)

            else:
                letra = muda

            decripto += letra

        print(decripto)

def main():
    recebeModo()
    recebeChave()
    print('Digite a mensagem:')
    mensagem = input('')
    traduz(modo, mensagem, chave)

main()
