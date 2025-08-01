# main.py
import pygame # Importa la biblioteca Pygame.

# Importa las clases y constantes de los módulos.
from constants import ANCHO_PANTALLA, ALTO_PANTALLA, AZUL, BLANCO, FPS, PUNTOS_POR_OBJETO, PUNTOS_POR_ENEMIGO
from game_elements.player import Jugador
from game_elements.platform import Plataforma
from game_elements.enemy import Enemigo
from game_elements.colectible import Objeto # ¡Nueva clase importada!

# 1. Inicialización de Pygame
pygame.init() # Inicializa todos los módulos de Pygame.

# 2. Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Plataformas con Puntuación y Enemigos")

# Inicializa la puntuación del juego.
puntuacion = 0
# Crea una fuente para mostrar la puntuación.
font = pygame.font.Font(None, 36)

# 3. Creación de objetos del juego
jugador = Jugador()
#1 numero es distancia, el segundo es para altura, el 3 es para largo y el 4 es el ancho
plataformas = pygame.sprite.Group()
plataformas.add(Plataforma(0, ALTO_PANTALLA - 20, ANCHO_PANTALLA, 20)) 
plataformas.add(Plataforma(100, ALTO_PANTALLA - 100, 150, 20))
plataformas.add(Plataforma(400, ALTO_PANTALLA - 200, 300, 20))
plataformas.add(Plataforma(50, ALTO_PANTALLA - 300, 100, 20))
plataformas.add(Plataforma(300, ALTO_PANTALLA - 150, 50, 20))
plataformas.add(Plataforma(300, ALTO_PANTALLA - 250, 20, 20))


enemigos = pygame.sprite.Group()
enemigos.add(Enemigo(150, ALTO_PANTALLA - 150, 40, 40, 150, 250))
enemigos.add(Enemigo(450, ALTO_PANTALLA - 250, 40, 40, 450, 550))

# Creación de objetos coleccionables
objetos = pygame.sprite.Group() # Crea un nuevo grupo de sprites para los objetos.
objetos.add(Objeto(200, ALTO_PANTALLA - 130, 20, 20)) # Objeto sobre la plataforma 1
objetos.add(Objeto(500, ALTO_PANTALLA - 230, 20, 20)) # Objeto sobre la plataforma 2
objetos.add(Objeto(80, ALTO_PANTALLA - 330, 20, 20))  # Objeto sobre la plataforma 3

# 4. Bucle principal del juego
corriendo = True
reloj = pygame.time.Clock()

def reset_game():
    """
    Función para reiniciar el juego si el jugador pierde.
    También reinicia la puntuación y la posición de los objetos y enemigos.
    """
    global puntuacion
    puntuacion = 0
    jugador.rect.centerx = ANCHO_PANTALLA // 2
    jugador.rect.bottom = ALTO_PANTALLA - 50
    jugador.velocidad_y = 0

    # Reiniciar la posición y el estado de los enemigos y objetos si es necesario.
    # Por ahora, simplemente los volvemos a crear para simplificar.
    enemigos.empty()
    enemigos.add(Enemigo(150, ALTO_PANTALLA - 150, 40, 40, 150, 250))
    enemigos.add(Enemigo(450, ALTO_PANTALLA - 250, 40, 40, 450, 550))
    
    objetos.empty()
    objetos.add(Objeto(200, ALTO_PANTALLA - 130, 20, 20))
    objetos.add(Objeto(500, ALTO_PANTALLA - 230, 20, 20))
    objetos.add(Objeto(80, ALTO_PANTALLA - 330, 20, 20))

def draw_score(surface, score):
    """
    Dibuja la puntuación en la esquina superior izquierda de la pantalla.
    """
    text_surface = font.render(f"Puntuación: {score}", True, BLANCO)
    surface.blit(text_surface, (10, 10))

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
    jugador.update(plataformas)
    enemigos.update()

    # 4.3. Detección de colisiones
    
    # Colisión con objetos
    # Detecta colisiones entre el jugador y los objetos.
    # El tercer argumento 'True' elimina el objeto del grupo si hay una colisión.
    objetos_recogidos = pygame.sprite.spritecollide(jugador, objetos, True)
    for obj in objetos_recogidos:
        puntuacion += PUNTOS_POR_OBJETO # Suma puntos por cada objeto recogido.
        print(f"Puntuación: {puntuacion}")

    # Colisión con enemigos
    colisiones_enemigos = pygame.sprite.spritecollide(jugador, enemigos, False)
    if colisiones_enemigos:
        # Itera sobre los enemigos con los que el jugador ha colisionado.
        for enemigo in colisiones_enemigos:
            # Si el jugador está cayendo y su posición inferior está por encima del centro del enemigo,
            # significa que ha saltado sobre él.
            if jugador.velocidad_y > 0 and jugador.rect.bottom <= enemigo.rect.centery + 10:
                # El enemigo es derrotado.
                enemigo.kill() # Elimina al enemigo del grupo de sprites.
                puntuacion += PUNTOS_POR_ENEMIGO
                print(f"¡Enemigo derrotado! Puntuación: {puntuacion}")
                # Hacemos que el jugador rebote un poco.
                jugador.velocidad_y = -5
            else:
                # Si el jugador choca con el enemigo por los lados o por debajo, el jugador "muere".
                print("¡Game Over!")
                reset_game()

    # 4.4. Dibujo de todos los elementos
    pantalla.fill(AZUL)

    # Dibuja los grupos de sprites.
    plataformas.draw(pantalla)
    enemigos.draw(pantalla)
    objetos.draw(pantalla)
    jugador.draw(pantalla)

    # Dibuja la puntuación en la pantalla.
    draw_score(pantalla, puntuacion)

    # 4.5. Actualiza la pantalla.
    pygame.display.flip()

    # 4.6. Controla la velocidad de fotogramas.
    reloj.tick(FPS)

# 5. Finalización de Pygame
pygame.quit()
