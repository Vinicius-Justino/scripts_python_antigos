try:
    cadastrados = open('cadastrados.txt')
    cadastrados.close()
except:
    cadastrados = open('cadastrados.txt', 'w')
    cadastrados.close()

def recebeComando():
    '''
Recebe a ação que o usuário gostaria de realizar.
    '''
    print('---------------------------------------')
    print('            MENU PRINCIPAL             ')
    print('---------------------------------------')
    print('1 - Ver pessoas cadastradas            ')
    print('2 - Cadastrar uma nova pessoa          ')
    print('3 - Sair do sistema                    ')
    print('---------------------------------------')
    while True:
        comando = input('Sua opção: ')

        if '1' <= comando <= '3':
            return int(comando)
        else:
            print('Digite apenas o número correspondente a ação que deseja tomar.')

def mostraCadastrados():
    '''
Mostra uma ficha com todas as pessoas cadastradas.
    '''
    cadastrados = open('cadastrados.txt')
    print('---------------------------------------')
    print('           PESSOAS CADASTRADAS         ')
    print('---------------------------------------')
    for mostra in cadastrados.readlines():
        print(mostra, end='')
    cadastrados.close()

def cadastraPessoa():
    '''
Recebe os dados de uma nova pessoa que gostaria de se cadastrar.
    '''
    print('---------------------------------------')
    print('             NOVO CADASTRO             ')
    print('---------------------------------------')
    nome = input('Nome: ')

    while True:
        erro = False
        idade = input('Idade: ')

        for char in idade:
            if not '0' <= char <= '9':
                erro = True
                break

        if len(idade) <= 3 and not erro:
            return [nome, idade]
        else:
            print('Digite apenas números com no máximo 3 algarismos.')

def insereCadastro(nome, idade):
    '''
Insere uma nova pessoa na lista de cadastrados.
    '''
    cadastrados = open('cadastrados.txt', 'a')
    saida = nome + ' '*(30-len(nome)) + ' '*(3-len(idade)) + idade + ' anos'
    cadastrados.write('{} \n'.format(saida))
    cadastrados.close()

def main():
    '''
Função principal do programa.
    '''
    while True:
        comando = recebeComando()

        if comando == 1:
            mostraCadastrados()

        elif comando == 2:
            dados = cadastraPessoa()
            insereCadastro(dados[0], dados[1])

        elif comando == 3:
            print('Volte sempre!')
            break

main()
