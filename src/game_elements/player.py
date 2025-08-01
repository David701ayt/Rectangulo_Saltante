# player.py
import pygame
# Importa las constantes definidas en el archivo constants.py.
from constants import ANCHO_PANTALLA, ALTO_PANTALLA, ROJO, GRAVEDAD, FUERZA_SALTO, VELOCIDAD_JUGADOR

class Jugador(pygame.sprite.Sprite):
    """
    Representa al personaje principal del juego.
    Hereda de pygame.sprite.Sprite para facilitar el manejo de sprites y colisiones.
    """
    def __init__(self):
        """
        Constructor de la clase Jugador.
        Inicializa la posición, tamaño, velocidad y estado del jugador.
        """
        super().__init__() # Llama al constructor de la clase padre (pygame.sprite.Sprite).
        self.ancho = 30    # Ancho del jugador.
        self.alto = 50     # Alto del jugador.
        # Crea un objeto Surface para dibujar el jugador (un rectángulo rojo).
        self.image = pygame.Surface([self.ancho, self.alto])
        self.image.fill(ROJO) # Rellena la superficie con color rojo.
        # Crea un objeto Rect que representa la posición y tamaño del jugador.
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO_PANTALLA // 2 # Posición inicial X (centro de la pantalla).
        self.rect.bottom = ALTO_PANTALLA - 50  # Posición inicial Y (cerca del suelo).

        self.velocidad_x = 0 # Velocidad horizontal actual del jugador.
        self.velocidad_y = 0 # Velocidad vertical actual del jugador (afectada por gravedad y salto).
        self.en_suelo = False # Booleano para saber si el jugador está tocando una plataforma o el suelo.

    def update(self, plataformas):
        """
        Actualiza el estado del jugador en cada fotograma del juego.
        Aplica gravedad, maneja el movimiento horizontal y detecta colisiones.
        """
        # Aplica la gravedad a la velocidad vertical.
        self.velocidad_y += GRAVEDAD
        # Limita la velocidad de caída para evitar que sea infinita.
        if self.velocidad_y > 10:
            self.velocidad_y = 10

        # Mueve el jugador horizontalmente.
        self.rect.x += self.velocidad_x
        # Asegura que el jugador no salga de los límites horizontales de la pantalla.
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA

        # Mueve el jugador verticalmente.
        self.rect.y += self.velocidad_y
        self.en_suelo = False # Asume que el jugador no está en el suelo al inicio de la actualización.

        # Manejo de colisiones con plataformas
        # Itera sobre todas las plataformas para verificar si hay colisión.
        for plataforma in plataformas:
            # Si el jugador colisiona con una plataforma.
            if self.rect.colliderect(plataforma.rect):
                # Si el jugador estaba cayendo y colisiona con la parte superior de la plataforma.
                if self.velocidad_y > 0 and self.rect.bottom <= plataforma.rect.centery:
                    self.rect.bottom = plataforma.rect.top # Coloca al jugador justo encima de la plataforma.
                    self.velocidad_y = 0 # Detiene la caída.
                    self.en_suelo = True # El jugador está en el suelo.
                # Si el jugador estaba subiendo y colisiona con la parte inferior de la plataforma.
                elif self.velocidad_y < 0 and self.rect.top >= plataforma.rect.centery:
                    self.rect.top = plataforma.rect.bottom # Coloca al jugador justo debajo de la plataforma.
                    self.velocidad_y = 0 # Detiene el movimiento vertical.

        # Si el jugador cae por debajo de la pantalla, lo resetea a una posición inicial.
        # Esto es una forma simple de manejar la "muerte" o caída fuera del mapa.
        if self.rect.top > ALTO_PANTALLA:
            self.rect.centerx = ANCHO_PANTALLA // 2
            self.rect.bottom = ALTO_PANTALLA - 50
            self.velocidad_y = 0
            self.en_suelo = False # Reinicia el estado de suelo.

    def jump(self):
        """
        Hace que el jugador salte si está en el suelo.
        """
        if self.en_suelo: # Solo puede saltar si está tocando una plataforma o el suelo.
            self.velocidad_y = FUERZA_SALTO # Aplica la fuerza de salto hacia arriba.
            self.en_suelo = False # Ya no está en el suelo.

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

    def draw(self, superficie):
        """
        Dibuja al jugador en la superficie de la pantalla.
        """
        superficie.blit(self.image, self.rect) # Dibuja la imagen del jugador en su posición.
