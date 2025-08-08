# collectible.py
import pygame
from constants import COLLECTIBLE_SPRITE

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
        # Carga la imagen del objeto. Asegúrate de tener el archivo correcto.
        try:
            self.image = pygame.image.load(COLLECTIBLE_SPRITE).convert_alpha()
        except pygame.error as message:
            print(f"No se pudo cargar la imagen: {COLLECTIBLE_SPRITE}")
            raise SystemExit(message)
        # Escala la imagen para que tenga un tamaño apropiado.
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
