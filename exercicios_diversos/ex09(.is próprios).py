def isalpha(entrada):
    '''
Retorna True se o valor digitado tiver apenas letras, se não, retorna False.
    '''
    for char in entrada:
        if not 'a' <= char <= 'z' and not 'A' <= char <= 'Z':
            return False

    return True

def isalnum(entrada):
    '''
Retorna True se o valor digitado tiver apenas letras e/ou números, se não,
retorna False.
    '''
    for char in entrada.lower():
        if not 'a' <= char <= 'z' and not 'A' <= char <= 'Z' and not '0' <= char <= '9':
            return False

    return True

def isnumeric(entrada):
    '''
Retorna True se o valor digitado tiver apenas números, se não, retorna False.
    '''
    for char in entrada:
        if not '0' <= char <= '9':
            return False

    return True

def islower(entrada):
    '''
Retorna True se todas as letras do valor digitado forem minúsculas, se não,
retorna False.
    '''
    um_minusculo = False
    
    for char in entrada:
        if isalpha(char):
            if not 'a' <= char <= 'z':
                return False
            else:
                um_minusculo = True

    if um_minusculo:
        return True

def isupper(entrada):
    '''
Retorna True se todas as letras do valor digitado forem maiúsculas, se não,
retorna False.
    '''
    um_maiusculo = False
    
    for char in entrada:
        if isalpha(char):
            if not 'A' <= char <= 'Z':
                return False
            else:
                um_maiusculo = True
                
    if um_maiusculo:
        return True

if __name__ == '__main__':
    entrada = input('Digite alguma coisa: ')
    print('\nTem apenas letras:', isalpha(entrada))
    print('Tem apenas números:', isnumeric(entrada))
    print('Tem letras e/ou números:', isalnum(entrada))
    print('As letras digitas são todas maiúsculas:', isupper(entrada))
    print('As letras digitadas são todas minusculas:', islower(entrada))
    
