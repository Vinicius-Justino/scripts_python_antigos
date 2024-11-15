usuario = open('usuários.txt', 'r')

for teste in range(5):
    print(usuario.readline())

usuario.close
