# main.py
import pygame # Importa la biblioteca Pygame.

# Importa las clases y constantes de los módulos.
from constants import ANCHO_PANTALLA, ALTO_PANTALLA, AZUL, FPS
from game_elements.player import Jugador
from game_elements.platform import Plataforma
from game_elements.enemy import Enemigo # ¡Nueva clase importada!

# 1. Inicialización de Pygame
pygame.init() # Inicializa todos los módulos de Pygame.

# 2. Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Plataformas con Enemigos") # Nuevo título.

# 3. Creación de objetos del juego
jugador = Jugador() # Crea una instancia del jugador.

# Crea un grupo de sprites para las plataformas.
plataformas = pygame.sprite.Group()
# Añade algunas plataformas al grupo.
plataformas.add(Plataforma(0, ALTO_PANTALLA - 20, ANCHO_PANTALLA, 20)) # Plataforma del suelo
plataformas.add(Plataforma(150, ALTO_PANTALLA - 100, 150, 20)) # Plataforma 1
plataformas.add(Plataforma(400, ALTO_PANTALLA - 200, 200, 20)) # Plataforma 2
plataformas.add(Plataforma(50, ALTO_PANTALLA - 300, 180, 99))  # Plataforma 3

# Creación de enemigos
enemigos = pygame.sprite.Group() # Crea un nuevo grupo de sprites para los enemigos.
# Añade un enemigo que se mueve entre las coordenadas 150 y 250.
enemigos.add(Enemigo(150, ALTO_PANTALLA - 150, 40, 40, 150, 250))
# Añade un segundo enemigo en otra posición.
enemigos.add(Enemigo(450, ALTO_PANTALLA - 250, 40, 40, 450, 550))


# 4. Bucle principal del juego
corriendo = True # Variable de control para el bucle del juego.
reloj = pygame.time.Clock() # Objeto Clock para controlar la velocidad de fotogramas.

def reset_game():
    """
    Función para reiniciar el juego si el jugador pierde.
    """
    jugador.rect.centerx = ANCHO_PANTALLA // 2
    jugador.rect.bottom = ALTO_PANTALLA - 50
    jugador.velocidad_y = 0

while corriendo:
    # 4.1. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.move_left()
            if evento.key == pygame.K_RIGHT:
                jugador.move_right()
            if evento.key == pygame.K_SPACE:
                jugador.jump()

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT and jugador.velocidad_x < 0:
                jugador.stop_x()
            if evento.key == pygame.K_RIGHT and jugador.velocidad_x > 0:
                jugador.stop_x()

    # 4.2. Actualización del estado del juego
    jugador.update(plataformas) # Actualiza el estado del jugador.
    enemigos.update() # Actualiza el estado de los enemigos.

    # 4.3. Detección de colisiones
    # Usa pygame.sprite.spritecollide para verificar si el jugador choca con algún enemigo.
    # El tercer argumento "False" indica que los sprites de los enemigos no deben ser eliminados.
    colisiones_enemigos = pygame.sprite.spritecollide(jugador, enemigos, False)
    if colisiones_enemigos:
        print("¡Game Over!")
        reset_game() # Reinicia la posición del jugador.

    # 4.4. Dibujo de todos los elementos
    pantalla.fill(AZUL) # Rellena la pantalla con un color de fondo.

    # Dibuja todas las plataformas y enemigos.
    plataformas.draw(pantalla)
    enemigos.draw(pantalla)
    jugador.draw(pantalla)

    # 4.5. Actualiza la pantalla.
    pygame.display.flip()

    # 4.6. Controla la velocidad de fotogramas.
    reloj.tick(FPS)

# 5. Finalización de Pygame
pygame.quit()
