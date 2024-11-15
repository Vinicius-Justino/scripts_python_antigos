from random import shuffle

with open("lista.txt") as lista:
    palavras = lista.read().splitlines()

print(palavras)
print(len(palavras))

ordem = [int(i) for i in input("\n\ncoloque a ordem separada por espaços\n:").split()]
lista_aleatoria = list(range(1,len(palavras)+1))
shuffle(lista_aleatoria)

palavraco = ""
for i in ordem:
    palavraco += palavras[lista_aleatoria[i-1]-1] + " "

print("\nAqui vai a sua dose de sabedoria:\n❝ " + palavraco + "❞")