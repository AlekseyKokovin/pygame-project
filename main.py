import pygame
import random


class blocks:

    def __init__(self, x):

        self.clock = pygame.time.Clock()
        self.color = colors[random.choice(['blue', 'green', 'red'])]
        self.block_coords = self.width, self.height = 40, 40

        self.x = 100 + x * self.width
        self.y = 10
        self.speed = self.height

    def update(self):
        if self.y + self.height < 10 + board.height * board.cell_size:
            self.y += self.speed * self.clock.tick() / 1000


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
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


size = width, height = 500, 500
board_x = 8
board_y = 12
board = Board(board_x, board_y)
screen = pygame.display.set_mode(size)
colors = {'blue': ((0, 0, 100), (0, 0, 255)),
          'green': ((0, 100, 0), (0, 255, 0)),
          'red': ((100, 0, 0), (255, 0, 0))}

all_blocks = []
first_blok = blocks(2)
all_blocks.append(first_blok)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    board.render(screen)
    for elem in all_blocks:
        elem.update()
    pygame.display.flip()
