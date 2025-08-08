# chasing_enemy.py
import pygame
from constants import VELOCIDAD_ENEMIGO_SEGUIDOR, RANGO_DETECCION, CHASING_ENEMY_SPRITE

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
        # Carga la imagen del enemigo seguidor. Asegúrate de tener "chasing_enemy.png" en la carpeta.
        try:
            self.image = pygame.image.load(CHASING_ENEMY_SPRITE).convert_alpha()
        except pygame.error as message:
            print(f"No se pudo cargar la imagen: {CHASING_ENEMY_SPRITE}")
            raise SystemExit(message)
        # Escala la imagen para que tenga un tamaño apropiado.
        self.image = pygame.transform.scale(self.image, (ancho, alto))
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
        distancia_x = jugador.rect.centerx - self.rect.centerx

        if abs(distancia_x) < RANGO_DETECCION:
            if distancia_x > 0:
                self.velocidad_x = VELOCIDAD_ENEMIGO_SEGUIDOR
            elif distancia_x < 0:
                self.velocidad_x = -VELOCIDAD_ENEMIGO_SEGUIDOR
        else:
            self.velocidad_x = 0
            
        self.rect.x += self.velocidad_x
