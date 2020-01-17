#jump space
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            playerY_ch = -3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            playerY_ch = 3
            break
    