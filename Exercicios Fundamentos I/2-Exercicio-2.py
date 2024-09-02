# Resolucao 1

# word = input("Qual palavra?")
# firtsLetter = word[0:1]
# word = word.capitalize()
# print(word.replace(firtsLetter, "#"))

# Resolucao 2 

firstWord = input("Primeira:")
secondWord = input("Segunda:")
aux = firstWord
firstWord = (firstWord.replace(firstWord[0:2], secondWord[0:2] ))
secondWord = (secondWord.replace(secondWord[0:2], aux[0:2] ))
answer = (firstWord + " " + secondWord)
print(answer)









