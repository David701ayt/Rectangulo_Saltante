# enemy.py
import pygame
from constants import VELOCIDAD_ENEMIGO, ENEMY_RUN_SPRITES, ANIMATION_SPEED

class Enemigo(pygame.sprite.Sprite):
    """
    Representa un enemigo en el juego que se mueve de un lado a otro con animaciones.
    """
    def __init__(self, x, y, ancho, alto, limite_izquierdo, limite_derecho):
        """
        Constructor de la clase Enemigo.
        Carga las imágenes de animación y las inicializa.
        """
        super().__init__()
        self.ancho = ancho
        self.alto = alto

        # Diccionario para almacenar las animaciones.
        self.animations = {}
        self.current_animation_frame = 0
        self.animation_counter = 0
        self.facing_right = True # Dirección a la que mira el enemigo.

        # Cargar imágenes de animación
        try:
            self.animations["run"] = [
                pygame.transform.scale(pygame.image.load(img).convert_alpha(), (self.ancho, self.alto))
                for img in ENEMY_RUN_SPRITES
            ]
        except pygame.error as message:
            print("Error al cargar las imágenes de animación del enemigo. Asegúrate de que existen y están en la carpeta correcta.")
            raise SystemExit(message)

        self.image = self.animations["run"][0] # Imagen inicial
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocidad_x = VELOCIDAD_ENEMIGO
        self.limite_izquierdo = limite_izquierdo
        self.limite_derecho = limite_derecho

    def update(self):
        """
        Actualiza el estado del enemigo, moviéndolo horizontalmente y actualizando su animación.
        """
        self.rect.x += self.velocidad_x

        # Cambiar dirección si alcanza los límites
        if self.rect.right > self.limite_derecho:
            self.velocidad_x = -VELOCIDAD_ENEMIGO
            self.facing_right = False # Mira a la izquierda
            # Voltear las imágenes de animación si es necesario
            for i, img in enumerate(self.animations["run"]):
                self.animations["run"][i] = pygame.transform.flip(img, True, False)
        elif self.rect.left < self.limite_izquierdo:
            self.velocidad_x = VELOCIDAD_ENEMIGO
            self.facing_right = True # Mira a la derecha
            # Voltear las imágenes de animación si es necesario
            for i, img in enumerate(self.animations["run"]):
                self.animations["run"][i] = pygame.transform.flip(img, True, False)

        # Lógica de animación
        self.animation_counter += 1
        if self.animation_counter >= ANIMATION_SPEED:
            self.animation_counter = 0
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.animations["run"])
        
        self.image = self.animations["run"][self.current_animation_frame]
