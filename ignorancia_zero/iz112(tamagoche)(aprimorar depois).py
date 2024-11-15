def calculaIMC(peso, altura):
    imc = peso/altura**2

    if imc < 18.5:
        resultado = 'abaixo do peso, será que não poderia ganhar uns quilinhos?'
    elif 18.5 <= imc <= 24.9:
        resultado = 'eutrófico, isso é ótimo!'
    elif 25 <= imc <= 29.9:
        resultado = 'com sobrepeso, é melhor ficar atento!'
    elif 30 <= imc <= 34.9:
        resultado = 'com obesidade I, que tal se exercitar um pouco mais?'
    elif 35 <= imc <= 39.9:
        resultado = 'com obesidade II, poderia pelo menos fazer umas caminhadas.'
    elif imc >= 40:
        resultado = 'com obesidade III...'

    return resultado

class pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.peso = peso
        pessoa.altura = altura
    def envelhecer(self):
        pessoa.idade += 1
        print('{} agora tem {} anos!'.format(pessoa.nome, pessoa.idade))

        if pessoa.idade <= 21:
            pessoa.altura += 0.005
            pessoa.altura = float('{:.3f}'.format(pessoa.altura))
            print('{} cresceu 0.5cm, sua altura agora é {}!'.format(pessoa.nome, pessoa.altura))
    def engordar(self, quilos):
        pessoa.peso += quilos
        imc = calculaIMC(pessoa.peso, pessoa.altura)
        print('{} engordou {} quilos, e está com {}kg agora.'.format(pessoa.nome, quilos, pessoa.peso))
        print('{} está {}'.format(pessoa.nome, imc))
    def emagrecer(self, quilos):
        pessoa.peso -= quilos
        imc = calculaIMC(pessoa.peso, pessoa.altura)
        print('{} emagreceu {} quilos, e está com {}kg agora.'.format(pessoa.nome, quilos, pessoa.peso))
        print('{} está {}'.format(pessoa.nome, imc))
    def crescer(self, cm):
        pessoa.altura += cm/100
        pessoa.altura = float('{:.3f}'.format(pessoa.altura))
        print('{} cresceu {}cm e está com {}m'.format(pessoa.nome, cm, pessoa.altura))
        if pessoa.altura >= 3:
            print('O céu é o limite!')

print('TAMAGOCHE')
nome = input('Digite o nome do seu mascote: ')
idade = int(input('Digite a idade do seu mascote: '))
peso = float(input('Digite o peso do seu mascote: '))
altura = float(input('Digite a altura em metros do seu mascote: '))

pessoa = pessoa(nome, idade, peso, altura)
while True:
    print('\nO que deseja fazer:')
    comando = input('envelhecer(1)   engordar(2)   emagrecer(3)   crescer(4) \n')

    if comando == '1':
        pessoa.envelhecer()

    elif comando == '2':
        quilos = float(input('Quantos quilos? \n'))
        pessoa.engordar(quilos)

    elif comando == '3':
        quilos = float(input('Quantos quilos? \n'))
        pessoa.emagrecer(quilos)

    elif comando == '4':
        cm = int(input('Quantos centímetros? \n'))
        pessoa.crescer(cm)

    else:
        print('Por favor, digite 1, 2, 3, ou 4.')
