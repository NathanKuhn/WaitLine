import pygame


class Sign (pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, rot):
        super().__init__()
        image.set_colorkey((255,255,255))
        self.image = pygame.transform.scale(image, (width, height))
        self.image = pygame.transform.rotate(self.image, rot)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    