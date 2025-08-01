# main.py
import pygame # Importa la biblioteca Pygame.

# Importa las clases y constantes de los módulos que hemos creado.
from constants import ANCHO_PANTALLA, ALTO_PANTALLA, AZUL, FPS
from game_elements.player import Jugador
from game_elements.platform import Plataforma

# 1. Inicialización de Pygame
pygame.init() # Inicializa todos los módulos de Pygame.

# 2. Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Plataformas Básico Modular") # Establece el título de la ventana.

# 3. Creación de objetos del juego
jugador = Jugador() # Crea una instancia del jugador.

# Crea un grupo de sprites para las plataformas.
plataformas = pygame.sprite.Group()
# Añade algunas plataformas al grupo.
plataformas.add(Plataforma(0, ALTO_PANTALLA - 20, ANCHO_PANTALLA, 20)) # Plataforma del suelo
plataformas.add(Plataforma(150, ALTO_PANTALLA - 100, 150, 20)) # Plataforma 1
plataformas.add(Plataforma(400, ALTO_PANTALLA - 200, 200, 20)) # Plataforma 2
plataformas.add(Plataforma(50, ALTO_PANTALLA - 300, 100, 20))  # Plataforma 3

# 4. Bucle principal del juego
corriendo = True # Variable de control para el bucle del juego.
reloj = pygame.time.Clock() # Objeto Clock para controlar la velocidad de fotogramas.

while corriendo:
    # 4.1. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.move_left() # Llama al método de movimiento a la izquierda del jugador.
            if evento.key == pygame.K_RIGHT:
                jugador.move_right() # Llama al método de movimiento a la derecha del jugador.
            if evento.key == pygame.K_SPACE:
                jugador.jump() # Llama a la función de salto del jugador.

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT and jugador.velocidad_x < 0:
                jugador.stop_x() # Detiene el movimiento horizontal si se suelta la flecha izquierda.
            if evento.key == pygame.K_RIGHT and jugador.velocidad_x > 0:
                jugador.stop_x() # Detiene el movimiento horizontal si se suelta la flecha derecha.

    # 4.2. Actualización del estado del juego
    jugador.update(plataformas) # Actualiza el estado del jugador, pasándole las plataformas.

    # 4.3. Dibujo de todos los elementos
    pantalla.fill(AZUL) # Rellena la pantalla con un color de fondo.

    # Dibuja todas las plataformas.
    for plataforma in plataformas:
        plataforma.draw(pantalla)

    jugador.draw(pantalla) # Dibuja al jugador.

    # 4.4. Actualiza la pantalla.
    pygame.display.flip()

    # 4.5. Controla la velocidad de fotogramas.
    reloj.tick(FPS)

# 5. Finalización de Pygame
pygame.quit()
