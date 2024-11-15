nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if media == 10:
    print('aprovado com distinção.')
    print('média: 10.0')

elif media >= 7:
    print('aprovado.')
    print('média: {:.1f}'.format(media))

else:
    print('reprovado.')
    print('média: {:.1f}'.format(media))
