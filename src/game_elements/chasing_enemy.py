# chasing_enemy.py
import pygame
from constants import MORADO, VELOCIDAD_ENEMIGO_SEGUIDOR, RANGO_DETECCION

class EnemigoSeguidor(pygame.sprite.Sprite):
    """
    Representa un enemigo que persigue al jugador cuando se acerca.
    """
    def __init__(self, x, y, ancho, alto):
        """
        Constructor de la clase EnemigoSeguidor.
        :param x: Posición inicial X.
        :param y: Posición inicial Y.
        :param ancho: Ancho del enemigo.
        :param alto: Alto del enemigo.
        """
        super().__init__()
        # Crea una superficie para el enemigo (un rectángulo morado).
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(MORADO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocidad_x = 0

    def update(self, jugador):
        """
        Actualiza el estado del enemigo. Comprueba si el jugador está
        dentro del rango de detección y lo persigue.
        :param jugador: Objeto del jugador para obtener su posición.
        """
        # Calcula la distancia horizontal al jugador.
        distancia_x = jugador.rect.centerx - self.rect.centerx

        # Comprueba si el jugador está dentro del rango de detección.
        if abs(distancia_x) < RANGO_DETECCION:
            # Si el jugador está a la derecha, se mueve a la derecha.
            if distancia_x > 0:
                self.velocidad_x = VELOCIDAD_ENEMIGO_SEGUIDOR
            # Si el jugador está a la izquierda, se mueve a la izquierda.
            elif distancia_x < 0:
                self.velocidad_x = -VELOCIDAD_ENEMIGO_SEGUIDOR
        else:
            # Si el jugador está fuera de rango, el enemigo se detiene.
            self.velocidad_x = 0
            
        self.rect.x += self.velocidad_x
