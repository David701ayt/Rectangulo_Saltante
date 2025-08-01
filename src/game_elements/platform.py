# platform.py
import pygame
# Importa el color VERDE de las constantes.
from constants import VERDE

class Plataforma(pygame.sprite.Sprite):
    """
    Representa una plataforma en el juego.
    Hereda de pygame.sprite.Sprite para facilitar el manejo de sprites y colisiones.
    """
    def __init__(self, x, y, ancho, alto):
        """
        Constructor de la clase Plataforma.
        Inicializa la posición y tamaño de la plataforma.
        """
        super().__init__() # Llama al constructor de la clase padre.
        # Crea una superficie para la plataforma (un rectángulo verde).
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(VERDE) # Rellena la superficie con color verde.
        # Crea un objeto Rect para la posición y tamaño de la plataforma.
        self.rect = self.image.get_rect()
        self.rect.x = x # Posición X de la plataforma.
        self.rect.y = y # Posición Y de la plataforma.

    def draw(self, superficie):
        """
        Dibuja la plataforma en la superficie de la pantalla.
        """
        superficie.blit(self.image, self.rect) # Dibuja la imagen de la plataforma.
