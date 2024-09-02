import pprint

gamesDict = {
    "resident evil 4":{
        "yearLaunc": 2023,
        "classification": 9.8,
        "genre": ["acao", "aventura"]
    },
    
    "mario odyssey":{
        "yearLaunc": 2017,
        "classification": 10,
        "genre": ["aventura", "3d"]
    },
    
    "donkey kong country":{
        "yearLaunc": 1995,
        "classification": 9.5,
        "genre": ["aventura ", "plataforma"]
    }
    
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 -  Bsucar informacao dentro de um dicionario aninhado
print(gamesDict["mario odyssey"]["genre"])

# 2 - Adicionar novo item
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])

# 3 - Excluir um dicionario
del gamesDict["resident evil 4"]
pp.pprint(gamesDict)