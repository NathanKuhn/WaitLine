import pygame
from gameMap import MAP

TILE_IMAGE = pygame.image.load("tile.png")

class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = TILE_IMAGE
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.speed = 0.1

        self.rect.x = self.image.get_width() * x
        self.rect.y = self.image.get_height() * y

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.Surface([32, 32])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.speed = 0.1

        self.rect.x = self.image.get_width() * x
        self.rect.y = self.image.get_height() * y

class Board(pygame.sprite.Group):

    def __init__(self, tilesX, tilesY):
        super().__init__()

        self.tileList = []

        for tileX in range(tilesX):
            self.tileList.append([])
            for tileY in range(tilesY):
                if (MAP[tileY][tileX]):
                    tile = Wall(tileX, tileY)
                else:
                    tile = Tile(tileX, tileY)
                self.tileList[tileX].append(tile)
                self.add(tile)