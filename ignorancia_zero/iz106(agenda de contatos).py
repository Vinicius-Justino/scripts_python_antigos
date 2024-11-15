dinossario = {}
print('AGENDA DE CONTATOS')
print('organize quantos contatos quiser')
print('digite "pare" no campo de texto "nome" para sair.')
while True:
    print('')
    nome = input('Digite o nome: ')

    if nome == 'pare':
        break
    
    telefone = input('Digite seu número de telefone: ')
    endereço = input('Digite o seu endereço: ')
    email = input('digite o seu email: ')

    dinossario[nome] ={'nome':nome, 'telefone':telefone, 'endereço':endereço, 'email':email}

aux = list(dinossario)
aux.sort()

for mostra1 in aux:
    print('')
    print('CONTATO {}'.format(aux.index(mostra1)+1))
    print('')
    for mostra2 in dinossario[mostra1]:
        saida = mostra2 + ' '*(9 - len(mostra2))
        print('{}- {}'.format(saida, dinossario[mostra1][mostra2]))
