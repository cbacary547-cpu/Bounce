import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
running = True
player_position = pygame.Vector2(screen.get_width() /2 - 260, screen.get_height() / 2 + 210)
dt = 0
plafond  = pygame.Rect (0, 0, 1000, 100)
sol = pygame.Rect (0, 600, 1000, 100)
mur_cote = pygame.Rect (0 ,0, 200, 700)
balle = pygame.Rect(  0 ,  0 , 80 , 80 )
obstacles = [plafond, sol, mur_cote]
balle.center = player_position

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ancienne_pos = player_position.copy()

    keys = pygame.key.get_pressed()   
    if keys[pygame.K_SPACE]:                 #saut
            player_position.y -= 300 * dt
    if keys[pygame.K_RIGHT]:                 #droite
            player_position.x += 300 * dt
    if keys[pygame.K_LEFT]:                  #gauche
            player_position.x -= 300 * dt
    if keys[pygame.K_DOWN]:                  #bas 
            player_position.y += 300 * dt
    if keys[pygame.K_UP]:                    #haut
                player_position.y -= 300 * dt
   
   
    balle.center = player_position
    if balle.collidelist(obstacles) != -1:
        player_position = ancienne_pos
        balle.center = player_position
    # couleur de fond
    screen.fill("blue")


    pygame.draw.circle(screen, "green", player_position , 40)    # Balle verte
    pygame.draw.rect(screen, (250, 0, 0), plafond)       
    pygame.draw.rect(screen, (250, 0, 0), mur_cote)
    pygame.draw.rect(screen, (250, 0, 0), sol)
    pygame.draw.rect(screen, (0, 0, 0), balle, 2)
    
    
    
    pygame.display.flip()
    dt = clock.tick(60)/1000  #60 FPS  
    
pygame.quit()