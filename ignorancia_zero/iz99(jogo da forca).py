asciis = [
'''   +----+
   |    |
        |
        |
        |
        | 
===========''',
'''   +----+
   |    |
   O    |
        |
        |
        |
===========''',
'''   +----+
   |    |
   O    |
   |    |
        |
        |
===========''',
'''   +----+
   |    |
   O    |
  /|    |
        |
        |
===========''',
'''   +----+
   |    |
   O    |
  /|\   |
        |
        |
===========''',
'''   +----+
   |    |
   O    |
  /|\   |
  /     |
        |
===========''',
'''   +----+
   |    |
   O    |
  /|\   |
  / \   |
        |
===========''']

from random import randint
from random import choice

objetos = [['giroscopio', 'medalha', 'carta', 'caderno', 'computador', 'cadeira', 'bandeira', 'concha', 'controle', 'escada', 'carteira', 'brinquedo', 'toalha', 'grampeador', 'chinelo', 'impressora' 'tesoura', 'chuveiro', 'teclado'], ['Objeto']]
animais = [['formiga', 'elefante', 'girafa', 'babuino', 'cachorro', 'gato', 'coruja', 'gorila', 'crocodilo'], ['Animal']]
comidas = [['hamburguer', 'chocolate', 'cebola', 'cenoura', 'tomate', 'melancia', 'lasanha', 'pirulito', 'coxinha', 'queijo', 'pipoca'], ['Comida']]
corpo = [['encefalo', 'ouvido', 'perna', 'joelho', 'cabelo', 'nariz', 'boca', 'barriga', 'pulso', 'esqueleto', 'cotovelo'], ['Corpo humano']]
esporte = [['futebol', 'basquete', 'queimada', 'corrida', 'canoagem', 'boxe', 'esgrima', 'atletismo', 'argolas'], ['Esporte']]
profissao = [['atleta', 'telemarketing', 'astronauta', 'bombeiro', 'enfermeiro', 'faxineiro', 'diarista', 'programador', 'jornalista', 'caminhoneiro'], ['Profissão']]
transporte = [['submarino', 'carro', 'barco', 'moto', 'bicicleta', 'trem', 'triciclo'], ['Meio de transporte']]
palavras = [objetos, animais, comidas, corpo, esporte, profissao]
jogando = True
certas = []
erradas = []
erros = 0

def escolhePalavra():
    global palavras
    indice = randint(0, 5)
    categoria = palavras[indice]
    palavra = [choice(categoria[0])] + [categoria[1]]

    return palavra
    
def imprimePalavra():
    global palavra, certas
    saida = ''
    for letras in palavra[0]:
        if letras in certas:
            saida += letras

        else:
            saida += '_'

        saida += ' '

    return saida

def imprimeJogo():
    global palavras, palavra, certas, erradas, erros
    print(palavra[1][0])
    print('')
    print(asciis[erros])
    print('')
    print('Letras erradas:', end=' ')
    for formata in erradas:
        print(formata, end=' ')
    print('')
    print(imprimePalavra())
    print('')

def palpite():
    global certas, erradas, erros
    while True:
        resposta = input('Digite seu palpite: ')

        if len(resposta) == 1:
            if 97 <= ord(resposta) <= 122 and resposta not in certas and resposta not in erradas:
                if resposta in palavra[0]:
                    certas += [resposta]

                else:
                    erradas += [resposta]
                    erros += 1

                break

            else:
                print('Insira apenas letras que não foram digitadas ainda.')

        else:
            print('Digite apenas uma letra.')

def verifica():
    global erros, palavra, certas, jogando
    aux = 0
    for verifica in palavra[0]:
        if verifica in certas:
            aux += 1

    if aux == len(palavra[0]):
        imprimeJogo()
        print('Parabéns, você acertou! A palavra era {}.'.format(palavra[0]))
        jogando = False

    elif erros == 6:
        imprimeJogo()
        print('Infelizmente você ultrapassou o limite de tentativas, a palavra era {}.'.format(palavra[0]))
        jogando = False
        
def main():
    global palavra, jogando, palavras, certas, erradas, erros
    while True:
        jogando = True
        palavra = escolhePalavra()
        certas = []
        erradas = []
        erros = 0
        while jogando:
            imprimeJogo()
            palpite()
            verifica()

        loop = input('Deseja jogar de novo(s/n): ')

        if loop == 'n':
            break

main()   
