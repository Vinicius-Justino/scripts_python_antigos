usuarios = open('usuários.txt', 'w')

def formata(texto, limite):
    if len(texto) < limite:
        saida =  texto + ' '*(limite - len(texto))

    return saida

usuarios.write('{} 456123789 \n'.format(formata('alexandre', 15)))
usuarios.write('{} 1245698456 \n'.format(formata('anderson', 15)))
usuarios.write('{} 123456456 \n'.format(formata('antonio', 15)))
usuarios.write('{} 91257581 \n'.format(formata('carlos', 15)))
usuarios.write('{} 987458 \n'.format(formata('cesar', 15)))
usuarios.write('{} 789456125'.format(formata('rosemary', 15)))

usuarios.close()
