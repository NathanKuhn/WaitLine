import pygame
from gameMap import checkCollision

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.Surface([32, 32])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.speed = 0.0001 # tiles per tick

        self.x = x
        self.y = y

        self.rect.x = x * 32
        self.rect.y = y * 32

        self.tickStartTime = pygame.time.get_ticks()
    
    def moveRight(self):

        currentTime = pygame.time.get_ticks()

        if (checkCollision(self.x + 1, self.y)):
            return

        if (currentTime - self.tickStartTime > 100):
            self.x += 1
            self.rect.x = self.x * 32
            self.tickStartTime = currentTime

    def moveLeft(self):

        currentTime = pygame.time.get_ticks()

        if (checkCollision(self.x - 1, self.y)):
            return

        if (currentTime - self.tickStartTime > 100):
            self.x -= 1
            self.rect.x = self.x * 32
            self.tickStartTime = currentTime

    def moveUp(self):

        currentTime = pygame.time.get_ticks()

        if (checkCollision(self.x, self.y - 1)):
            return

        if (currentTime - self.tickStartTime > 100):
            self.y -= 1
            self.rect.y = self.y * 32
            self.tickStartTime = currentTime

    def moveDown(self):

        currentTime = pygame.time.get_ticks()

        if (checkCollision(self.x, self.y + 1)):
            return

        if (currentTime - self.tickStartTime > 100):
            self.y += 1
            self.rect.y = self.y * 32
            self.tickStartTime = currentTime


