from random import randint
q1n1 = randint(1, 20)
q1n2 = randint(1, 20)
q2n1 = randint(1, 20)
q2n2 = randint(1, 20)
q3n1 = randint(1, 20)
q3n2 = randint(1, 20)
q4n1 = randint(1, 20)
q4n2 = randint(1, 20)
q5n1 = randint(1, 20)
q5n2 = randint(1, 20)
print('-------------------CALCULADORA:the book, the movie, the game-----------------')
nome = input('digite seu nome de usuário:')
print('digite o resultado das multiplicaçôes a seguir:')
q1 = input('{}x{}='.format(q1n1, q1n2))
q2 = input('{}x{}='.format(q2n1, q2n2))
q3 = input('{}x{}='.format(q3n1, q3n2))
q4 = input('{}x{}='.format(q4n1, q4n2))
q5 = input('{}x{}='.format(q5n1, q5n2))
print('---------------------------------GABARITO------------------------------------')
print('resultado:{} / Sua resposta:{}'.format(q1n1*q1n2, q1))
print('resultado:{} / Sua resposta:{}'.format(q2n1*q2n2, q2))
print('resultado:{} / Sua resposta:{}'.format(q3n1*q3n2, q3))
print('resultado:{} / Sua resposta:{}'.format(q4n1*q4n2, q4))
print('resultado:{} / Sua resposta:{}'.format(q5n1*q5n2, q5))
ponto = input('Quantas você acertou?')
print('Parabéns {}, {} é um bom resultado!'.format(nome, ponto))
