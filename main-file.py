import pygame
import sys
import pygameMenu

pygame.init()

#window
screen_s = (1300, 760)
gDisplay = pygame.display.set_mode(screen_s)
pygame.display.set_caption('Escape The Mountain')

#icon
icon = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\backgrounds\\mountain.png')
pygame.display.set_icon(icon)

#player
player = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\characters\\demon1.png')
playerX = 300
playerY = 40

"""
#player 2
player2 = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\ric.png')
playerX2 = 50
playerY2 = 20
def player_fu2(x,y):
    gDisplay.blit(player2, (x, y))
"""
#PLAYER1 XY
def player_fu(x,y):
    gDisplay.blit(player, (x, y))

move = 8

run = True
while run:
    #background
    background = "C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\backgrounds\\The_Hell.png"
    B_image = pygame.image.load(background)
    gDisplay.blit(B_image, [0, -0])
    #
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    #moving X;
    if keys[pygame.K_LEFT] and playerX > 2:
        playerX -= move
    if keys[pygame.K_RIGHT] and playerX < 1200:
        playerX += move
    #MOVING Y;
    if keys[pygame.K_UP] and playerY > 2:
        playerY -= move
    if keys[pygame.K_DOWN] and playerY < 401:
        playerY += move

    player_fu(playerX, playerY)


    """
        #REC player2
        
        #moving X;
        if keys[pygame.K_LEFT] and playerX2 > 2:
            playerX2 -= move
        if keys[pygame.K_RIGHT] and playerX2 < 1200:
            playerX2 += move
        
        #MOVING Y;
        if keys[pygame.K_UP] and playerY2 > 2:
            playerY2 -= move
        if keys[pygame.K_DOWN] and playerY2 < 401:
            playerY2 += move
        player_fu2(playerX2, playerY2)
        """
        
    pygame.display.update()