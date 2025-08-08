# player.py
import pygame
from constants import (
    ANCHO_PANTALLA, ALTO_PANTALLA, GRAVEDAD, FUERZA_SALTO, VELOCIDAD_JUGADOR,
    PLAYER_IDLE_SPRITE, PLAYER_RUN_SPRITES, PLAYER_JUMP_SPRITE, ANIMATION_SPEED
)

class Jugador(pygame.sprite.Sprite):
    """
    Representa al personaje principal del juego con animaciones.
    """
    def __init__(self):
        """
        Constructor de la clase Jugador.
        Carga todas las imágenes de animación y las inicializa.
        """
        super().__init__()
        self.ancho = 50
        self.alto = 70

        # Diccionario para almacenar todas las animaciones.
        self.animations = {}
        self.current_animation_frame = 0 # Índice del frame actual de la animación.
        self.animation_counter = 0       # Contador para controlar la velocidad de la animación.
        self.facing_right = True         # Dirección a la que mira el jugador.

        # Cargar imágenes de animación
        try:
            # Animación de IDLE (quieto)
            self.animations["idle"] = pygame.transform.scale(
                pygame.image.load(PLAYER_IDLE_SPRITE).convert_alpha(), (self.ancho, self.alto)
            )
            # Animación de RUN (correr)
            self.animations["run"] = [
                pygame.transform.scale(pygame.image.load(img).convert_alpha(), (self.ancho, self.alto))
                for img in PLAYER_RUN_SPRITES
            ]
            # Animación de JUMP (saltar)
            self.animations["jump"] = pygame.transform.scale(
                pygame.image.load(PLAYER_JUMP_SPRITE).convert_alpha(), (self.ancho, self.alto)
            )
        except pygame.error as message:
            print("Error al cargar las imágenes de animación del jugador. Asegúrate de que existen y están en la carpeta correcta.")
            raise SystemExit(message)

        # Establece la imagen inicial del jugador.
        self.image = self.animations["idle"]
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO_PANTALLA // 2
        self.rect.bottom = ALTO_PANTALLA - 50

        self.velocidad_x = 0
        self.velocidad_y = 0
        self.en_suelo = False

    def update(self, plataformas):
        """
        Actualiza el estado y la animación del jugador en cada fotograma.
        """
        # --- Lógica de movimiento y colisiones (sin cambios) ---
        self.velocidad_y += GRAVEDAD
        if self.velocidad_y > 10:
            self.velocidad_y = 10

        self.rect.x += self.velocidad_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA

        self.rect.y += self.velocidad_y
        self.en_suelo = False

        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.velocidad_y > 0 and self.rect.bottom <= plataforma.rect.centery + 10:
                    self.rect.bottom = plataforma.rect.top
                    self.velocidad_y = 0
                    self.en_suelo = True
                elif self.velocidad_y < 0 and self.rect.top >= plataforma.rect.centery - 10:
                    self.rect.top = plataforma.rect.bottom
                    self.velocidad_y = 0

        if self.rect.top > ALTO_PANTALLA:
            self.rect.centerx = ANCHO_PANTALLA // 2
            self.rect.bottom = ALTO_PANTALLA - 50
            self.velocidad_y = 0
            self.en_suelo = False
        # --- Fin de lógica de movimiento y colisiones ---

        # --- Lógica de animación ---
        self.animation_counter += 1
        if self.animation_counter >= ANIMATION_SPEED:
            self.animation_counter = 0
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.animations["run"])

        if not self.en_suelo:
            # Si no está en el suelo, está saltando o cayendo.
            self.image = self.animations["jump"]
        elif self.velocidad_x != 0:
            # Si se está moviendo horizontalmente, está corriendo.
            self.image = self.animations["run"][self.current_animation_frame]
        else:
            # Si está en el suelo y no se mueve, está quieto.
            self.image = self.animations["idle"]

        # Voltear la imagen si el jugador cambia de dirección
        if self.velocidad_x < 0 and self.facing_right:
            self.facing_right = False
            # Voltea todas las imágenes de animación para que miren a la izquierda.
            for key in self.animations:
                if isinstance(self.animations[key], list):
                    self.animations[key] = [pygame.transform.flip(img, True, False) for img in self.animations[key]]
                else:
                    self.animations[key] = pygame.transform.flip(self.animations[key], True, False)
        elif self.velocidad_x > 0 and not self.facing_right:
            self.facing_right = True
            # Voltea todas las imágenes de animación para que miren a la derecha.
            for key in self.animations:
                if isinstance(self.animations[key], list):
                    self.animations[key] = [pygame.transform.flip(img, True, False) for img in self.animations[key]]
                else:
                    self.animations[key] = pygame.transform.flip(self.animations[key], True, False)
        # --- Fin de lógica de animación ---

    def jump(self):
        """
        Hace que el jugador salte si está en el suelo.
        """
        if self.en_suelo:
            self.velocidad_y = FUERZA_SALTO
            self.en_suelo = False
            # Al saltar, resetea el contador de animación para que el sprite de salto se muestre inmediatamente.
            self.animation_counter = 0

    def stop_x(self):
        """
        Detiene el movimiento horizontal del jugador.
        """
        self.velocidad_x = 0

    def move_left(self):
        """
        Establece la velocidad para mover al jugador a la izquierda.
        """
        self.velocidad_x = -VELOCIDAD_JUGADOR

    def move_right(self):
        """
        Establece la velocidad para mover al jugador a la derecha.
        """
        self.velocidad_x = VELOCIDAD_JUGADOR
