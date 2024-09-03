gameList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]

# 1 - Iterando valores de uma lista

for game in gameList:
    print(game)
    
# 2 - Quando a condicao for atendida, o Loop sera encerrado
for game in gameList:
    if game == "Red Dead 2":
        break
    print(game)
    
# 3 - Quando a condicao for atendida, o loop vai para a proxima iteracao
for game in gameList:
    if game == "Red Dead 2":
        continue 
    print(game)
    
# 4 - Avaliacao do Jogo
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliacoes deseja fazer no jogo:\n"))
sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo:\n"))
    sum += note #sum = sum + note
print(f"Media de avaliacao do jogo {gameName} e {sum/gameRating:.2f}")    