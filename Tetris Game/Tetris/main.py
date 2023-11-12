import pygame
from copy import deepcopy
from pygame.locals import *
from random import choice, randrange
from pygame import mixer
from moviepy.editor import VideoFileClip
from pygame.transform import rotate
import pygame_gui
import os

# Define las dimensiones del juego y el tamaño de las celdas (TILE)
W, H = 10, 20
TILE = 36  
GAME_RES = W * TILE, H * TILE
RES = 1280, 720  
FPS = 60

# Inicializa Pygame y otras bibliotecas
pygame.init()
mixer.init()
sc = pygame.display.set_mode(RES)
game_sc = pygame.Surface(GAME_RES)
clock = pygame.time.Clock()

# Calcula el desplazamiento necesario para centrar el juego
game_offset_x = (RES[0] - GAME_RES[0]) // 2
game_offset_y = (RES[1] - GAME_RES[1]) // 2

# Crea la cuadrícula centrada
grid = [pygame.Rect(x * TILE + game_offset_x, y * TILE + game_offset_y, TILE, TILE) for x in range(W) for y in range(H)]

# Define las posiciones iniciales de las figuras
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

# Crea listas de rectángulos para las figuras y el rectángulo de la figura
figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
field = [[0 for i in range(W)] for j in range(H)]

# Define variables relacionadas con la animación y las imágenes de fondo
anim_count, anim_speed, anim_limit = 0, 45, 1000
bg = pygame.image.load('img/bg.jpg').convert()
game_bg = pygame.image.load('img/bg2.jpg').convert()

# Crea fuentes para el texto
main_font = pygame.font.Font('font/font.ttf', 80)
font = pygame.font.Font('font/font.ttf', 40)
nextFont = pygame.font.Font('font/font.ttf', 25)

# Define títulos y colores
title_next = nextFont.render('NEXT', True, pygame.Color('white'))
title_tetris = main_font.render('TETRIS', True, pygame.Color('purple'))
title_score = font.render('Score:', True, pygame.Color('white'))
title_record = font.render('PR:', True, pygame.Color('white'))

get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))
figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()
score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

# Función que verifica si la posición de una figura es válida en el campo de juego
def is_valid_position(figure, field):
    for rect in figure:
        x, y = rect.topleft
        if x < 0 or x >= W or y >= H or field[y][x]:
            return False
    return True

# Función que verifica si la figura está dentro de los límites del campo de juego
def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

# Función que obtiene el récord guardado en un archivo
def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')
            
# Función que muestra la pantalla de "Cómo jugar"
def how_to_play_screen():
    how_to_play_image = pygame.image.load('img/how_to_play_image.jpg')
    how_to_play_rect = how_to_play_image.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return
                elif event.key == K_ESCAPE:  # Agrega la detección de la tecla "Esc" para volver a la pantalla de inicio
                    return

        sc.fill((0, 0, 0))  # Limpia la pantalla

        how_to_play_rect.center = (RES[0] // 2, RES[1] // 2)
        sc.blit(how_to_play_image, how_to_play_rect)

        pygame.display.flip()

def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))

# Función que muestra la pantalla de inicio del juego 
def start_screen():
    mixer.music.load('music/menu.mp3')
    mixer.music.play(-1)

    # Cargar el video de fondo
    video_clip = VideoFileClip('img/startscreen.mp4')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    mixer.music.stop()  # Detiene la música cuando el juego comienza
                    video_clip.close()
                    return
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_h:  # Agrega la detección de la tecla "H" para ver las instrucciones
                    how_to_play_screen()

        frame = video_clip.get_frame(clock.get_time() / 1000)  # Obtener el cuadro actual del video
        frame = pygame.surfarray.make_surface(frame)  # Convierte el cuadro a una superficie de Pygame

        frame = rotate(frame, 270)

        # Agregar texto "TETRIS" en el cuadro
        title_surface = main_font.render('TETRIS', True, pygame.Color('purple'))
        title_rect = title_surface.get_rect()
        title_rect.center = (RES[0] // 2, 100)  # Posición del título en la parte superior

        # Agregar texto "Presiona Enter para comenzar"
        text_surface = font.render('Presiona Enter para comenzar', True, pygame.Color('white'))
        text_rect = text_surface.get_rect()
        text_rect.center = (RES[0] // 2, RES[1] - 50)  # Posición del texto en la parte inferior

        # Agregar texto "PR: Record"
        record = get_record()
        record_surface = font.render(f'PR: {record}', True, pygame.Color('gold'))
        record_rect = record_surface.get_rect()
        record_rect.center = (RES[0] // 2, RES[1] - 100)  # Posición del récord debajo del texto "Presiona Enter para comenzar"

        # Agregar texto "Press Q to Quit" en la esquina superior derecha
        quit_text = font.render('Press Q to Quit', True, pygame.Color('white'))
        quit_rect = quit_text.get_rect()
        quit_rect.topright = (RES[0] - 10, 10)

        # Agregar texto "How to Play (H)" en la esquina inferior derecha
        how_to_play_text = font.render('How to Play (H)', True, pygame.Color('white'))
        how_to_play_rect = how_to_play_text.get_rect()
        how_to_play_rect.bottomright = (1280,120)

        # Dibuja el cuadro de video y los textos
        sc.blit(frame, (0, 0))
        sc.blit(title_surface, title_rect)
        sc.blit(text_surface, text_rect)
        sc.blit(record_surface, record_rect)
        sc.blit(quit_text, quit_rect)
        sc.blit(how_to_play_text, how_to_play_rect)  # Agrega el texto "How to Play (H)"

        pygame.display.flip()


        
game_over = False
start_screen()
mixer.music.load('music/game.mp3')
mixer.music.play(-1)

while True:
    record = get_record()  # Obtiene el récord actual del juego
    dx, dy, rotation = 0, 0, False  # Inicializa las variables de movimiento y rotación
    space_pressed = False  # Variable para rastrear si se ha presionado la barra espaciadora

    sc.blit(bg, (0, 0))  # Dibuja el fondo en la pantalla principal
    sc.blit(game_sc, (0, 0))  # Dibuja la superficie del juego en la pantalla principal
    game_sc.blit(game_bg, (0, 0))  # Dibuja el fondo del juego en la superficie del juego

    # Retraso para las líneas completas (para dar un efecto visual de pausa)
    for i in range(lines):
        pygame.time.wait(200)

    # Captura y procesamiento de eventos de teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # Si el evento de cierre de ventana se produce, termina el juego
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1  # Mueve la figura hacia la izquierda
            elif event.key == pygame.K_RIGHT:
                dx = 1  # Mueve la figura hacia la derecha
            elif event.key == pygame.K_DOWN:
                anim_limit = 50  # Ajusta este valor para controlar la velocidad de caída
            elif event.key == pygame.K_UP:
                rotation = True  # Activa la rotación de la figura
            elif event.key == pygame.K_z:  # Agrega esta condición para detectar la tecla "C"
                # Rota la figura hacia la izquierda
                figure_old = deepcopy(figure)  # Copia la figura actual
                for i in range(4):
                    x = figure[i].y - center.y
                    y = figure[i].x - center.x
                    figure[i].x = center.x + x  # Cambia la dirección de la rotación
                    figure[i].y = center.y - y
                if not check_borders():
                    figure = deepcopy(figure_old)  # Restaura la figura si se encuentra con un obstáculo
            elif event.key == pygame.K_SPACE:
                space_pressed = True  # Activa la caída rápida de la figura

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                anim_limit = 2000  # Restaura el límite de velocidad de caída

    # Movimiento horizontal (izquierda o derecha)
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)  # Restaura la figura si se encuentra con un obstáculo

    # Movimiento vertical (caída automática)
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    y, x = figure_old[i].y, figure_old[i].x
                    if 0 <= y < H and 0 <= x < W:  # Comprobación de límites
                        field[y][x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                anim_limit = 2000  # Restaura el límite de velocidad de caída
                break

    # Control de caída rápida
    if space_pressed:
        while True:
            figure_old = deepcopy(figure)
            for i in range(4):
                figure[i].y += 1
            if not is_valid_position(figure, field):  # Verifica si la nueva posición es válida
                for i in range(4):
                    y, x = figure_old[i].y, figure_old[i].x
                    if 0 <= y < H and 0 <= x < W:  # Comprobación de límites
                        field[y][x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                anim_limit = 2000  # Restaura el límite de velocidad de caída
                break
        space_pressed = False  # Restaura la variable de caída rápida

    # Rotación de la figura
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotation:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)  # Restaura la figura si la rotación es inválida

    # Comprobación de líneas completas y actualización de la puntuación
    line, lines = H - 1, 0
    for row in range(H - 1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1
        else:
            anim_speed += 3
            lines += 1

    # Cálculo de la puntuación
    score += scores[lines]

    # Dibujo de la cuadrícula
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

    # Dibujo de la figura actual
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, color, figure_rect)

    # Dibujo del campo de juego
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * TILE, y * TILE
                pygame.draw.rect(game_sc, col, figure_rect)

    # Dibujo de la próxima figura
    for i in range(4):
        figure_rect.x = next_figure[i].x * TILE + 275
        figure_rect.y = next_figure[i].y * TILE + 100
        pygame.draw.rect(sc, next_color, figure_rect)
    # Dibujo de títulos
    sc.blit(title_tetris, (635, 220))
    sc.blit(title_score, (930, 10))
    sc.blit(title_next, (420, 40))
    sc.blit(font.render(str(score), True, pygame.Color('white')), (1100, 10))
    sc.blit(title_record, (930, 100))
    sc.blit(font.render(record, True, pygame.Color('gold')), (1100, 100))
   
    # Comprueba si el juego ha terminado
    for i in range(W):
        if field[0][i]:
            set_record(record, score)  # Establece el nuevo récord si es necesario
            game_over = True  # Establece la variable de "Game Over"
            break

    pygame.display.flip()  # Actualiza la pantalla
    clock.tick(FPS)  # Controla la velocidad del bucle principal

    # Comprueba si el juego ha terminado (fuera del bucle principal)
    if game_over:
        game_over = False  # Restablece la variable de "Game Over"
        field = [[0 for i in range(W)] for i in range(H)]  # Reinicia el campo de juego
        anim_count, anim_speed, anim_limit = 0, 60, 2000  # Restablece las animaciones y la velocidad
        score = 0  # Restablece la puntuación
        start_screen()  # Vuelve a la pantalla de inicio después de perder
        mixer.music.load('music/game.mp3')  # Carga la música del juego
        mixer.music.play(-1)  # Reproduce la música en bucle