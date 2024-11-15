erro = True
while erro:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')

    if len(nome) == len(senha):
        igual = 0
        for correçao in range(len(nome)):
            if ord(nome[correçao]) == ord(senha[correçao]):
                igual += 1
            elif ord(nome[correçao])+32 == ord(senha[correçao]) or ord(nome[correçao])-32 == ord(senha[correçao]):
                igual += 1

        if igual == len(nome):
            print('Senha Inválida.')

        else:
            print('Senha Aceita.')
            erro = False

    else:
        print('Senha Aceita.')
        erro = False
