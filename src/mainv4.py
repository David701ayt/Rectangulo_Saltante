# main.py
import pygame # Importa la biblioteca Pygame.

# Importa las clases y constantes de los módulos.
from constants import ANCHO_PANTALLA, ALTO_PANTALLA, AZUL, BLANCO, FPS, PUNTOS_POR_OBJETO, PUNTOS_POR_ENEMIGO, PUNTOS_POR_ENEMIGO_SEGUIDOR
from game_elements.player import Jugador
from game_elements.platform import Plataforma
from game_elements.enemy import Enemigo
from game_elements.chasing_enemy import EnemigoSeguidor # ¡Importa el nuevo enemigo!
from game_elements.colectible import Objeto

# 1. Inicialización de Pygame
pygame.init()

# 2. Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Plataformas con Enemigos Mejorados y Puntuación")

puntuacion = 0
font = pygame.font.Font(None, 36)

# 3. Creación de objetos del juego
jugador = Jugador()

plataformas = pygame.sprite.Group()
plataformas.add(Plataforma(0, ALTO_PANTALLA - 20, ANCHO_PANTALLA, 20))
plataformas.add(Plataforma(150, ALTO_PANTALLA - 100, 150, 20))
plataformas.add(Plataforma(400, ALTO_PANTALLA - 200, 200, 20))
plataformas.add(Plataforma(50, ALTO_PANTALLA - 300, 100, 20))
plataformas.add(Plataforma(600, ALTO_PANTALLA - 350, 150, 20))
plataformas.add(Plataforma(300, ALTO_PANTALLA - 150, 50, 20))
plataformas.add(Plataforma(300, ALTO_PANTALLA - 250, 20, 20))

enemigos = pygame.sprite.Group()
# Enemigos que se mueven de un lado a otro.
enemigos.add(Enemigo(150, ALTO_PANTALLA - 150, 40, 40, 150, 250))
enemigos.add(Enemigo(450, ALTO_PANTALLA - 250, 40, 40, 450, 550))
# Nuevos enemigos que persiguen al jugador.
enemigos.add(EnemigoSeguidor(650, ALTO_PANTALLA - 400, 40, 40))
enemigos.add(EnemigoSeguidor(300, ALTO_PANTALLA - 350, 40, 40))

objetos = pygame.sprite.Group()
objetos.add(Objeto(200, ALTO_PANTALLA - 130, 20, 20))
objetos.add(Objeto(500, ALTO_PANTALLA - 230, 20, 20))
objetos.add(Objeto(80, ALTO_PANTALLA - 330, 20, 20))
objetos.add(Objeto(680, ALTO_PANTALLA - 380, 20, 20))

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

    enemigos.empty()
    enemigos.add(Enemigo(150, ALTO_PANTALLA - 150, 40, 40, 150, 250))
    enemigos.add(Enemigo(450, ALTO_PANTALLA - 250, 40, 40, 450, 550))
    enemigos.add(EnemigoSeguidor(650, ALTO_PANTALLA - 400, 40, 40))
    enemigos.add(EnemigoSeguidor(300, ALTO_PANTALLA - 350, 40, 40))
    
    objetos.empty()
    objetos.add(Objeto(200, ALTO_PANTALLA - 130, 20, 20))
    objetos.add(Objeto(500, ALTO_PANTALLA - 230, 20, 20))
    objetos.add(Objeto(80, ALTO_PANTALLA - 330, 20, 20))
    objetos.add(Objeto(680, ALTO_PANTALLA - 380, 20, 20))

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
    
    # Actualiza todos los enemigos en el grupo.
    for enemigo in enemigos:
        if isinstance(enemigo, EnemigoSeguidor):
            # Si es un enemigo seguidor, le pasamos el objeto 'jugador' para que pueda rastrearlo.
            enemigo.update(jugador)
        else:
            # Si es un enemigo normal, su método 'update' no requiere el jugador.
            enemigo.update()

    # 4.3. Detección de colisiones
    objetos_recogidos = pygame.sprite.spritecollide(jugador, objetos, True)
    for obj in objetos_recogidos:
        puntuacion += PUNTOS_POR_OBJETO
        print(f"Puntuación: {puntuacion}")

    colisiones_enemigos = pygame.sprite.spritecollide(jugador, enemigos, False)
    if colisiones_enemigos:
        for enemigo in colisiones_enemigos:
            # Colisión para derrotar al enemigo saltando sobre él.
            if jugador.velocidad_y > 0 and jugador.rect.bottom <= enemigo.rect.centery + 10:
                enemigo.kill()
                # Aplica una puntuación diferente según el tipo de enemigo.
                puntuacion += PUNTOS_POR_ENEMIGO_SEGUIDOR if isinstance(enemigo, EnemigoSeguidor) else PUNTOS_POR_ENEMIGO
                print(f"¡Enemigo derrotado! Puntuación: {puntuacion}")
                jugador.velocidad_y = -5 # Rebote del jugador
            else:
                # Si choca por los lados o por abajo, el juego se reinicia.
                print("¡Game Over!")
                reset_game()

    # 4.4. Dibujo de todos los elementos
    pantalla.fill(AZUL)

    plataformas.draw(pantalla)
    enemigos.draw(pantalla)
    objetos.draw(pantalla)
    jugador.draw(pantalla)

    draw_score(pantalla, puntuacion)

    # 4.5. Actualiza la pantalla.
    pygame.display.flip()

    # 4.6. Controla la velocidad de fotogramas.
    reloj.tick(FPS)

# 5. Finalización de Pygame
pygame.quit()
