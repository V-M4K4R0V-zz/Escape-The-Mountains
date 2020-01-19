import pygame
import sys
import pygameMenu
import random

pygame.init()

#window
screen_s = (1300, 760)
gDisplay = pygame.display.set_mode((screen_s)) #, pygame.FULLSCREEN)
pygame.display.set_caption('Escape The Mountain')

#game icon
icon = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\backgrounds\\mountain.png')
pygame.display.set_icon(icon)
#--------------------------------------------OBJECTS-------------------------------------------#
#--------------------------------------------player
player = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\characters\\demon1.png')
playerX = 350
playerY = 401
#--------------------------------------------enemy 1
enemy = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\characters\\warrior.png')
enemyX = random.randint(0, 1260)
enemyY = 401
#--------------------------------------------enemy 2
enemy2 = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\characters\\warrior.png')
enemyX2 = random.randint(0, 1260)
enemyY2 = 401
#--------------------------------------------weapons-------------------------------------------#
weapon = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\characters\\spear.png')

#PLAYER1 
def player_fu(x,y):
    gDisplay.blit(player, (x, y))

move = 8
run = True
jump = True

while run:
    #background
    background = "C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\backgrounds\\The_Hell.png"
    B_image = pygame.image.load(background)
    gDisplay.blit(B_image, [0, -0])
    #
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
    #------------------------------PLAYER MOVEMENT----------------------------------------#
    keys = pygame.key.get_pressed()
    #moving X;
    if keys[pygame.K_LEFT] and playerX > 2:
        playerX -= move
    if keys[pygame.K_RIGHT] and playerX < 1200:
        playerX += move
    """
    #MOVING Y;
    if keys[pygame.K_UP] and playerY > 2:
        playerY -= move
    if keys[pygame.K_DOWN] and playerY < 401:
        playerY += move
    """
    #jumping 
    if keys[pygame.K_SPACE]:
        jump = playerY - 30
        playerY = jump   
    elif playerY > 2 and playerY < 401:
        playerY += 10
        jump = False

    #-------------------weapon inc
    forward = True
    if keys[pygame.K_c]:
        forward = playerX + 20
        gDisplay.blit(weapon, (forward, playerY + 15))
    elif forward > 2 and forward < 1200:
        forward += 50 
        gDisplay.blit(weapon, (forward, playerY + 15))
    #------------------------------ENEMY1-----------------------------------------#
    #enemyX = random.randint(0, 1300)
    #enemyY = 401
    #------------------------------ENEMY2-----------------------------------------#
    #enemyX2 = random.randint(0, 1300)
    #enemyY2 = 401
    #-----------------------------------------------------------------------------#
    
    gDisplay.blit(enemy, (enemyX, enemyY))
    gDisplay.blit(enemy2, (enemyX2, enemyY2))
    player_fu(playerX, playerY)
    
    #screen update  
    pygame.display.update()