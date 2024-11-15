def count(string, substring):
    cont = 0

    for separa in range(len(string) + 1 - len(substring)):
        if string[separa:separa+len(substring)] == substring:
            cont += 1

    return cont

print(count('mississipi', 's')) 
