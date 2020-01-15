import pygame
import sys
import pygameMenu

pygame.init()

#window
screen_s = (600, 700)
gDisplay = pygame.display.set_mode(screen_s)
pygame.display.set_caption('Escape The Mountain')

#icon
icon = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\mountain.png')
pygame.display.set_icon(icon)


run = True

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
    #background
    background = "C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\backg.jpg"
    B_image = pygame.image.load(background)
    gDisplay.blit(B_image, [0, -180])
    pygame.display.update()
