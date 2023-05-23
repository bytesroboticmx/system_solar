import pygame
import math

# Inicializa pygame
pygame.init()

# Configuracion de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System")

# Define los codigos enteros RBG
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define los parametros y propiedades de la tierra
sun_radius = 50
sun_pos = (width // 2, height // 2)
earth_radius = 20
earth_distance = 150
earth_angle = 0
earth_speed = 0.01
#Define los parametro de la luna
moon_radius = 10
moon_distance = 40
moon_angle = 0
moon_speed = 0.05

# Ejecuta el ciclo principal del sistema
running = True
while running:
    # Evento handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualiza la posicion de la tierra
    earth_x = sun_pos[0] + earth_distance * math.cos(earth_angle)
    earth_y = sun_pos[1] + earth_distance * math.sin(earth_angle)
    earth_angle += earth_speed

    # Actualiza la posicion de la luna
    moon_x = earth_x + moon_distance * math.cos(moon_angle)
    moon_y = earth_y + moon_distance * math.sin(moon_angle)
    moon_angle += moon_speed

    # Dibuja el fondo de pantalla
    screen.fill(BLACK)

    # Dibuja el sol
    pygame.draw.circle(screen, YELLOW, sun_pos, sun_radius)

    # Dibuja la tierra
    pygame.draw.circle(screen, BLUE, (int(earth_x), int(earth_y)), earth_radius)

    # Dibuja la luna
    pygame.draw.circle(screen, RED, (int(moon_x), int(moon_y)), moon_radius)

    # Actualiza la pantalla
    pygame.display.flip()

# Termina pygame
pygame.quit()
