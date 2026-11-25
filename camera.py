import pygame


class Camera:

  def __init__(self, largeur_ecran=1000, limite_gauche=0, limite_droite=None):
    self.x = 0
    self.largeur_ecran = largeur_ecran
    self.demi_largeur = largeur_ecran / 2
    self.limite_gauche = limite_gauche
    self.limite_droite = limite_droite

  def suivre(self, balle):
    """Met à jour la position de la caméra pour centrer la balle."""
    self.x = balle.position.x - self.demi_largeur

    if self.limite_gauche is not None:
      self.x = max(self.limite_gauche, self.x)
    if self.limite_droite is not None:
      self.x = min(self.limite_droite - self.largeur_ecran, self.x)

  def appliquer_point(self, position):
    """Décale un Vector2 ou un tuple (x, y) pour l'affichage."""
    return (position[0] - self.x, position[1])

  def appliquer_rect(self, rect):
    """Renvoie une copie décalée d'un pygame.Rect."""
    return rect.move(-self.x, 0)

  def appliquer_sommets(self, sommets):
    """Renvoie une liste de sommets décalés pour un polygone."""
    return [(x - self.x, y) for (x, y) in sommets]