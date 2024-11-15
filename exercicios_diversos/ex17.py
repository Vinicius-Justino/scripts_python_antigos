co = float(input('digite o valor do cateto oposto:'))
ca = float(input('digite o valor do cateto adjacente:'))
hip = (co**2+ca**2)**(1/2)
print('esse triângulo tem catetos {} e {}, e hipotenusa {}'.format(co, ca, hip))
