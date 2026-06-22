import pygame

pygame.init()

pygame.mixer.music.load('New age.mp3')
pygame.mixer.music.play()

pygame.mixer.music.stop = input('Pressione Enter para encerrar...')
#outra forma seria importar o playsound