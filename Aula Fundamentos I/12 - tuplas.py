gamesTuple = ("Fifa 24", "Red Dead 2", "Star Wars Survivor",
              "Mario Odyssey", "The Legend of Zelda")
print(gamesTuple)
print(type(gamesTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 -Buscar o ultimo item da lista
print(gamesTuple[-1])

# 3 - Buscar jogos ate uma determinada posicao
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posicao em diante
print(gamesTuple[2:])

# 5 - Recuperar item da tupla pelo indice
print(gamesTuple.index("Red Dead 2"))

# Nao possibilita adicionar valores na tupla
# Nao possibilita remover valores na tupla
# Nao possibilita ordenar valores na tupla