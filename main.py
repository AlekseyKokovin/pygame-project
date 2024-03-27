import pygame
import random


class figure:

    def __init__(self, color, x, y, type):
        self.figure_blocks = []
        self.color = color
        self.form = figures_type[type]
        self.figure = []
        self.can_move = True
        self.can_rotate = type != 'o'
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

        self.stop_row = [0, 0, 0]

    def update(self):

        self.stop_row = [0, 0, 0]
        for i in range(len(self.figure)):
            for j in range(len(self.figure[i])):
                if self.figure[i][j] != 0:
                    self.stop_row[i] = self.figure[i][j]

        for block in self.figure_blocks:
            block.update()

        stop_by_block = False
        for i in self.stop_row:
            if i != 0:
                try:
                    if board.board[i.coord_y() + 1][i.coord_x()]:
                        stop_by_block = True
                except IndexError:
                    stop_by_block = True

        if stop_by_block and self.can_move:
            for i in self.figure:
                for j in i:
                    if j != 0:
                        j.can_move = False
                        board.board[j.coord_y()][j.coord_x()] = j
            self.can_move = False

        for i in range(len(board.board)):
            if all(board.board[i]):
                for j in range(len(board.board[i])):
                    del board.board[i][j]
                    board.board[i][j] = 0
                    for elem in figures:
                        elem.update()

    def rotate_left(self):
        for i in range(3):
            self.rotate_right()

    def rotate_right(self):
        if self.can_rotate:
            self.figure = list(zip(*self.figure[::-1]))

    def left(self):
        can_do = True
        for i in self.figure:
            for j in i:
                if j != 0:
                    try:
                        if board.board[j.coord_y()][j.coord_x() - 1] != 0:
                            can_do = False
                    except IndexError:
                        can_do = False

        if can_do:
            for i in self.figure:
                for j in i:
                    if j != 0:
                        j.change_block_pos(-1, 0)

    def right(self):
        can_do = True
        for i in self.figure:
            for j in i:
                if j != 0:
                    try:
                        if board.board[j.coord_y()][j.coord_x() - 1] != 0:
                            can_do = False
                    except IndexError:
                        can_do = False
        if can_do:
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
        self.block_deleted = False

    def update(self):
        if self.can_move:
            self.y += self.speed * self.clock.tick() / 1000

    def change_block_pos(self, x, y):
        self.y += y * self.height
        self.x += x * self.width

    def coord_x(self):
        return int((self.x - 100) // self.width)

    def coord_y(self):
        return int((self.y - 10) // self.height)


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
          'red': ((100, 0, 0), (255, 0, 0)),
          'yellow': ((100, 100, 0), (255, 255, 0)),
          'light_blue': ((0, 100, 100), (0, 255, 255)),
          'purple': ((100, 0, 100), (255, 0, 255))}

figures_type = {
    't': [(0, 0, 0), (1, 2, 3), (0, 1, 0)],
    'i': [(0, 1, 0), (0, 1, 0), (0, 1, 0)],
    'z': [(0, 0, 1), (0, 1, 2), (0, 1, 0)],
    'l': [(0, 1, 0), (0, 1, 0), (0, 1, 2)],
    'o': [(0, 1, 2), (0, 1, 2), (0, 0, 0)]
}

figures = []
all_blocks = []

a = figure(random.choice(list(colors.keys())), -1, 0, 'o')
figures.append(a)
a = figure(random.choice(list(colors.keys())), 1, -1, 'o')
figures.append(a)
a = figure(random.choice(list(colors.keys())), 3, -2, 'o')
figures.append(a)
a = figure(random.choice(list(colors.keys())), 5, -3, 'o')
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
