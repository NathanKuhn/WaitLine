import pygame
from gameMap import MAP
from enum import Enum

BURRITO_IMAGE = pygame.image.load("textures/burrito.png"); BURRITO_IMAGE.set_colorkey((0, 0, 0))
ICE_CREAM_IMAGE = pygame.image.load("textures/icecream.png"); ICE_CREAM_IMAGE.set_colorkey((0, 0, 0))
LEAF_IMAGE = pygame.image.load("textures/leaf.png"); LEAF_IMAGE.set_colorkey((255, 255, 255))
PIZZA_IMAGE = pygame.image.load("textures/pizza.png"); PIZZA_IMAGE.set_colorkey((255, 255, 255))
BURGER_IMAGE = pygame.image.load("textures/hamburger.png"); BURGER_IMAGE.set_colorkey((0, 0, 0))
NOODLES_IMAGE = pygame.image.load("textures/uwucat.png"); NOODLES_IMAGE.set_colorkey((255, 255, 255))

class FoodType(Enum):
    BURRITO = 0
    ICE_CREAM = 1
    LEAF = 2
    PIZZA = 3
    BURGER = 4
    NOODLES = 5

FOOD_IMAGES = {
    FoodType.BURRITO : BURRITO_IMAGE,
    FoodType.ICE_CREAM : ICE_CREAM_IMAGE,
    FoodType.LEAF : LEAF_IMAGE,
    FoodType.PIZZA : PIZZA_IMAGE,
    FoodType.BURGER : BURGER_IMAGE,
    FoodType.NOODLES : NOODLES_IMAGE
}

class Food(pygame.sprite.Sprite):

    def __init__(self, foodType, x, y):
        super().__init__()

        self.foodType = foodType

        self.image = FOOD_IMAGES[foodType]
        self.rect = self.image.get_rect()

        self.rect.x = x * 32
        self.rect.y = y * 32

        self.x = x
        self.y = y
    
    def getPos(self):
        return (self, self.x, self.y)
    
    def setPos(self, x, y):
        self.x = x
        self.y = y

        self.rect.x = x * 32
        self.rect.y = y * 32
