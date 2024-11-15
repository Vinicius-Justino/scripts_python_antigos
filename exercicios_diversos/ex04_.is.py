while True:
    c = input('digite algo: ')
    #CLASSE
    print('a classe é {}'.format(type(c)))
    #ALFABÉTICO?
    if c.isalpha() == True:
        print('é alfabético.')
    if c.isalpha() == False:
        print('não é alfabético.')
    #NUMÉRICO?
    if c.isnumeric() == True:
        print('é um número.')
    if c.isnumeric() == False:
        print('não é um número.')
    #ALFANUMÉRICO?
    if c.isalnum() == True:
        print('é alfanumérico.')
    if c.isalnum() == False:
        print('não é alfanumérico.')
    #TEXTO?
    if c.isascii() == True:
        print('é um texto.')
    if c.isascii() == False:
        print('não é um texto.')
    #ESPAÇOS?
    if c.isspace() == True:
        print('esse valor tem apenas espaços.')
    if c.isspace() == False:
        print('esse valor não tem apenas espaços.')
    #MAIÚSCULO?
    if c.isupper() == True:
        print('está escrito em letras maiúsculas.')
    if c.isupper() == False:
        print('não está escrito em letra maiúsculas.')
    #MINÚSCULO?
    if c.islower() == True:
        print('está escrito em letras minúsculas.')
    if c.islower() == False:
        print('não está escrito em letras minúsculas.')
    #CAPITALIZADO?
    if c.istitle() == True:
        print('está capitalizado.')
    if c.istitle() == False:
        print('não está capitalizado.')
    #É POSSÍVEL MOSTRAR?
    if c.isprintable() == True:
        print('isso pode ser mostrado na tela.')
    if c.isprintable() == False:
        print('isso não pode ser mostrado na tela.')
