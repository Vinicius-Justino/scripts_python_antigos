class Banco(object):
    total = 0
    taxa_reserva = 0.1
    __reserva_exigida = 1000
    def __calculaReserva():
        print('A reserva do seu banco é de R${:.2f}, o mínimo é {:.2f}'.format(Banco.total*taxa_reserva, __reserva_exigida))
    def podeEmprestimo(self, saldo):
        if self.saldo*Banco.taxa_reserva >= Banco.__reserva_exigida == True:
            print('Você pode receber emprestimos.')
        elif self.saldo*Banco.taxa_reserva >= Banco.__reserva_exigida == False:
            print('Você não pode receber empréstimos.')

class Conta(Banco):
    def __init__(self, saldo, ID, senha):
        self.saldo = saldo
        self.__ID = ID
        self.__senha = senha
        Banco.total += saldo
    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.saldo += valor
            Banco.total += valor
            print('O dinheiro foi deposito com sucesso!')
        else:
            print('senha inválida, tente novamente.')
    def saque(self, senha, valor):
        if senha == self.__senha:
            if self.saldo >= valor:
                self.saldo -= valor
                Banco.total -= valor
                print('O dinheiro foi sacado com sucesso!')
            else:
                print('Infelizmente, você não pode sacar essa quantia.')
        else:
            print('Senha inválida, tente novamente.')
    def status(self):
        self.podeEmprestimo(self.saldo)
    def Saldo(self):
        print('O seu saldo é de R${:.2f}'.format(self.saldo))

saldo = float(input('Digite o valor do seu saldo: '))
ID = int(input('Digite o número do seu ID: '))
senha = input('Digite a sua senha: ')

conta = Conta(saldo, ID, senha)

while True:
    print('\nO que deseja fazer?')
    açao = input('fazer um depósito(1)  sacar um quantia(2)  conferir seu status no banco(3)  conferir o seu saldo(4) \n')

    if açao == '1':
        valor = float(input('Digite o valor que deseja depositar: '))
        confere = input('Confirme a sua senha: ')

        conta.deposito(confere, valor)

    elif açao == '2':
        valor = float(input('Digite o valor que deseja sacar: '))
        confere = input('Confirme a sua senha: ')

        conta.saque(confere, valor)

    elif açao == '3':
        conta.status()

    elif açao == '4':
        conta.Saldo()

    else:
        print('Não reconheco como um comando, tente novamente.')
