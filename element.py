import pygame

TABLE_TEXTURE = pygame.image.load("textures/table.png")
CHAIR_TEXTURE = pygame.image.load("textures/chair.png")

class GameElement(pygame.sprite.Sprite):

    def __init__(self, image, x, y, rot=0):
        super().__init__()

        self.image = pygame.transform.rotate(image, rot)
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.x = x * 32
        self.rect.y = y * 32

class Table(GameElement):

    def __init__(self, x, y, rot=0):
        super().__init__(TABLE_TEXTURE, x, y, rot)

class Chair(GameElement):

    def __init__(self, x, y, rot=0):
        super().__init__(CHAIR_TEXTURE, x, y, rot)