gameSet = {"Fifa 23", "Red Dead 2", "Star Wars",
           "The Legend of Zelda", "Mario Odyssey", "Resident evil 4"}

print(gameSet)

# 1 - Buscar tamanho do set
print(len(gameSet))

# 2 - True e 1 sao considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gameSet.update(exampleSet)
print(gameSet)

# 4 -  Remover um item do set
gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)

# - Nao possibilita recuperar valores via slice(Fatiamento)