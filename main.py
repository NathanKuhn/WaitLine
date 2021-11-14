import pygame
import random
from player import Player
from board import Board
from gameMap import MAP
import element
from sign import Sign

BOARD_WIDTH = len(MAP)

def main():

    pygame.init()    
    screen = pygame.display.set_mode((BOARD_WIDTH * 32, BOARD_WIDTH * 32))

    all_sprites_list = pygame.sprite.Group()

    board = Board(24, 24)

    for _ in range(20):
        x = random.randrange(1, BOARD_WIDTH - 1)
        y = random.randrange(1, BOARD_WIDTH - 1)
        board.addTable(x, y)
    
    all_sprites_list.add(board.sprites())

    player = Player(board, 1, 1)
    all_sprites_list.add(player)

    all_sprites_list.add(Sign(pygame.image.load("textures/sweet.png"), 220, 170, 200, 120, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/streats.png"), 600, 220, 200, 100, 270))
    all_sprites_list.add(Sign(pygame.image.load("textures/Hearth.png"), 220, 340, 200, 100, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/balance.png"), 550, 620, 180, 80, 0))



    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 0, 0))

        if (pygame.key.get_pressed()[pygame.K_w]):
            player.moveUp()
        elif (pygame.key.get_pressed()[pygame.K_s]):
            player.moveDown()
        elif (pygame.key.get_pressed()[pygame.K_d]):
            player.moveRight()
        elif (pygame.key.get_pressed()[pygame.K_a]):
            player.moveLeft()
        else:
            player.updateStill()

        all_sprites_list.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()