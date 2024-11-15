from math import pi

class objetoGrafico(object):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno):
        self.cor = cor_de_preenchimento
        self.pintada = preenchida
        self.borda = cor_de_contorno

class retangulo(objetoGrafico):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, base, altura):
        super(retangulo, self).__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
        self.base = base
        self.altura = altura
    def area(self):
        print('A área desse retângulo é {:.1f}.'.format(self.base*self.altura))
    def perimetro(self):
        print('O perímetro desse retângulo é {:.1f}.'.format((self.base+self.altura)*2))

class circulo(objetoGrafico):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, raio):
        super(circulo, self).__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
        self.raio = raio
    def area(self):
        print('A área desse círculo é {:.1f}.'.format(pi*(self.raio**2)))
    def perimetro(self):
        print('O perímetro desse círculo é {:.1f}.'.format((2*pi)*self.raio))

class triangulo(objetoGrafico):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, base, altura):
        super(triangulo, self).__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
        self.base = base
        self.altura = altura
    def area(self):
        print('A área desse triângulo é de {:.1f}.'.format((self.base*self.altura)/2))
    def perimetro(self):
        print('O perímetro desse triângulo é de {:.1f}.'.format(self.base + self.altura + (self.base**2 + self.altura**2)**(1/2)))

retangulo = retangulo('branco', True, 'preto', 5, 3)
circulo = circulo('branco', True, 'preto', 1)
triangulo = triangulo('roxo', False, 'vermelho', 3, 4)

retangulo.area()
retangulo.perimetro()

circulo.area()
circulo.perimetro()

triangulo.area()
triangulo.perimetro()
