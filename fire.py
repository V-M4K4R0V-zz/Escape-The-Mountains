

















































weapon = pygame.image.load('C:\\Users\\ahmed\\Desktop\\work\\Escape-The-Mountains\\characters\\spear.png')

bullX = True
B_X_move = True
bull_state = "ready"

def fire_cordinates(x,y):
    gDisplay.blit(weapon, (x, y))
    bull_state = "fire"
    gDisplay.blit(weapon, (bullX, bullY + 15))

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_Space:
        fire_cordinates(bullX, playerY)

if bull_state is "fire":
    fire_cordinates(bullX, playerY)
    bullX -= B_X_move