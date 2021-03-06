import pygame
import random
from player import Player
from board import Board
from gameMap import MAP
import element
from sign import Sign
import board
from threading import Thread
import getData

BOARD_WIDTH = len(MAP)

def main():

    pygame.init()    
    screen = pygame.display.set_mode((BOARD_WIDTH * 32, BOARD_WIDTH * 32))

    all_sprites_list = pygame.sprite.Group()

    board = Board(24, 24)

    done = False

    def updateFoodScores():

        while not done:
            data = getData.logData()
            for key, value in data.items():
                board.foodScores[key] = int(data[key]) + 1

    dataThread = Thread(target=updateFoodScores)
    dataThread.start()

    for _ in range(20):
        x = random.randrange(1, BOARD_WIDTH - 1)
        y = random.randrange(1, BOARD_WIDTH - 1)
        if (x, y) not in board.deliveryLocations.values() and (x-1, y) not in board.deliveryLocations.values() and (x+1, y) not in board.deliveryLocations.values() and (x, y+1) not in board.deliveryLocations.values() and (x, y-1) not in board.deliveryLocations.values():
            board.addTable(x, y)

    all_sprites_list.add(board.sprites())

    player = Player(board, 1, 1, True)
    all_sprites_list.add(player)

    players = []
    for i in range(10):
        x = random.randrange(1, BOARD_WIDTH-1)
        y = random.randrange(1, BOARD_WIDTH-1)
        if MAP[y][x] == 0 and board.elements[y][x] == 0:
            players.append(Player(board, x, y, False))
            all_sprites_list.add(players[-1])
            players[-1].caffinated = False

    all_sprites_list.add(Sign(pygame.image.load("textures/sweet.png"), 220, 170, 200, 120, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/streats.png"), 600, 220, 200, 100, 270))
    all_sprites_list.add(Sign(pygame.image.load("textures/Hearth.png"), 220, 340, 200, 100, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/balance.png"), 550, 620, 180, 80, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/brunch.png"), 110, 630, 200, 80, 0))
    all_sprites_list.add(Sign(pygame.image.load("textures/noodles.png"), 320, 630, 150, 60, 0))


    caffine_timer = pygame.time.get_ticks()

    score = 0
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 0, 0))

        if pygame.time.get_ticks() < caffine_timer + 3000:
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

        if (pygame.key.get_pressed()[pygame.K_q]):
            player.package = 0
        
        for (food, x, y) in [
            board.burrito.getPos(),
            board.iceCream.getPos(),
            board.leaf.getPos(),
            board.pizza.getPos(),
            board.burger.getPos(),
            board.noodles.getPos()
        ]:
            if (x, y) == (player.x, player.y):
                player.package = food.foodType
                food.setPos(25, 25)
                board.placeFoodItem(food.foodType)

        for key, value in board.deliveryLocations.items():
            if (player.x, player.y) == value:
                if (player.package == key):
                    score += board.foodScores[key]
                    caffine_timer = pygame.time.get_ticks()
                    board.changeAllFoods()
                    player.package = 0

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

        for key, value in board.deliveryLocations.items():
            font = pygame.font.SysFont(None, 25)
            k = board.deliveryLocations[key]
            
            img = font.render(str(board.foodScores[key]), True, (10,100,10))
            screen.blit(img, (value[0]*32 + 6, value[1]*32 + 9))

        font = pygame.font.SysFont(None, 40)
        img = font.render("Score: " + str(score), True, (0,0,0))
        screen.blit(img, (65, 5))

        pygame.display.flip()

if __name__ == "__main__":
    main()