gameName = "Fifa 23"
gameDescription = """
    Fifa 23 e um jogo de futebol,
    desenvolvido pela Ea Sports,
    que possibilita jogar localmente ou online.
"""
print(gameName.upper()) # Retronar string em maiusculo
print(gameName.lower()) # Retronar string em minusculo
print(gameName.capitalize()) # Apenas primeira letra maiusculo
print(gameName.title()) # Todas as letras maiusculo
print(gameName.center(10, "-")) # Retorna string centralizada com caractere de preenchimento
print(gameName.find("a")) # Retorna a posicao de um determinado caractere
print(gameDescription.count("f")) # Conta caracteres
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento por outro
print(gameDescription.split(",")) # Quebra a string por em um caractere especifico