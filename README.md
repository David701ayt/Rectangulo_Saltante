# Rectangulo_Saltante
REPOSITORIO DE JUEGO Rectangulo_Saltante
🎮 Características del Juego
Generación de Niveles Procedimental: Cada nivel se genera de manera única y aleatoria, asegurando que cada partida sea diferente.

Dificultad Progresiva: La dificultad aumenta gradualmente con cada nivel. Las plataformas se vuelven más pequeñas y los enemigos más numerosos, lo que requiere mayor habilidad y precisión.

Objetivo de Nivel: Para avanzar al siguiente nivel, debes recolectar las 3 monedas que se generan en el escenario.

Jugabilidad Infinita: Sin un final predefinido, puedes jugar y ver hasta qué nivel puedes llegar.

🕹️ Controles
Flecha Izquierda: Moverse a la izquierda.

Flecha Derecha: Moverse a la derecha.

Barra Espaciadora: Saltar.

R: Reiniciar el juego después de un Game Over.

🛠️ Requisitos del Sistema
Para ejecutar este juego, necesitas tener instalado Python y la biblioteca Pygame.

🚀 Cómo Ejecutar el Juego
Instala Pygame: Si aún no tienes Pygame, puedes instalarlo fácilmente a través de pip:

pip install pygame

Ejecuta el Juego: Navega hasta la carpeta del proyecto y ejecuta el archivo principal main.py desde tu terminal:

python main.py

📂 Estructura del Proyecto
main.py: Contiene la lógica principal del juego, el bucle de juego, la detección de colisiones y la generación de niveles.

player.py: Define la clase Jugador y su comportamiento.

platform.py: Define la clase Plataforma.

enemy.py: Define la clase Enemigo.

chasing_enemy.py: Define la clase EnemigoSeguidor.

collectible.py: Define la clase Objeto (moneda).

constants.py: Almacena todas las constantes del juego, como colores, velocidades, fuerza de salto y rutas de archivos de assets.

assets/: Carpeta que contiene las imágenes y archivos de sonido del juego.

🙏 Créditos
Este proyecto fue desarrollado utilizando la maravillosa biblioteca Pygame. ¡Un gran agradecimiento a la comunidad de Pygame por su continuo apoyo!
