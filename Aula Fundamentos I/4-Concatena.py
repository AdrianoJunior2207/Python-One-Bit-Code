name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de Lancamento do jogo\n")) 
gamePrice = float(input("Digite o preco do jogo:\n"))
planIncluded = input("Ele esta incluido na assinatura?\n")

print("###Dados do Jogo###")
print("===================")
# Alternativa 1
print("Nome do Jogo :", name)
print("Ano de Lancamento :", yearLaunch)
print("Preco do Jogo :", gamePrice)
print("Esta incluso no plano :", planIncluded)

# Alternativa 2
print("Nome do Jogo :", name, 
      "\n Ano de Lancamento :", yearLaunch, 
      "\n Preco do Jogo :", gamePrice, 
      "\n Esta incluso no plano :", planIncluded 
     )


# Alternativa 3
print(f"Nome do Jogo : {name} \nAno de Lancamento :{yearLaunch} \nPreco do Jogo :{gamePrice} \nEsta incluso no plano:{planIncluded}")