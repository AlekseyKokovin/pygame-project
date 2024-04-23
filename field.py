from math import ceil

from main_screensaver import start_screen

import pygame
import random


class Figure:

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
                    block = Blocks(i.index(j) + x, self.form.index(i) + y, color, self.can_move)
                    fig.append(block)
                    all_blocks.append(block)
                    self.figure_blocks.append(block)
                else:
                    fig.append(0)
            self.figure.append(fig)

    def update(self):

        for block in self.figure_blocks:
            block.update()

        stop_by_block = False
        for block in self.figure_blocks:
            if not block:
                continue
            target_y = block.coord_y() + 1
            if target_y >= board.height or \
                    (target_y >= 0 and board.board[target_y][block.coord_x()]):
                stop_by_block = True

        if stop_by_block and self.can_move:
            for i in self.figure:
                for j in i:
                    if j:
                        j.can_move = False
                        j.y = j.coord_y() * 40 + 10
                        board.board[j.coord_y()][j.coord_x()] = j
            self.can_move = False

        delete_indexes = []
        for i in range(len(board.board)):
            if all(board.board[i]):
                delete_indexes.append(i)
        for i in sorted(delete_indexes, reverse=True):
            for j in range(len(board.board[i]) - 1, -1, -1):
                board.board[i][j].need_delete = True
                board.board[i][j] = 0

    def can_rotate_figure(self):
        for y, row in enumerate(self.figure):
            for x, block in enumerate(row):
                if block:
                    new_x, new_y = 140, 50
                    if x == 0 and y == 0:
                        new_x = block.x + board.cell_size * 2
                    elif x == 1 and y == 0:
                        new_x = block.x + board.cell_size
                        new_y = block.y + board.cell_size
                    elif x == 2 and y == 0:
                        new_y = block.y + board.cell_size * 2
                    elif x == 2 and y == 1:
                        new_x = block.x - board.cell_size
                        new_y = block.y + board.cell_size
                    elif x == 2 and y == 2:
                        new_x = block.x - board.cell_size * 2
                    elif x == 1 and y == 2:
                        new_x = block.x - board.cell_size
                        new_y = block.y - board.cell_size
                    elif x == 0 and y == 2:
                        new_y = block.y - board.cell_size * 2
                    elif x == 0 and y == 1:
                        new_x = block.x + board.cell_size
                        new_y = block.y - board.cell_size
                    y_pos = (new_y - board.top) / 40
                    if int(y_pos) != y_pos:
                        y_pos = int(y_pos) + 1
                    y_pos = int(y_pos)
                    new_x, new_y = int((new_x - board.left) // 40), int((new_y - board.top) // 40)
                    if new_x < 0 or new_x >= board_x or y_pos >= board_x or (new_y >= 0 and board.board[new_y][new_x] != 0):
                        return False
        return True

    def rotate_right(self):
        if self.can_rotate and self.can_rotate_figure():
            for y, row in enumerate(self.figure):
                for x, block in enumerate(row):
                    if block:
                        if x == 0 and y == 0:
                            block.x += board.cell_size * 2
                        elif x == 1 and y == 0:
                            block.x += board.cell_size
                            block.y += board.cell_size
                        elif x == 2 and y == 0:
                            block.y += board.cell_size * 2
                        elif x == 2 and y == 1:
                            block.x -= board.cell_size
                            block.y += board.cell_size
                        elif x == 2 and y == 2:
                            block.x -= board.cell_size * 2
                        elif x == 1 and y == 2:
                            block.x -= board.cell_size
                            block.y -= board.cell_size
                        elif x == 0 and y == 2:
                            block.y -= board.cell_size * 2
                        elif x == 0 and y == 1:
                            block.x += board.cell_size
                            block.y -= board.cell_size
            self.figure = list(zip(*self.figure[::-1]))

    def left(self):
        can_do = True
        for i in self.figure:
            for j in i:
                if j != 0:
                    try:
                        if j.coord_x() - 1 < 0:
                            raise IndexError
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
                        if j.coord_x() + 1 >= board_x:
                            raise IndexError
                        if board.board[j.coord_y()][j.coord_x() + 1] != 0:
                            can_do = False
                    except IndexError:
                        can_do = False
        if can_do:
            for i in self.figure:
                for j in i:
                    if j != 0:
                        j.change_block_pos(1, 0)


class Blocks:

    def __init__(self, x, y, color, can_move):
        self.clock = pygame.time.Clock()
        self.color = colors[color]
        self.block_coords = self.width, self.height = 40, 40

        self.x = board.left + min(max(x, 0), board.width - 1) * self.width
        self.y = board.top - self.height * 4 + min(max(y, 0), board.height - 1) * self.height

        self.speed = self.height
        self.can_move = can_move
        self.need_delete = False
        self.block_deleted = False

    def update(self):
        if self.can_move:
            self.y += self.speed * self.clock.tick() / 1000

    def change_block_pos(self, x, y):
        self.y += y * self.height
        self.x += x * self.width

    def coord_x(self):
        return int((self.x - board.left) // self.width)

    def coord_y(self):
        return int((self.y - board.top) // self.height)


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


def update_all_blocks():
    delete_indexes = []
    for i in range(len(all_blocks)):
        if all_blocks[i].need_delete:
            delete_indexes.append(i)
    for index in sorted(delete_indexes, reverse=True):
        del all_blocks[index]


def form_choice(x):
    for_choice = []
    if x <= board_x - 3:
        for_choice.append('i')
        for_choice.append('t')
        for_choice.append('o')
        for_choice.append('l')
        for_choice.append('z')
    return for_choice


colors = {'blue': ((0, 0, 100), (0, 0, 255)),
          'green': ((0, 100, 0), (0, 255, 0)),
          'red': ((100, 0, 0), (255, 0, 0)),
          'yellow': ((100, 100, 0), (255, 255, 0)),
          'light_blue': ((0, 100, 100), (0, 255, 255)),
          'purple': ((100, 0, 100), (255, 0, 255))}

figures_type = {
    't': [(0, 0, 0), (16, 17, 18), (0, 19, 0)],
    'i': [(0, 13, 0), (0, 14, 0), (0, 15, 0)],
    'z': [(0, 0, 9), (0, 10, 11), (0, 12, 0)],
    'l': [(0, 5, 0), (0, 6, 0), (0, 7, 8)],
    'o': [(0, 1, 2), (0, 3, 4), (0, 0, 0)]
}


def check_game_end():
    for block in board.board[0]:
        if block:
            return True
    return False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 650, 650
    music = screen = pygame.display.set_mode(size)

    running = True
    while running:
        a = start_screen(screen, width, height)
        if not a:
            break

        x_and_y, play_songs, volume = a
        if play_songs:
            current_song_index = 0
            pygame.mixer.music.load(f"Music/music{play_songs[current_song_index]}.mp3")
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)

        board_x, board_y = x_and_y
        board = Board(board_x, board_y)
        clock = pygame.time.Clock()
        figures = []
        all_blocks = []

        x = random.choice(range(0, board_x - 2))
        for_choice = form_choice(x)
        a = Figure(random.choice(list(colors.keys())), x, 0, random.choice(for_choice))
        figures.append(a)

        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True
                    pygame.mixer.music.stop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        game_over = True
                    if event.key == pygame.K_UP:
                        a.rotate_right()
                    if event.key == pygame.K_RIGHT:
                        a.right()
                    if event.key == pygame.K_LEFT:
                        a.left()
                    if event.key == pygame.K_UP:
                        a.update()

            color_start = pygame.Color('Black')
            color_end = (139, 0, 139)
            for y in range(height):
                r = int((color_end[0] - color_start[0]) * (y / height) + color_start[0])
                g = int((color_end[1] - color_start[1]) * (y / height) + color_start[1])
                b = int((color_end[2] - color_start[2]) * (y / height) + color_start[2])
                pygame.draw.rect(screen, (r, g, b), pygame.Rect(0, y, width, 1))

            board.render(screen)

            if not a.can_move:
                x = random.choice(range(0, board_x - 2))
                for_choice = form_choice(x)
                a = Figure(random.choice(list(colors.keys())), x, 0, random.choice(for_choice))
                figures.append(a)

                if check_game_end():
                    game_over = True
                    pygame.mixer.music.stop()
                    break

            for elem in figures:
                elem.update()

            if not pygame.mixer.music.get_busy() and play_songs:
                current_song_index = (current_song_index + 1) % len(play_songs)
                pygame.mixer.music.load(f"Music/music{play_songs[current_song_index]}.mp3")
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play(-1)

            update_all_blocks()
            pygame.display.flip()

        if not running:
            break

pygame.quit()
