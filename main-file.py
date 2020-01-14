import pygame
import sys

pygame.init()

gDisplay = pygame.display.set_mode((600,700))
pygame.display.set_caption('Escape The Mountain')

icon = "C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\icon.png"

pygame.display.set_icon(icon)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
