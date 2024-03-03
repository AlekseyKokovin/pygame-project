import os
import sys
import pygame
# (?) - не знаю как точно сделать, просто идея

if __name__ == '__main__':
    pygame.init()
    # tetris_class = Tetris(x, y) Tetris - класс поля , x и y - ширина и высота
    FPS = 60
    size = WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    active_game = False
    # ^ если идет игра, то меняем на True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass # вовращаемся на заставку
                if event.key == pygame.K_UP and active_game:
                    pass
                    # tetris_class.rotate(tetris_class.active_figure) rotate - функция поворота фигуры, active_figure - фигура, которая спускается
                if event.key == pygame.K_DOWN and active_game:
                    pass
                    # tetris_class.active_figure.pos = tetris_class.active_figure.pos[0], tetris_class.active_figure.pos[1] + y y - длина клетки
                if event.key == pygame.K_RIGHT and active_game:
                    pass
                    # if фигура не должна быть в самом краю справа
                        # tetris_class.active_figure.pos = tetris_class.active_figure.pos[0] + x, tetris_class.active_figure.pos[1] x - ширина клетки
                if event.key == pygame.K_LEFT and active_game:
                    pass
                    # if фигура не должна быть в самом краю слева
                        # tetris_class.active_figure.pos = tetris_class.active_figure.pos[0] - x, tetris_class.active_figure.pos[1] x - ширина клетки
                if event.key == pygame.K_p:
                    active_game = False if active_game else True
                    # pause/resume

        clock.tick(FPS)
    pygame.quit()