import pygame


class blocks:

    def __init__(self, x):
        self.clock = pygame.time.Clock()
        self.block_coords = self.width, self.height = 50, 50

        self.x = 100 + x * self.width
        self.y = 0
        self.speed = self.height

    def update(self):
        self.y += self.speed * self.clock.tick() / 1000
