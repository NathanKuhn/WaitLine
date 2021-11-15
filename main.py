import pygame
import random
from player import Player
from board import Board
from gameMap import MAP
import element
from sign import Sign
import board

BOARD_WIDTH = len(MAP)

def main():

    pygame.init()    
    screen = pygame.display.set_mode((BOARD_WIDTH * 32, BOARD_WIDTH * 32))

    all_sprites_list = pygame.sprite.Group()

    board = Board(24, 24)

    for _ in range(20):
        x = random.randrange(1, BOARD_WIDTH - 1)
        y = random.randrange(1, BOARD_WIDTH - 1)
        if (x, y) not in board.deliveryLocations and (x-1, y) not in board.deliveryLocations and (x+1, y) not in board.deliveryLocations and (x, y+1) not in board.deliveryLocations and (x, y-1) not in board.deliveryLocations:
            board.addTable(x, y)

    all_sprites_list.add(board.sprites())

    player = Player(board, 1, 1)
    all_sprites_list.add(player)

    players = []
    for i in range(10):
        x = random.randrange(1, BOARD_WIDTH-1)
        y = random.randrange(1, BOARD_WIDTH-1)
        if MAP[y][x] == 0 and board.elements[y][x] == 0:
            players.append(Player(board, x, y))
            all_sprites_list.add(players[-1])
            players[-1].caffinated = False



    all_sprites_list.add(Sign(pygame.image.load("textures/sweet.png"), 220, 170, 200, 120, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/streats.png"), 600, 220, 200, 100, 270))
    all_sprites_list.add(Sign(pygame.image.load("textures/Hearth.png"), 220, 340, 200, 100, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/balance.png"), 550, 620, 180, 80, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/brunch.png"), 110, 630, 200, 80, 0))

    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 0, 0))

        if pygame.time.get_ticks() < 3000:
            player.caffinated = True
        else:
            player.caffinated = False

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

        if pygame.time.get_ticks() & 500 == 0:
            for i in range(len(players)):
                p = players[i]
                j = random.randrange(0,4)
                if j==0:
                    p.moveUp()
                elif j==1:
                    p.moveDown()
                elif j==2:
                    p.moveLeft()
                else:
                    p.moveRight()


        all_sprites_list.draw(screen)

        for key, values in board.deliveryLocations.items():
            font = pygame.font.SysFont(None, 25)
            img = font.render(Board.foodScores[i], True, (0,0,0))
            screen.blit(img, (board.deliveryLocations[key][0]*32, board.deliveryLocations[key][0]*32))

        pygame.display.flip()

if __name__ == "__main__":
    main()