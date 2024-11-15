#Classe Ponto

class Ponto(object):
    def _init_(self,vx,vy):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy
#Classe Retângulo
        
class Retangulo(object):
    def _init_(self,l,a):
        self.largura = l
        self.altura = a
        
        
#Função Imprime ponto
        
def ImprimePonto(objetoPonto):
    print("Posição central do retãngulo")
    print("X: ", objetoPonto.x, "Y: ", objetoPonto.y)
    
# Função achar o centro do retângulo

def EncontraCentro(objetoPonto, objetoRetangulo):
    
    objetoPonto.x = (objetoRetangulo.largura - objetoPonto.vx) / 2
    objetoPonto.y = (objetoRetangulo.altura  - objetoPonto.vy) / 2
    
#Tela de Boas vindas
    
print("BEM VINDO !!!!")

#Recolhendo Dados

l = int(input("Digite a largura do retângulo: "))
a = int(input("Digite a altura do retângulo: "))
vx = int(input("Dogite o vertice x do ponto: ")) 
vy = int(input("Dogite o vertice y do ponto: "))

#Processando Dados

ponto = Ponto(vx, vy)
retangulo = Retangulo(l,a)
EncontraCentro(ponto, retangulo)

#Imprime X e Y central

ImprimePonto(ponto)
