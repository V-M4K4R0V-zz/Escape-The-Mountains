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

#player
player = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\warrior.png')
playerX = 300
playerY = 40
playerX_ch=0
def player_fu(x,y):
    gDisplay.blit(player, (x, y))

run = True
while run:
    #background
    background = "C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\pixie.png"
    B_image = pygame.image.load(background)
    gDisplay.blit(B_image, [0, -180])
    #
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        #keyboard input algo
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerX_ch = 0.2
            if event.type == pygame.K_RIGHT:
                playerX_ch = 0.2
        if event.type == pygame.KEYUP:
            playerX_ch = 1
    playerY += playerX_ch
    player_fu(playerX, playerY)
    pygame.display.update()