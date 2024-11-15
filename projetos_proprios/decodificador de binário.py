mensagem = input('Digite a mensagem que deseja decodificar: ').split()
decodificada = ''

for caracteres in mensagem:
    char = 0

    for decodifica in range(7, -1, -1):
        if caracteres[decodifica] == '1':
            char += 2**(8-(decodifica+1))

    decodificada += chr(char)

print(decodificada)
