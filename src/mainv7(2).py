# main.py
import pygame
import random

# Importa las clases y constantes de los módulos.
from constants import (
    ANCHO_PANTALLA, ALTO_PANTALLA, AZUL, BLANCO, FPS, NEGRO,
    PUNTOS_POR_OBJETO, PUNTOS_POR_ENEMIGO, PUNTOS_POR_ENEMIGO_SEGUIDOR,
    BG_MUSIC, JUMP_SOUND, ENEMY_DEFEAT_SOUND, MUSICA_VOLUMEN, EFECTO_VOLUMEN,
    BACKGROUND_IMAGE, FUERZA_SALTO, GRAVEDAD
)
from game_elements.player import Jugador
from game_elements.platform import Plataforma
from game_elements.enemy import Enemigo
from game_elements.chasing_enemy import EnemigoSeguidor
from game_elements.collectible import Objeto

# 1. Inicialización de Pygame y del mezclador de audio
pygame.init()
pygame.mixer.init()

# 2. Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Plataformas con Dificultad Progresiva")

# Inicialización de variables del juego
puntuacion = 0
nivel = 0
game_state = "menu"
num_monedas_nivel = 3

# Fuentes
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 36)

# 3. Carga de assets (audio y fondo)
try:
    pygame.mixer.music.load(BG_MUSIC)
    pygame.mixer.music.set_volume(MUSICA_VOLUMEN)
    jump_sound = pygame.mixer.Sound(JUMP_SOUND)
    jump_sound.set_volume(EFECTO_VOLUMEN)
    defeat_sound = pygame.mixer.Sound(ENEMY_DEFEAT_SOUND)
    defeat_sound.set_volume(EFECTO_VOLUMEN)
except pygame.error as message:
    print("Error al cargar los archivos de sonido. Asegúrate de que están en la misma carpeta.")
    print(message)
    jump_sound = None
    defeat_sound = None

try:
    background = pygame.image.load(BACKGROUND_IMAGE).convert()
    background = pygame.transform.scale(background, (ANCHO_PANTALLA, ALTO_PANTALLA))
except pygame.error as message:
    print(f"Error al cargar la imagen de fondo: {BACKGROUND_IMAGE}. Usando color de fondo azul.")
    print(message)
    background = None

# --- Lógica del juego ---
jugador = Jugador()
plataformas = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
objetos = pygame.sprite.Group()
plataforma_base = Plataforma(0, ALTO_PANTALLA - 20, ANCHO_PANTALLA, 20)
plataformas.add(plataforma_base)

def generar_nivel():
    """
    Genera un nuevo conjunto de plataformas, enemigos y objetos.
    La dificultad aumenta con el nivel.
    """
    global nivel
    nivel += 1
    
    plataformas.empty()
    enemigos.empty()
    objetos.empty()
    plataformas.add(plataforma_base)
    
    # La altura máxima del salto del jugador es una función de la FUERZA_SALTO y la GRAVEDAD.
    # Se genera una altura de salto máxima aproximada para asegurar que las plataformas sean alcanzables.
    # Se usa 0.9 para tener un rango generoso pero desafiante.
    altura_salto_max = abs(FUERZA_SALTO) * (abs(FUERZA_SALTO) / (2 * GRAVEDAD))
    print(f"Altura de salto máxima del jugador: {altura_salto_max:.2f} px")
    
    ultima_plataforma_y = ALTO_PANTALLA - 100
    
    # Control de dificultad
    num_plataformas = 5 + nivel # Aumenta el número de plataformas
    ancho_plataforma_min = max(50, 150 - nivel * 10) # Las plataformas se hacen más cortas
    ancho_plataforma_max = max(100, 250 - nivel * 10)
    
    # Se asegura de que se generen al menos 3 plataformas para las monedas
    num_plataformas = max(num_plataformas, num_monedas_nivel)

    plataformas_para_monedas = []

    for _ in range(num_plataformas):
        plataforma_valida = False
        while not plataforma_valida:
            # Genera una posición para la nueva plataforma
            ancho_plataforma = random.randint(ancho_plataforma_min, ancho_plataforma_max)
            x = random.randint(0, ANCHO_PANTALLA - ancho_plataforma)
            
            # Ajusta el y_offset para que las plataformas siempre sean alcanzables con la fuerza de salto
            y_offset = random.randint(int(altura_salto_max * 0.3), int(altura_salto_max * 0.6))
            y = ultima_plataforma_y - y_offset
            
            if y < 50:
                y = 50
            
            nueva_plataforma = Plataforma(x, y, ancho_plataforma, 20)

            # Verifica si la nueva plataforma se superpone con las existentes
            superposicion = False
            for p in plataformas:
                # Comprueba si los rectángulos de las plataformas se solapan
                if nueva_plataforma.rect.colliderect(p.rect):
                    superposicion = True
                    break
            
            if not superposicion:
                plataforma_valida = True
        
        plataformas.add(nueva_plataforma)
        ultima_plataforma_y = y
        plataformas_para_monedas.append(nueva_plataforma)

        # Genera un enemigo de manera aleatoria en la plataforma
        if random.random() < (0.3 + nivel * 0.1): # Aumenta la probabilidad de enemigos
            if random.random() < 0.5:
                enemigos.add(Enemigo(x + 10, y - 40, 40, 40, x, x + ancho_plataforma - 40))
            else:
                enemigos.add(EnemigoSeguidor(x + 10, y - 40, 40, 40))
    
    # Genera exactamente el número de monedas requerido
    random.shuffle(plataformas_para_monedas)
    for i in range(min(num_monedas_nivel, len(plataformas_para_monedas))):
        p = plataformas_para_monedas[i]
        objetos.add(Objeto(p.rect.x + p.rect.width // 2, p.rect.y - 30, 20, 20))


def reset_game():
    """
    Función para reiniciar el juego.
    """
    global puntuacion, nivel
    puntuacion = 0
    nivel = 0
    jugador.rect.centerx = ANCHO_PANTALLA // 2
    jugador.rect.bottom = ALTO_PANTALLA - 50
    jugador.velocidad_y = 0
    jugador.velocidad_x = 0
    generar_nivel()

def draw_score(surface, score, level):
    """
    Dibuja la puntuación y el nivel en la pantalla.
    """
    score_text = font_medium.render(f"Puntuación: {score}", True, BLANCO)
    level_text = font_medium.render(f"Nivel: {level}", True, BLANCO)
    surface.blit(score_text, (10, 10))
    surface.blit(level_text, (10, 45))

def draw_menu():
    """
    Dibuja el menú de inicio.
    """
    pantalla.fill(NEGRO)
    title_text = font_large.render("Plataformas Infinitas", True, BLANCO)
    title_rect = title_text.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 4))
    pantalla.blit(title_text, title_rect)
    
    start_text = font_medium.render("Presiona ESPACIO para empezar", True, BLANCO)
    start_rect = start_text.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
    pantalla.blit(start_text, start_rect)

def draw_game_over():
    """
    Dibuja la pantalla de Game Over.
    """
    pantalla.fill(NEGRO)
    game_over_text = font_large.render("GAME OVER", True, BLANCO)
    game_over_rect = game_over_text.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 4))
    pantalla.blit(game_over_text, game_over_rect)

    final_score_text = font_medium.render(f"Puntuación Final: {puntuacion}", True, BLANCO)
    final_score_rect = final_score_text.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
    pantalla.blit(final_score_text, final_score_rect)
    
    restart_text = font_medium.render("Presiona R para reiniciar", True, BLANCO)
    restart_rect = restart_text.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 + 50))
    pantalla.blit(restart_text, restart_rect)

# Generamos el primer nivel al iniciar el juego
reset_game()

corriendo = True
reloj = pygame.time.Clock()

pygame.mixer.music.play(-1)

while corriendo:
    # 4.1. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        
        if game_state == "menu":
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                game_state = "playing"
                reset_game()
                pygame.mixer.music.play(-1)
        elif game_state == "playing":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador.move_left()
                if evento.key == pygame.K_RIGHT:
                    jugador.move_right()
                if evento.key == pygame.K_SPACE:
                    if jugador.en_suelo:
                        jugador.jump()
                        if jump_sound:
                            jump_sound.play()
                    else:
                        jugador.jump()
            
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador.velocidad_x < 0:
                    jugador.stop_x()
                if evento.key == pygame.K_RIGHT and jugador.velocidad_x > 0:
                    jugador.stop_x()
        elif game_state == "game_over":
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                game_state = "menu"
    
    # 4.2. Actualización del estado del juego
    if game_state == "playing":
        jugador.update(plataformas)
        
        for enemigo in enemigos:
            if isinstance(enemigo, EnemigoSeguidor):
                enemigo.update(jugador)
            else:
                enemigo.update()
        
        # Detección de colisiones
        objetos_recogidos = pygame.sprite.spritecollide(jugador, objetos, True)
        for obj in objetos_recogidos:
            puntuacion += PUNTOS_POR_OBJETO
        
        colisiones_enemigos = pygame.sprite.spritecollide(jugador, enemigos, False)
        if colisiones_enemigos:
            for enemigo in colisiones_enemigos:
                if jugador.velocidad_y > 0 and jugador.rect.bottom <= enemigo.rect.centery + 10:
                    if defeat_sound:
                        defeat_sound.play()
                    enemigo.kill()
                    puntuacion += PUNTOS_POR_ENEMIGO_SEGUIDOR if isinstance(enemigo, EnemigoSeguidor) else PUNTOS_POR_ENEMIGO
                    jugador.velocidad_y = -5
                else:
                    game_state = "game_over"
                    pygame.mixer.music.stop()

        # Generación de nuevo nivel si el jugador se cae de la pantalla
        if jugador.rect.top > ALTO_PANTALLA:
            game_state = "game_over"
            pygame.mixer.music.stop()

        # Generación de nuevo nivel si todas las monedas han sido recolectadas
        if len(objetos) == 0:
            generar_nivel()

    # 4.3. Dibujo de todos los elementos
    if background:
        pantalla.blit(background, (0, 0))
    else:
        pantalla.fill(AZUL)

    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        plataformas.draw(pantalla)
        enemigos.draw(pantalla)
        objetos.draw(pantalla)
        pantalla.blit(jugador.image, jugador.rect)
        draw_score(pantalla, puntuacion, nivel)
    elif game_state == "game_over":
        draw_game_over()

    # 4.4. Actualiza la pantalla.
    pygame.display.flip()

    # 4.5. Controla la velocidad de fotogramas.
    reloj.tick(FPS)

# 5. Finalización de Pygame
pygame.quit()
