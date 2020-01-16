import pygame
import sys
import pygameMenu

pygame.init()

#window
screen_s = (1300, 760)
gDisplay = pygame.display.set_mode(screen_s)
pygame.display.set_caption('Escape The Mountain')

#icon
icon = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\mountain.png')
pygame.display.set_icon(icon)

#player
player = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\123.png')
playerX = 300
playerY = 40
playerX_ch = 0
playerY_ch = 0

"""
#player rich
player2 = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\ric.png')
playerX1 = 50
playerY1 = 20
def player2_fu(x,y):
    gDisplay.blit(player2, (x, y))
"""

def player_fu(x,y):
    gDisplay.blit(player, (x, y))



run = True
while run:
    #background
    background = "C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\The_Hell.png"
    B_image = pygame.image.load(background)
    gDisplay.blit(B_image, [0, -0])
    #
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        #keyboard input algo for X
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_ch = -8
            if event.key == pygame.K_RIGHT:
                playerX_ch = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_ch = 0

        #keyboard input algo for Y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_ch = -8
            if event.key == pygame.K_DOWN:
                playerY_ch = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_ch = 0
        """
        #REC
        #keyboard input algo for X
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX1 += -8
            if event.key == pygame.K_d:
                playerX1 += 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX1

        #keyboard input algo for Y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY1 += -8
            if event.key == pygame.K_s:
                playerY1 += 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY1
        """


    #window wall
    if playerX >= 1360:
        playerX = 530
    elif playerY >= 760:
        playerY = 615
    elif playerX <= 0:
        playerX = 10
    elif playerY <= 0:
        playerY = 10
    else: #moving
        playerY += playerY_ch
        playerX += playerX_ch
        player_fu(playerX, playerY)
        #player2_fu(playerX1, playerY1)
        
    pygame.display.update()