import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 500
ALTO = 500
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

# Colores
rojo = (255, 0, 0)
blanco = (255, 255, 255)

# Dibujar figuras
def dibujar_figuras(VENTANA):
    VENTANA.fill(blanco)  # Fondo blanco

    # cuadrado (superior izquierdo)
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(25, 50, 75, 75))

    # rectángulo (superior centro)
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(150, 50, 150, 75))

    # trapecio (superior derecho)
    pygame.draw.polygon(VENTANA, rojo, [(350, 50), (450, 50), (475, 125), (325, 125)])

    # triángulo (centro izquierda)
    pygame.draw.polygon(VENTANA, rojo, [(25, 300), (175, 300), (100, 175)])


    # figura irregular (centro medio)
    pygame.draw.polygon(VENTANA, rojo, [(275, 150), (325, 200), (325, 225), (350, 225), (325,250),
                                        (350,300), (200,300), (225, 250), (200, 225), (225,225), (225,200)])


    # triángulo (centro derecha)
    pygame.draw.polygon(VENTANA, rojo, [(375, 300), (450, 300), (412.5, 175)])

    # semicírculo sobre un rectángulo (inferior izquierda)
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(25, 450, 150, 25))
    pygame.draw.circle(VENTANA, rojo, (100, 402), 50, 0)


    # creeper face (inferior derecha)
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(300, 325, 50, 50))
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(400, 325, 50, 50))
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(350, 375, 50, 75))
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(325, 400, 25, 75))
    pygame.draw.rect(VENTANA, rojo, pygame.Rect(400, 400, 25, 75))

    pygame.display.update()

# Bucle principal
ejecutar = True
while ejecutar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

    dibujar_figuras(VENTANA)

pygame.quit()
