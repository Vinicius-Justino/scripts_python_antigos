def maiusculo(string):
    '''
Transforma todas as letras de uma string em
maiúsculas utilizando o padrão ASCII.
    '''
    final = ''
    for letras in string:
        if 97 <= ord(letras) <= 122:
            aux = chr(ord(letras) - 32)

        else:
            aux = letras

        final += aux

    print(final)

def minusculo(string):
    '''
transforma todas as letras de uma string em
minúsculas utilizando o padrão ASCII.
    '''
    final = ''
    for letras in string:
        if 65 <= ord(letras) <= 90:
            aux = chr(ord(letras) + 32)

        else:
            aux = letras

        final += aux

    print(final)

maiusculo('Chiclete')
minusculo('CHiCleTe')
