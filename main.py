import pygame
import random


class figure:

    def __init__(self, color, x, y, type):
        self.figure_blocks = []
        self.color = color
        self.form = figures_type[type]
        self.figure = []
        self.can_move = True
        self.can_rotate = True
        for i in self.form:
            fig = []
            for j in i:
                if j != 0:
                    block = blocks(i.index(j) + x, self.form.index(i) + y, color, self.can_move)
                    fig.append(block)
                    all_blocks.append(block)
                    self.figure_blocks.append(block)
                else:
                    fig.append(0)
            self.figure.append(fig)
        self.the_lowerest = self.figure_blocks[-1]

    def update(self):
        for block in self.figure_blocks:
            block.update()
        if self.the_lowerest.y + board.cell_size >= (board.height * board.cell_size) + 10:
            for i in self.figure:
                for j in i:
                    if j != 0:
                        j.can_move = False
            self.can_move = False

    def rotate_left(self):
        for i in range(3):
            self.rotate_right()

    def rotate_right(self):
        if self.can_rotate:
            self.figure = list(zip(*self.figure[::-1]))

    def left(self):
        for i in self.figure:
            for j in i:
                if j != 0:
                    j.change_block_pos(-1, 0)

    def right(self):
        for i in self.figure:
            for j in i:
                if j != 0:
                    j.change_block_pos(1, 0)


class blocks:

    def __init__(self, x, y, color, can_move):

        self.clock = pygame.time.Clock()
        self.color = colors[color]
        self.block_coords = self.width, self.height = 40, 40

        self.x = 100 + x * self.width
        self.y = 10 - self.height * 4 + self.height * y
        self.speed = self.height
        self.can_move = can_move

    def update(self):
        if self.can_move:
            self.y += self.speed * self.clock.tick() / 1000

    def change_block_pos(self, x, y):
        self.y += y * self.height
        self.x += x * self.width


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.left = 100
        self.top = 10
        self.cell_size = 40

    def render(self, scr):
        pygame.draw.line(scr, 'white', (self.left, self.top),
                                       (self.left, self.top + self.cell_size * self.height))
        pygame.draw.line(scr, 'white', (self.left, self.top),
                                       (self.left + self.cell_size * self.width, self.top))

        pygame.draw.line(scr, 'white', (self.left + self.width * self.cell_size, self.top),
                                       (self.left + self.width * self.cell_size, self.top + self.cell_size * self.height))
        pygame.draw.line(scr, 'white', (self.left, self.top + self.height * self.cell_size),
                                       (self.left + self.width * self.cell_size, self.top + self.cell_size * self.height))

        for elem in all_blocks:
            pygame.draw.rect(scr, elem.color[0], ((elem.x, elem.y), (elem.width, elem.height)))
            pygame.draw.rect(scr, elem.color[1], ((elem.x + 8, elem.y + 8), (elem.width - 16, elem.height - 16)))

            pygame.draw.rect(scr, 'white', ((elem.x, elem.y), (elem.width, elem.height)), 1)
            pygame.draw.rect(scr, 'white', ((elem.x + 8, elem.y + 8), (elem.width - 16, elem.height - 16)), 1)

            pygame.draw.line(scr, 'white', (elem.x, elem.y), (elem.x + 8, elem.y + 8))
            pygame.draw.line(scr, 'white', (elem.x + 40, elem.y), (elem.x + 32, elem.y + 8))
            pygame.draw.line(scr, 'white', (elem.x, elem.y + 40), (elem.x + 8, elem.y + 32))
            pygame.draw.line(scr, 'white', (elem.x + 40, elem.y + 40), (elem.x + 32, elem.y + 32))

        pygame.draw.rect(scr, 'black', ((100, 0), (40 * self.width, 10)))


size = width, height = 500, 500
board_x = 8
board_y = 12
board = Board(board_x, board_y)
screen = pygame.display.set_mode(size)

colors = {'blue': ((0, 0, 100), (0, 0, 255)),
          'green': ((0, 100, 0), (0, 255, 0)),
          'red': ((100, 0, 0), (255, 0, 0))}

figures_type = {
    't': [(0, 0, 0), (1, 2, 3), (0, 1, 0)],
    'i': [(0, 1, 0), (0, 1, 0), (0, 1, 0)],
    'z': [(0, 0, 1), (0, 1, 2), (0, 1, 0)],
    'l': [(0, 1, 0), (0, 1, 0), (0, 1, 2)],
    'o': [(0, 1, 2), (0, 1, 2), (0, 0, 0)]
}

figures = []
all_blocks = []

a = figure(random.choice(['blue', 'green', 'red']), 0, 0, 'z')
figures.append(a)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    board.render(screen)
    for elem in figures:
        elem.update()
    pygame.display.flip()
