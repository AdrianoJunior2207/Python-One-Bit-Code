name = input("Digite o nome do jogo\n")
yearLauch = int(input("Digite o ano de lancamento do jogo:\n"))
classification = float(input("Digite a classificacao do jogo:\n"))

if classification >= 8.0 and yearLauch > 2015:
    print(f"Recomendo jogar {name}!")
else:
    print(f"Nao recomendo jogar {name}!")

