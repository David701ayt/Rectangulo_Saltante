# collectible.py
import pygame
from constants import AMARILLO

class Objeto(pygame.sprite.Sprite):
    """
    Representa un objeto coleccionable en el juego.
    """
    def __init__(self, x, y, ancho, alto):
        """
        Constructor de la clase Objeto.
        :param x: Posición inicial X.
        :param y: Posición inicial Y.
        :param ancho: Ancho del objeto.
        :param alto: Alto del objeto.
        """
        super().__init__()
        # Crea una superficie para el objeto (un rectángulo amarillo).
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
