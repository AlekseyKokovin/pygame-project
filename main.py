import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class blocks(pygame.sprite.Sprite):
    image = load_image("green_block")
    # изображение нужно сделать 50 на 50 пикселей

    def __init__(self, x):
        super().__init__(figure_sprites)
        self.rect = self.image.get_rect()
        self.clock = pygame.time.Clock()

        # x - номер места появления, не координата
        self.rect.x = 100 + x * self.rect.width
        self.rect.y = 0
        self.speed = self.rect.height

    def update(self):
        self.rect.y += self.speed * self.clock.tick() / 1000


if __name__ == '__main__':
    pygame.init()
    # tetris_class = Tetris(x, y) Tetris - класс поля , x и y - ширина и высота
    FPS = 60
    size = WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode(size)
    figure_sprites = pygame.sprite.Group()
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
        if active_game:
            pass
            # проверить можно ли опустить на 1 клетку вниз
            # tetris_class.active_figure.pos = tetris_class.active_figure.pos[0], tetris_class.active_figure.pos[1] + y y - длина клетки
        clock.tick(FPS)
    pygame.quit()
