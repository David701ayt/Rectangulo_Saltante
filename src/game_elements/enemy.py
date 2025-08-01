# enemy.py
import pygame
from constants import AZUL_OSCURO, VELOCIDAD_ENEMIGO

class Enemigo(pygame.sprite.Sprite):
    """
    Representa un enemigo en el juego.
    Se mueve horizontalmente de forma automática dentro de un rango definido.
    """
    def __init__(self, x, y, ancho, alto, limite_izquierdo, limite_derecho):
        """
        Constructor de la clase Enemigo.
        :param x: Posición inicial X.
        :param y: Posición inicial Y.
        :param ancho: Ancho del enemigo.
        :param alto: Alto del enemigo.
        :param limite_izquierdo: Límite izquierdo del área de movimiento del enemigo.
        :param limite_derecho: Límite derecho del área de movimiento del enemigo.
        """
        super().__init__()
        # Crea una superficie para el enemigo (un rectángulo azul oscuro).
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(AZUL_OSCURO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocidad_x = VELOCIDAD_ENEMIGO # Velocidad inicial del enemigo.
        self.limite_izquierdo = limite_izquierdo
        self.limite_derecho = limite_derecho

    def update(self):
        """
        Actualiza el estado del enemigo, moviéndolo horizontalmente.
        Cambia de dirección al llegar a los límites definidos.
        """
        self.rect.x += self.velocidad_x

        # Si el enemigo alcanza el límite derecho, cambia de dirección.
        if self.rect.right > self.limite_derecho:
            self.velocidad_x = -VELOCIDAD_ENEMIGO

        # Si el enemigo alcanza el límite izquierdo, cambia de dirección.
        if self.rect.left < self.limite_izquierdo:
            self.velocidad_x = VELOCIDAD_ENEMIGO
