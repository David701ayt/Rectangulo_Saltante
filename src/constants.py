# constants.py

# Configuración de la pantalla
ANCHO_PANTALLA = 800 # Ancho de la ventana del juego en píxeles.
ALTO_PANTALLA = 600  # Alto de la ventana del juego en píxeles.
FPS = 60             # Cuadros por segundo (Frames Per Second) para la fluidez del juego.

# Colores (formato RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_OSCURO = (0, 0, 150)
AMARILLO = (255, 255, 0)
# Nuevo color para el enemigo seguidor.
MORADO = (128, 0, 128)

# Constantes del jugador y física
GRAVEDAD = 0.5        # Fuerza de la gravedad que tira al jugador hacia abajo.
VELOCIDAD_JUGADOR = 5 # Velocidad horizontal del jugador.
FUERZA_SALTO = -10    # Fuerza del salto (negativo porque Y aumenta hacia abajo).

# Constantes para los enemigos
VELOCIDAD_ENEMIGO = 3 # Velocidad horizontal del enemigo que se mueve de un lado a otro.
VELOCIDAD_ENEMIGO_SEGUIDOR = 2 # Velocidad del nuevo enemigo que persigue al jugador.
RANGO_DETECCION = 150 # Distancia a la que el enemigo seguidor empieza a perseguir al jugador.

# Constantes para objetos y puntuación
PUNTOS_POR_OBJETO = 100 # Puntos que se otorgan al recoger un objeto.
PUNTOS_POR_ENEMIGO = 200 # Puntos que se otorgan al derrotar un enemigo.
PUNTOS_POR_ENEMIGO_SEGUIDOR = 400 # Puntos por derrotar al enemigo que persigue.
