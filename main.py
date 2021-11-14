import pygame
from player import Player
from board import Board
from gameMap import MAP
import element

BOARD_WIDTH = len(MAP)

def main():

    pygame.init()    
    screen = pygame.display.set_mode((BOARD_WIDTH * 32, BOARD_WIDTH * 32))

    all_sprites_list = pygame.sprite.Group()

    board = Board(24, 24)
    all_sprites_list.add(board.sprites())

    player = Player(1, 1)
    all_sprites_list.add(player)

    chair1 = element.Chair(3, 3, 0)
    chair2 = element.Chair(2, 4, 90)
    chair3 = element.Chair(3, 5, 180)
    chair4 = element.Chair(4, 4, 270)

    table = element.Table(3, 4)

    all_sprites_list.add(chair1, chair2, chair3, chair4, table)

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

        if (pygame.key.get_pressed()[pygame.K_d]):
            player.moveRight()
        elif (pygame.key.get_pressed()[pygame.K_a]):
            player.moveLeft()

        all_sprites_list.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()