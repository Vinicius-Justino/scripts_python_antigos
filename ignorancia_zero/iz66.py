def somaImposto(imposto, preço):
    preço += preço/100*imposto
    return preço

print(somaImposto(25, 100))
print(somaImposto(10, 800))
