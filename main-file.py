import pygame
import sys
import pygameMenu


pygame.init()

#window
screen_s = (600, 700)

gDisplay = pygame.display.set_mode(screen_s)
pygame.display.set_caption('Escape The Mountain')

#start menu
m_size = (200, 300)

pygameMenu.Menu(gDisplay, m_size, font, title, *args) # -> Menu object

#background
background = "C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\backg.jpg"
B_image = pygame.image.load(background).convert()
gDisplay.blit(B_image, [0, -180])


game_over = False

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

