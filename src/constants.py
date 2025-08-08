# constants.py

# Configuración de la pantalla
ANCHO_PANTALLA = 800 # Ancho de la ventana del juego en píxeles.
ALTO_PANTALLA = 600  # Alto de la ventana del juego en píxeles.
FPS = 60             # Cuadros por segundo (Frames Per Second) para la fluidez del juego.

# Colores (formato RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
#
ANIMATION_SPEED = 4

# Constantes del jugador y física
GRAVEDAD = 0.5        # Fuerza de la gravedad que tira al jugador hacia abajo.
VELOCIDAD_JUGADOR = 5 # Velocidad horizontal del jugador.
FUERZA_SALTO = -14   # Fuerza del salto (negativo porque Y aumenta hacia abajo).

# Constantes para los enemigos
VELOCIDAD_ENEMIGO = 3 # Velocidad horizontal del enemigo que se mueve de un lado a otro.
VELOCIDAD_ENEMIGO_SEGUIDOR = 2 # Velocidad del nuevo enemigo que persigue al jugador.
RANGO_DETECCION = 90 # Distancia a la que el enemigo seguidor empieza a perseguir al jugador.

# Constantes para objetos y puntuación
PUNTOS_POR_OBJETO = 100 # Puntos que se otorgan al recoger un objeto.
PUNTOS_POR_ENEMIGO = 200 # Puntos que se otorgan al derrotar un enemigo.
PUNTOS_POR_ENEMIGO_SEGUIDOR = 300 # Puntos por derrotar al enemigo que persigue.

# Nombres de archivos de assets (¡usa los tuyos!)
# Sprites del jugador para animaciones
PLAYER_IDLE_SPRITE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Characters/Default/character_green_front.png"
PLAYER_RUN_SPRITES = ["/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Characters/Default/character_green_walk_a.png","/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Characters/Default/character_green_walk_b.png"] # Lista de frames para correr
PLAYER_JUMP_SPRITE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Characters/Default/character_green_jump.png"

# Sprites del enemigo normal
ENEMY_RUN_SPRITES = ["/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Enemies/Default/saw_a.png", "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Enemies/Default/saw_b.png"] # Lista de frames para correr del enemigo normal

BACKGROUND_IMAGE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Backgrounds/Default/background_color_hills.png" # ¡Nueva constante para el fondo!

# Coloca estos archivos en la misma carpeta que el código.
PLAYER_SPRITE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Characters/Default/character_green_idle.png"
ENEMY_SPRITE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Enemies/Default/saw_b.png"
CHASING_ENEMY_SPRITE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Enemies/Default/bee_b.png"
COLLECTIBLE_SPRITE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Tiles/Default/coin_gold.png"
PLATFORM_SPRITE = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sprites/Tiles/Default/block_green.png"
BG_MUSIC = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sounds/sfx_bump.ogg"
JUMP_SOUND = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/jump.mp3"
ENEMY_DEFEAT_SOUND = "/home/usuario/Documentos/curso_programacion/Rectangulo_Saltante/assets/kenney_new-platformer-pack-1.0/Sounds/sfx_disappear.ogg"

# Constantes de audio
MUSICA_VOLUMEN = 0.5
EFECTO_VOLUMEN = 0.8
