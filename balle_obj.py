import pygame


class Balle:
    """Balle contrôlée par le joueur."""

    def __init__(self, x, y, rayon=40, couleur="green", vitesse=300):
        self.position = pygame.Vector2(x, y)
        self.rayon = rayon
        self.couleur = couleur
        self.vitesse = vitesse
        # Rectangle de collision (carré de 2 x rayon autour de la balle)
        self.rect = pygame.Rect(0, 0, rayon * 2, rayon * 2)
        self.rect.center = self.position

    def lire_touches(self):
        """Retourne la direction voulue selon les touches (vecteur)."""
        touches = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)
        if touches[pygame.K_RIGHT]:
            direction.x += 1
        if touches[pygame.K_LEFT]:
            direction.x -= 1
        if touches[pygame.K_DOWN]:
            direction.y += 1
        if touches[pygame.K_UP] or touches[pygame.K_SPACE]:
            direction.y -= 1
        return direction

    def deplacer(self, dt, obstacles):
        """Déplace la balle, axe par axe, en annulant le mouvement si collision."""
        direction = self.lire_touches()

        # Axe X
        ancien_x = self.position.x
        self.position.x += direction.x * self.vitesse * dt
        self.rect.center = self.position
        if self.rect.collidelist(obstacles) != -1:
            self.position.x = ancien_x

        # Axe Y
        ancien_y = self.position.y
        self.position.y += direction.y * self.vitesse * dt
        self.rect.center = self.position
        if self.rect.collidelist(obstacles) != -1:
            self.position.y = ancien_y

        self.rect.center = self.position

    def dessiner(self, ecran):
        """Dessine la balle et son rectangle de collision."""
        pygame.draw.circle(ecran, self.couleur, self.position, self.rayon)
        pygame.draw.rect(ecran, (0, 0, 0), self.rect, 2)


# --- Initialisation ---
pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

plafond = pygame.Rect(0, 0, 1000, 100)
sol = pygame.Rect(0, 600, 1000, 100)
mur_cote = pygame.Rect(0, 0, 200, 700)
obstacles = [plafond, sol, mur_cote]

balle = Balle(screen.get_width() / 2 - 260, screen.get_height() / 2 + 210)

running = True
dt = 0

# --- Boucle principale ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    balle.deplacer(dt, obstacles)

    screen.fill("blue")
    for obstacle in obstacles:
        pygame.draw.rect(screen, (250, 0, 0), obstacle)
    balle.dessiner(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()