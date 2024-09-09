# 1 - Liste valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#     if i < 4:
#         print(i)

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["Fifa 23", "Red Dead 2", "Star Wars",
           "The Legend of Zelda", "Mario Odyssey", "Resident evil 4"]

# 2 - Jogos que possua a letra A

newList = [x for x in gamesList if "a" in x]
print(newList)

# Fazendo com FOR
for y in gamesList:
    if "R" in y:
        print(y)
        
        
# 3 - Jogos que zerei
gamesFinished = [x for x in gamesList if x != "Red Dead 2"]
print(gamesFinished)