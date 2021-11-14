import pygame
from gameMap import MAP

TILE_IMAGE = pygame.image.load("textures/tile.png")
WALL_IMAGE = pygame.image.load("textures/wall.png")
WINDOW_IMAGE = pygame.image.load("textures/window.png")
OUTER_WALL_IMAGE = pygame.image.load("textures/outerWall.png")
HEARTH_LOGO = pygame.image.load("textures/hearth.png")
SWEET_BAR_LOGO = pygame.image.load("textures/sweet.png")

class Tile(pygame.sprite.Sprite):

    def __init__(self, image, x, y):

        super().__init__()

        self.image = image
        self.image.set_colorkey((0, 0, 0))
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
                
                if (MAP[tileY][tileX] == 1):
                    tile = Tile(WALL_IMAGE, tileX, tileY)

                elif (MAP[tileY][tileX] == 2):
                    tile = Tile(WINDOW_IMAGE, tileX, tileY)

                elif (MAP[tileY][tileX] == 3):
                    tile = Tile(OUTER_WALL_IMAGE, tileX, tileY)

                else:
                    tile = Tile(TILE_IMAGE, tileX, tileY)

                self.tileList[tileX].append(tile)
                self.add(tile)