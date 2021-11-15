import pygame
from gameMap import MAP
import element
import food

TILE_IMAGE = pygame.image.load("textures/tile.png")
WALL_IMAGE = pygame.image.load("textures/wall.png")
WINDOW_IMAGE = pygame.image.load("textures/window.png")
OUTER_WALL_IMAGE = pygame.image.load("textures/outerWall.png")
DELIVERY = pygame.image.load("textures/delivery.png")
DELIVERY_LOCATIONS = [(10, 4), (10, 14), (5, 18), (13, 18), (20, 18), (17, 10)]

foodScores = {
    food.FoodType.ICE_CREAM : 10,
    food.FoodType.BURRITO : 10,   
    food.FoodType.BURGER : 10,
    food.FoodType.NOODLES : 10,
    food.FoodType.PIZZA : 10,
    food.FoodType.LEAF : 10
}

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

        self.deliveryLocations = DELIVERY_LOCATIONS


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
                
                if (tileX == 10 and tileY == 4):
                    tile = Tile(DELIVERY, tileX, tileY)
                elif (tileX == 10 and tileY == 14):
                    tile = Tile(DELIVERY, tileX, tileY)
                elif (tileX == 5 and tileY == 18):
                    tile = Tile(DELIVERY, tileX, tileY)
                elif (tileX == 13 and tileY == 18):
                    tile = Tile(DELIVERY, tileX, tileY)
                elif (tileX == 20 and tileY == 18):
                    tile = Tile(DELIVERY, tileX, tileY)
                elif (tileX == 17 and tileY == 10):
                    tile = Tile(DELIVERY, tileX, tileY)

                self.tileList[tileX].append(tile)
                self.add(tile)

        self.elements = [[0 for _ in range(tilesX)] for _ in range(tilesY)]

    def addTable(self, x, y):

        if MAP[y][x] == 0 and self.elements[y][x] == 0:
            table = element.Table(x, y)
            self.elements[y][x] = table
            self.add(table)

            if MAP[y-1][x] == 0 and self.elements[y-1][x] == 0:
                chair = element.Chair(x,y-1)
                self.elements[y-1][x] = chair
                self.add(chair)

            if MAP[y+1][x] == 0 and self.elements[y+1][x] == 0:
                chair = element.Chair(x,y+1,180)
                self.elements[y+1][x] = chair
                self.add(chair)

            if MAP[y][x+1] == 0 and self.elements[y][x+1] == 0:
                chair = element.Chair(x+1,y,270)
                self.elements[y][x+1] = chair
                self.add(chair)
                
            if MAP[y][x-1] == 0 and self.elements[y][x-1] == 0:
                chair = element.Chair(x-1,y,90)
                self.elements[y][x-1] = chair
                self.add(chair)

    def checkCollision(self, x, y, direction, moveItems=False):
        if (x < 0 or x >= len(MAP) or y < 0 or y >= len(MAP[0])):
              return True

        if (moveItems):
            if (self.pushElement(x, y, direction)):
                return True

        return (MAP[y][x] != 0 or (self.elements[y][x] != 0 and not moveItems))
    
    def pushElement(self, x, y, direction):

        if (self.elements[y][x] == 0):
            return False

        xd = direction[0] + x
        yd = direction[1] + y

        if (self.elements[yd][xd] != 0):
            if (not self.pushElement(xd, yd, direction)):
                return True

        if (self.elements[yd][xd] == 0 and MAP[yd][xd] == 0):
            self.elements[yd][xd] = self.elements[y][x]
            self.elements[y][x] = 0
            self.updateElements()
            return False
        
        return True
    
    def updateElements(self):

        for y in range(len(self.elements)):
            for x in range(len(self.elements[0])):
                if (issubclass(type(self.elements[y][x]), element.GameElement)):
                    self.elements[y][x].rect.x = x * 32
                    self.elements[y][x].rect.y = y * 32

#    def displayText(self, x, y, size, text):
        