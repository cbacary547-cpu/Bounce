import pygame


class obstacle_sommet:

  def __init__(self, sommets, couleur=(250, 0, 0)):
    self.sommets = sommets
    self.couleur = couleur
    self.a_touche = False

    xs = [p[0] for p in sommets]
    ys = [p[1] for p in sommets]
    self.rect = pygame.Rect(
        min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
    )

  def verifier_collision(self, balle):
    balle_rect = pygame.Rect(
        balle.position.x - balle.rayon,
        balle.position.y - balle.rayon,
        balle.rayon * 2,
        balle.rayon * 2,
    )

    if self.rect.colliderect(balle_rect):
      if not self.a_touche:
        self.a_touche = True
        return True
    else:
      self.a_touche = False

    return False

  def dessiner(self, ecran, camera):
    pygame.draw.polygon(
        ecran, self.couleur, camera.appliquer_sommets(self.sommets)
    )