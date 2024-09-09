# import pygame

# decolando = [x for x in range(11) if x<11]
# print(decolando[::-1])
# pygame.mixer.init()
# pygame.mixer.music.load("C:\\Users\\Juninho\\Desktop\\Learing Python\\Python One Bit Code\\Exercicios Fundamentos I\\PS5_trophie_platinum.mp3")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():  # Espera até o som terminar de tocar
#     pass

num = 1
while (num != 0):
    num = int(input("Qual tabuada voce quer de 1 a 10?"))
    for i in range(11):
        print(f"{num * i}")



