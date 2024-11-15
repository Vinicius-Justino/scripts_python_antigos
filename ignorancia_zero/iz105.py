def geraDicionario():
    palavras = open('PALAVRAS.txt')

    dicionario = palavras.readlines()

    for arruma in range(len(dicionario)):
        if '\n' in dicionario[arruma]:
            saida = ''
            for tira in dicionario[arruma]:
                if tira == '\n':
                    continue

                saida += tira

            dicionario[arruma] = saida

    return dicionario

def recebeFrase():
    while True:
        erro = False
        secreta = input('Digite a frase secreta: \n').upper()
        for confere in secreta:
            if '0' <= confere <= '9' or 192 <= ord(confere):
                erro = True

        if erro == False:
            return secreta

        else:
            print('Digite apenas letras sem acento, não digite números.')

def procuraPalavra(dicionario, palavra):
    letras = []
    palavras_possiveis = []
    
    for letra in palavra:
        if 'A' <= letra <= 'Z':
            letras += [palavra.index(letra)]
            
    for procura in dicionario:
        if len(procura) == len(palavra):
            aux = list(procura)
            cont = 0

            for testa in letras:
                if aux[testa] == palavra[testa]:
                    cont += 1

            if cont == len(letras):
                palavras_possiveis += [procura]

    return palavras_possiveis

def organizaPossiveis(frase):
    lista = []
    for organiza in frase.split():
        lista += [procuraPalavra(dicionario, organiza)]

    return lista

def criaFrases(candidatas_totais):
    aux = open('auxiliar.py', 'w')
    aux.write('def funcao_auxiliar(candidatas_totais):\n')
    aux.write('\tarquivo = open("FRASE.txt", "w")\n')

    aux.write('\tfrase = []\n')
    aux.write('\tfor i in range(len(candidatas_totais)):\n')
    aux.write('\t\tfrase.append("")\n')

    for i in range(len(candidatas_totais)):
        linha = '\t'*(i+1)
        linha += 'for a%i in range(len(candidatas_totais[%i])):\n'%(i,i)
        aux.write(linha)
        linha = '\t'*(i+2) + 'frase[%i]= candidatas_totais[%i][a%i]\n'%(i,i,i)
        aux.write(linha)

    aux.write('\t'*(i+2) + 'frase_s = ""\n')
    aux.write('\t'*(i+2) + 'for palavra in frase:\n')
    aux.write('\t'*(i+3)+ 'frase_s += palavra\n')
    aux.write('\t'*(i+3)+ 'frase_s += " "\n')
    aux.write('\t'*(i+2) + 'arquivo.write(frase_s + "\\n")\n')

    aux.write('\tarquivo.close()')

    aux.close()

    print("Gerando Lista de Palavras Candidatas...")

dicionario = geraDicionario()
secreta = recebeFrase()
possiveis = organizaPossiveis(secreta)
criaFrases(possiveis)

from auxiliar import funcao_auxiliar

def main():
    funcao_auxiliar(possiveis)

main()
                

    
