# platform.py
import pygame
from constants import PLATFORM_SPRITE # Importa la ruta del sprite de la plataforma

class Plataforma(pygame.sprite.Sprite):
    """
    Representa una plataforma en el juego.
    Hereda de pygame.sprite.Sprite para facilitar el manejo de sprites y colisiones.
    """
    def __init__(self, x, y, ancho, alto):
        """
        Constructor de la clase Plataforma.
        Inicializa la posición y tamaño de la plataforma, y carga su imagen.
        """
        super().__init__()
        # Carga la imagen de la plataforma. Asegúrate de tener el archivo correcto.
        try:
            self.image = pygame.image.load(PLATFORM_SPRITE).convert_alpha()
        except pygame.error as message:
            print(f"No se pudo cargar la imagen: {PLATFORM_SPRITE}")
            raise SystemExit(message)
        # Escala la imagen para que coincida con el ancho y alto deseados de la plataforma.
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y