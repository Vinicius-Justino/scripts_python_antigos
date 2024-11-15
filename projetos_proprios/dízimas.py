from decimal import *
from math import floor

# Aumenta a precisão das casas decimais, para conseguirmos perídos maiores
PRECISAO = 100
getcontext().prec = PRECISAO

def achaPeriodo(dizima):
    # Pega a parte decimal da dízima
    parte_decimal = str(dizima - floor(dizima))[2:]
    
    # Pega o período da dízima
    for i in range(PRECISAO):
        for casa_decimal in range(1, PRECISAO):
            
            # Confere as repetições do período
            repetiçoes = []
            for i in range(1, floor(PRECISAO / casa_decimal) - 1):
                repetiçoes.append(parte_decimal[:casa_decimal] == parte_decimal[casa_decimal * i:casa_decimal * (i + 1)])
            
            # Se o periodo se repete infinitamente, retorna
            if False not in repetiçoes: 
                return parte_decimal[:casa_decimal]
        
        # Retira lentamente a parte não periódica da parte decimal, até que só sobre o período
        parte_decimal = str(parte_decimal)[1:]

if __name__ == "__main__":
    # pega a dízima
    n1 = Decimal(int(input("numerador: ")))
    n2 = Decimal(int(input("denominador: ")))
    dizima = n1 / n2

    print(f"\ndízima: {dizima}")
    print(f"período: {achaPeriodo(dizima)}")