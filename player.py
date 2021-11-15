import pygame

PLAYER_TEXTURE_0 = pygame.image.load("textures/player0.png"); PLAYER_TEXTURE_0.set_colorkey((0,0,0))
PLAYER_TEXTURE_1 = pygame.image.load("textures/player1.png"); PLAYER_TEXTURE_1.set_colorkey((0,0,0))
PLAYER_TEXTURE_2 = pygame.image.load("textures/player2.png"); PLAYER_TEXTURE_2.set_colorkey((0,0,0))


ANIM = [
    PLAYER_TEXTURE_1,
    PLAYER_TEXTURE_0,
    PLAYER_TEXTURE_2
]

class Player(pygame.sprite.Sprite):

    def __init__(self, board, x, y):

        super().__init__()

        self.board = board

        self.image = PLAYER_TEXTURE_0
        self.rect = self.image.get_rect()

        self.speed = 0.0005 # tiles per tick

        self.x = x
        self.y = y

        self.rect.x = x * 32
        self.rect.y = y * 32

        self.tickStartTime = pygame.time.get_ticks()
        self.rotation = 0

        self.package = 0


    def updateStill(self):
        self.image = pygame.transform.rotate(PLAYER_TEXTURE_0, self.rotation)
        
    def moveRight(self):

        currentTime = pygame.time.get_ticks()

        if (currentTime - self.tickStartTime > 100):
            self.x += 1
            self.tickStartTime = currentTime
            self.image = pygame.transform.rotate(ANIM[self.x % len(ANIM)], 270)
            self.rotation = 270

            if (self.board.checkCollision(self.x, self.y, (1, 0), self.caffinated)):
                self.x -= 1
            self.rect.x = self.x * 32

    def moveLeft(self):

        currentTime = pygame.time.get_ticks()

        if (currentTime - self.tickStartTime > 100):
            self.x -= 1
            self.tickStartTime = currentTime
            self.image = pygame.transform.rotate(ANIM[self.x % len(ANIM)], 90)
            self.rotation = 90

            if (self.board.checkCollision(self.x, self.y, (-1, 0), self.caffinated)):
                self.x += 1

            self.rect.x = self.x * 32
    def moveUp(self):

        currentTime = pygame.time.get_ticks()

        if (currentTime - self.tickStartTime > 100):
            self.y -= 1
            self.tickStartTime = currentTime
            self.image = pygame.transform.rotate(ANIM[self.y % len(ANIM)], 0)
            self.rotation = 0
        
            if (self.board.checkCollision(self.x, self.y, (0, -1), self.caffinated)):
                self.y += 1
            self.rect.y = self.y * 32
    
    def moveDown(self):

        currentTime = pygame.time.get_ticks()

        if (currentTime - self.tickStartTime > 100):
            self.y += 1
            self.tickStartTime = currentTime
            self.image = pygame.transform.rotate(ANIM[self.y % len(ANIM)], 180)
            self.rotation = 180
        
            if (self.board.checkCollision(self.x, self.y, (0, 1), self.caffinated)):
                self.y -= 1
            self.rect.y = self.y * 32


