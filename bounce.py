import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
running = True
player_position = pygame.Vector2(screen.get_width() /2 - 260, screen.get_height() / 2 + 150) 
dt = 0
plafond  = pygame.Rect (0, 0, 1000, 100)
sol = pygame.Rect (0, 600, 1000, 100)
mur_cote = pygame.Rect (0 ,0, 200, 700)
balle = pygame.Rect(  0 ,  0 , 80 , 80 )
obstacles = [plafond, sol, mur_cote]
balle.center = player_position
vitesse = pygame.Vector2(0, 0)
gravite = 1000
est_au_sol = False


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ancienne_pos = player_position.copy()

    keys = pygame.key.get_pressed()   
   # déplacements vertical + gravité
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and est_au_sol:
        vitesse.y = -500
        est_au_sol = False
  # déplacements horizontaux 
    if keys[pygame.K_RIGHT]:                 #droite
            player_position.x += 300 * dt
    if keys[pygame.K_LEFT]:                  #gauche
            player_position.x -= 300 * dt


    balle.center = player_position
    if balle.colliderect(mur_cote):
        player_position.x = ancienne_pos.x
        balle.center = player_position
   
    balle.center = player_position
    vitesse.y += gravite * dt
    player_position.y += vitesse.y * dt
    balle.center = player_position

    if balle.colliderect(plafond):
       balle.top = plafond.bottom
       player_position.y = balle.centery
       vitesse.y = 0


    if balle.colliderect(sol):
      balle.bottom = sol.top
      player_position.y = balle.centery
      vitesse.y = 0
      est_au_sol = True


    screen.fill("blue")
    pygame.draw.circle(screen, "green", player_position , 40)    # Balle verte
    pygame.draw.rect(screen, (250, 0, 0), plafond)       
    pygame.draw.rect(screen, (250, 0, 0), mur_cote)
    pygame.draw.rect(screen, (250, 0, 0), sol)
    pygame.draw.rect(screen, (0, 0, 0), balle, 2)
    
    
    
    pygame.display.flip()
    dt = clock.tick(60)/1000  #60 FPS  
    
pygame.quit()

