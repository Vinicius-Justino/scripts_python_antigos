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

    return final

tel = input('Telefonou para a vítima? R: ')
alibi = input('Esteve no local do crime? R: ')
casa = input('Mora perto da vítima? R: ')
conta = input('Devia para a vítima? R: ')
trampo = input('Já trabalhou para a vítima? R: ')

respostas = [tel, alibi, casa, conta, trampo]
provas = 0

for analise in respostas:
    if minusculo(analise) == 'sim':
        provas += 1

if provas == 5:
    print('\nAssassino.')

elif provas == 4 or provas == 3:
    print('\nCumplice.')

elif provas == 2:
    print('\nSuspeito.')

else:
    print('\nInocente.')
