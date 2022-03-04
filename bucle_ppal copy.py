import pygame as pg

pg.init()

pantalla = pg.display.set_mode((400, 500))

game_over = False

x = 0

def parabola(x):
    return x*x
velocidad_x = 1
    
while not game_over:
    # Primero: procesar eventos
    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True

    # Modificar los objetos del juego
    x += velocidad_x
    y = 0.001 * x * x

    if x >= 600 - 10:
        velocidad_x = velocidad_x * -1
    
    # Aquí no hay nada que hacer

    # Refrescar la pantalla
    pantalla.fill((255, 0, 0))
    pg.draw.circle(pantalla, (255, 255, 0), (x, y), 10)
    print(x, y)

    pg.display.flip()

pg.quit()